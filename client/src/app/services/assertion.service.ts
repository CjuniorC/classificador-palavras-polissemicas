import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { BehaviorSubject } from 'rxjs';

interface Response{
  success: boolean,
  message: string
}

@Injectable({
  providedIn: 'root'
})
export class AssertionService {

  private url = 'https://classificador-18ac0.firebaseapp.com/assertion';
  assert = new BehaviorSubject<Response>({success: false, message: ''});
  

  constructor(
    private http: HttpClient
  ) { }

  assertion(sentence, corpus){
    const headers = new HttpHeaders({'Access-Control-Allow-Origin':'*','Access-Control-Allow-MethodsGET':'POST, PATCH, PUT, DELETE, OPTIONS'})
    this.http.put<Response>(this.url,{sentence:sentence, corpus:corpus}, {headers})
    .subscribe(result => {
      this.assert.next(result);
    })
  }


}
