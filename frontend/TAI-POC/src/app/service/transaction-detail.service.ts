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
  private message = new BehaviorSubject('First Message');
  sharedMessage = this.message.asObservable();
  private transactionData ;

  constructor(private http: HttpClient,private router: Router) { }
  getTransactionData(transactionId){
     this.http.get(`http://localhost:5000/transaction/${transactionId}`)
     .subscribe((res: any) => {
      // this.saveData(res)
      // console.log(res)
      let navigationExtras: NavigationExtras = {
        queryParams: {
            "user": JSON.stringify(res)
        }
      };
      // console.log(navigationExtras)
      this.router.navigate(["/transaction"],  navigationExtras);
      // this.router.navigate(['/transaction'] ,{state: {v: res}});
    },
    error  => {
      console.log(error)
      // return 0;
    })
  }
  saveData(data){
    this.transactionData = data;
    console.log(this.transactionData)
  }
}
