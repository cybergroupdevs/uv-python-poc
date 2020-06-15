import { ActivatedRoute } from '@angular/router';
import { Component, OnInit } from '@angular/core';
import { DiscountService } from '../service/discount.service';
import { RefundService } from '../service/refund.service';

@Component({
  selector: 'transaction-detail',
  templateUrl: './transaction-detail.component.html',
  styleUrls: ['./transaction-detail.component.css'],
})

export class TransactionDetailComponent implements OnInit {
  constructor(
    private activatedRoute: ActivatedRoute,
    private refundService: RefundService
  ) {}
  headerData;

  ngOnInit() {
    this.activatedRoute.queryParams.subscribe((params) => {
      this.headerData = JSON.parse(params['transactionData']);
    });
  }

  showRefundDetails() {
    this.refundService
      .refundDetails(this.transactionId)
      .subscribe((res: any) => {
        this.refundManagerName = res.refundData['refundMgrName'];
        this.refundTicketNumber = res.refundData['ticketNumber'];
      });
  }
  
  showDiscountDetails() {
    this.discountService.get(this.transactionId).subscribe((res: any) => {
      this.discountPct = res.discountDetails['pct'];
      this.discountSubtotal = res.discountDetails['subTotal'];
    });
  }
}
