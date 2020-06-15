import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-transaction',
  templateUrl: './transaction.component.html',
  styles: [],
})
export class TransactionComponent implements OnInit {
  data;
  transactionHeading = [];
  transactionData;
  constructor(private activatedRoute: ActivatedRoute) {}

  ngOnInit() {
    this.activatedRoute.queryParams.subscribe((params) => {
      this.data = JSON.parse(params['transactionData']);
      this.transactionData = this.data['transactionDetails'];
      this.transactionHeading = Object.keys(this.transactionData[0]);
    });
  }
}
