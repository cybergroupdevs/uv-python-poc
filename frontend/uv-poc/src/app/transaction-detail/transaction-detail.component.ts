import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'transaction-detail',
  templateUrl: './transaction-detail.component.html',
  styles: [],
})
export class TransactionDetailComponent implements OnInit {
  constructor(private activatedRoute: ActivatedRoute) {}
  headerData;

  ngOnInit() {
    this.activatedRoute.queryParams.subscribe((params) => {
      this.headerData = JSON.parse(params['transactionData']);
    });
  }
}
