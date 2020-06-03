import { Injectable } from '@angular/core';
import { Router, NavigationExtras } from '@angular/router';
import { HttpClient } from '@angular/common/http';


@Injectable({
  providedIn: 'root'
})
export class OrderDetailService {

  constructor(private http: HttpClient,private router: Router) { }
  get(transactionId){
    return this.http.get(`http://localhost:5000/transaction/${transactionId}/order`)
  }
}
