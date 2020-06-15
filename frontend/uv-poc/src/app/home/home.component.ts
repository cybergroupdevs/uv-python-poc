import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { TransactionDetailService } from '../service/transaction-detail.service';
import { Router, NavigationExtras } from '@angular/router';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})

export class HomeComponent implements OnInit {
  constructor(
    private router: Router,
    private transactionDetailService: TransactionDetailService
  ) {}
  transactionForm = new FormGroup({
    transactionId: new FormControl('', [Validators.required]),
  });
  errorMessage;
  ngOnInit(): void {}
  async getTransactionDetails() {
    var transactionId = this.transactionForm.value.transactionId;
    await this.transactionDetailService.get(transactionId).subscribe(
      (res: any) => {
        let navigationExtras: NavigationExtras = {
          queryParams: {
            transactionData: JSON.stringify(res),
          },
        };
        this.router.navigate(['/transaction'], navigationExtras);
      },
      (error) => {
        this.errorMessage = error.error['error'];
      }
    );
  }
}
