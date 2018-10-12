import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { ClassifyService } from '../../services/classify.service';

@Component({
  selector: 'app-main-view',
  templateUrl: './main-view.component.html',
  styleUrls: ['./main-view.component.scss']
})
export class MainViewComponent implements OnInit {

  form: FormGroup;
  taggedSentence: any[];
  disabledBtn: boolean;
  meaning: string;
  loading: boolean = false;
  sentence: string;

  tagged = false;
  greetings = false;

  constructor(
    private formBuilder: FormBuilder,
    private classifyService: ClassifyService,

  ) { }

  ngOnInit() {
    this.form = this.formBuilder.group({
      sentence: ['', [Validators.required, Validators.pattern(/[\s\S]*manga+[\s\S]+/)]]
    })
    this.form.statusChanges.subscribe(
      status => {
        if (status == "VALID") {
          this.disabledBtn = false;
        } else {
          this.disabledBtn = true;
        }
      }
    )

    this.classifyService.response.subscribe(
      value => {
        this.taggedSentence = value;
        this.setMeaning(this.taggedSentence);
        this.loading = false;
        this.form.reset();
      }
    )
  }

  setMeaning(array) {
    array.forEach(el => {
      if (el[0].includes('manga') || el[0].includes('mangas')) {
        if (el[1].includes('n+fruta')) {
          this.meaning = 'Fruta'
        } else {
          this.meaning = 'Roupa'
        }
      }
    });
  }

  submit() {
    if (this.form.valid) {
      this.loading = true;
      this.tagged = true;
      this.classifyService.classify(this.form.controls.sentence.value);
      this.sentence = this.form.controls.sentence.value;
    }
  }

  setLoading(event) {
    this.loading = event;
  }

  resetTagged(event) {
    this.tagged = event;
  }

  setGreetings(event){
    this.greetings = event;

    setTimeout(() => {
      this.greetings = false;
    }, 10000);
  }

}
