import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../environments/environment';
import { BehaviorSubject } from 'rxjs';
import { Router, NavigationExtras } from '@angular/router';
import { TransactionDetailComponent } from '../transaction-detail/transaction-detail.component'

@Injectable({
  providedIn: 'root'
})
export class TransactionDetailService {

  constructor(private http: HttpClient,private router: Router) { }
  getTransactionData(transactionId){
     this.http.get(`http://localhost:5000/transaction/${transactionId}`)
     .subscribe((res: any) => {
      let navigationExtras: NavigationExtras = {
        queryParams: {
            "user": JSON.stringify(res)
        }
      };
      this.router.navigate(["/transaction"],  navigationExtras);
    },
    error  => {
      console.log(error)
      // return 0;
    })
  }
}
