import { Injectable } from '@angular/core';

import { HttpClient } from '@angular/common/http';
import { BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ClassifyService {

  response = new BehaviorSubject<any[]>([]);

  constructor(
    private http: HttpClient
  ) { }

  classify(sentence:string){
    this.http.get(`http://localhost:5000/${sentence}`)
    .subscribe(
      result => {
        this.response.next(result as any[]);
      }
    )
  }
}
