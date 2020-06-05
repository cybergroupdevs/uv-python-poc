import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';
@Injectable({
  providedIn: 'root'
})
export class TransactionDetailService {

  constructor(private http: HttpClient,private router: Router) { }
  get(transactionId){
    return this.http.get(`http://localhost:5000/transaction/${transactionId}`)
  }
}
