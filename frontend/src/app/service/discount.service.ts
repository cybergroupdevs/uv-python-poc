import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../environments/environment';
import { BehaviorSubject } from 'rxjs';
import { Router, NavigationExtras } from '@angular/router';


@Injectable({
  providedIn: 'root'
})
export class DiscountService {

  constructor(private http: HttpClient,private router: Router) { }
  get(transactionId){
    return this.http.get(`http://localhost:5000/transaction/${transactionId}/discount`)
  }

}
