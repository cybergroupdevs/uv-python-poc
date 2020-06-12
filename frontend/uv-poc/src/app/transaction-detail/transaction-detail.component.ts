import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { CreditCardService } from '../service/credit-card.service';

@Component({
  selector: 'transaction-detail',
  templateUrl: './transaction-detail.component.html',
  styles: [],
})
export class TransactionDetailComponent implements OnInit {
  constructor(
    private activatedRoute: ActivatedRoute,
    private creditCardService: CreditCardService
  ) {}
  headerData;
  cardDetails: any;
  creditCardHeading = [];

  ngOnInit() {
    this.activatedRoute.queryParams.subscribe((params) => {
      this.headerData = JSON.parse(params['transactionData']);
    });
  }
  showCreditCardDetails() {
    this.creditCardService
      .get(this.headerData.customerDetails['transactionId'])
      .subscribe((res: any) => {
        this.cardDetails = res['cardDetails'];
        this.creditCardHeading = Object.keys(res['cardDetails'][0]);
      });
  }
}
