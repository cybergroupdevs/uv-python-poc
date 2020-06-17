import { ActivatedRoute } from '@angular/router';
import { Component, OnInit } from '@angular/core';
import { CreditCardService } from '../service/credit-card.service';
import { DiscountService } from '../service/discount.service';
import { RefundService } from '../service/refund.service';
import { CommissionService } from '../service/commission.service';
import { CustomerHistoryComponent } from '../customer-history/customer-history.component';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { CustomerService } from '../service/customer.service';
import { MatDialog } from '@angular/material/dialog';

@Component({
  selector: 'transaction-detail',
  templateUrl: './transaction-detail.component.html',
  styleUrls: ['./transaction-detail.component.css'],
})
export class TransactionDetailComponent implements OnInit {
  constructor(
    private activatedRoute: ActivatedRoute,
    private creditCardService: CreditCardService,
    private discountService: DiscountService,
    private refundService: RefundService,
    private commissionService: CommissionService,
    public dialog: MatDialog
  ) {}
  headerData;
  cardDetails: any;
  creditCardHeading = [];
  transactionId: any;
  refundData: any;
  refundHeading: string[];
  discountData: any;
  discountHeading: string[];

  ngOnInit() {
    this.activatedRoute.queryParams.subscribe((params) => {
      this.headerData = JSON.parse(params['transactionData']);
      this.transactionId = this.headerData.customerDetails['transactionId']
    });

    this.commissionService.activeTab.subscribe((data) => {
      if (data.toString() == 'Credit card') {
        this.creditCardService
          .get(this.transactionId)
          .subscribe((res: any) => {
            this.cardDetails = res['cardDetails'];
            this.creditCardHeading = Object.keys(res['cardDetails'][0]);
          });
      } else if (data.toString() == 'Refund') {
        this.showRefundDetails();
      } else if (data.toString() == 'Discount') {
        this.showDiscountDetails();
      }
    });
  }

  showRefundDetails() {
    this.refundService
      .refundDetails(this.transactionId)
      .subscribe((res: any) => {
        this.refundData = [res.refundData];
        this.refundHeading = Object.keys(res.refundData);
      });
  }

  showDiscountDetails() {
    this.discountService
      .get(this.transactionId)
      .subscribe((res: any) => {
        this.discountData = [res.discountDetails];
        this.discountHeading = Object.keys(res.discountDetails);
      });
  }

  onChangeTab(event) {
    this.commissionService.changeActiveTab(event['tab']['textLabel']);
  }
  openDialog(): void {
    const dialogRef = this.dialog.open(CustomerHistoryComponent, {
      width: '800px',
    });
  }
}