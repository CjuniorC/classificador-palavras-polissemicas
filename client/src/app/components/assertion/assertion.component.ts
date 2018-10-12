import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';
import { AssertionService } from '../../services/assertion.service';

import {takeWhile} from 'rxjs/operators';


@Component({
  selector: 'app-assertion',
  templateUrl: './assertion.component.html',
  styleUrls: ['./assertion.component.scss']
})
export class AssertionComponent implements OnInit {

  @Input('result') meaning;
  @Input('sentence') sentence;

  @Output() loadingEmitter =  new EventEmitter();
  @Output() resultEmitter = new EventEmitter();
  @Output() greetingsEmitter = new EventEmitter();

  isAlive = true;

  constructor(
    private assertionService: AssertionService
  ) { }

  ngOnInit() {
    this.isAlive = true;
    this.assertionService.assert
    .subscribe(
      result => {
        this.loadingEmitter.emit(false);
        this.resultEmitter.emit(false);
    })
  }

  assertion(success: boolean){
    if(this.sentence){
      this.greetingsEmitter.emit(true);
      if(success){
        if(this.meaning == 'Fruta'){
          this.assertionService.assertion(this.sentence, 'frute');
        }else{
          this.assertionService.assertion(this.sentence, 'clothes');
        }
      }else{
        if(this.meaning == 'Fruta'){
          this.assertionService.assertion(this.sentence, 'clothes');
        }else{
          this.assertionService.assertion(this.sentence, 'frute');
        }
      }
    }
  }
}
