import { Component, OnInit } from '@angular/core';
import { CommissionService } from '../service/commission.service';
import { Router , ActivatedRoute, NavigationExtras} from '@angular/router';
import { map, filter } from 'rxjs/operators';
import {Observable} from 'rxjs';
import { DiscountService } from '../service/discount.service'
import { RefundService } from '../service/refund.service'

@Component({
  selector: 'transaction-detail',
  templateUrl: './transaction-detail.component.html',
  styleUrls: ['./transaction-detail.component.css']
})
export class TransactionDetailComponent implements OnInit {

  constructor(private _commissionService: CommissionService, private activatedRoute: ActivatedRoute, private discountService: DiscountService, private refundService: RefundService) { }
  private headerData;
  transactionId;
  phoneNo;
  transactionType;
  name;
  operator;
  pfid;
  saleCns;
  rental;
  postedOn;
  discountPct;
  discountSubtotal:number;
  refundManagerName;
  refundTicketNumber;
  ngOnInit() {
    this.activatedRoute.queryParams.subscribe(params => {
      this.headerData = JSON.parse(params["user"]);
      this.setValues(this.headerData)
    });
   }

   setValues(details){
    this.transactionId = details.customerDetails['transactionId'];
    this.phoneNo = details.customerDetails['phoneNo'];
    this.transactionType = details.customerDetails['transactionType'];
    this.operator = details.customerDetails['operator'];
    this.name = details.customerDetails['name'];
    this.pfid = details.customerDetails['pfid'];
    this.saleCns = details.customerDetails['saleCns'];
    this.rental = details.customerDetails['rentalNo'];
    this.postedOn = details.customerDetails['date'];

  }
  showDiscountDetails(){
    this.discountService.get(this.transactionId)
    .subscribe((res:any)=>{
      this.discountPct = res.discountDetails['pct'];
      this.discountSubtotal = res.discountDetails['subTotal'];
    })
  }
  showRefundDetails(){
    this.refundService.get(this.transactionId)
    .subscribe((res:any)=>{
      this.refundManagerName = res.refundData['refundMgrName'];
      this.refundTicketNumber = res.refundData['ticketNumber'];
    })
  }
  onChangeTab(event){
    this._commissionService.changeActiveTab(event['tab']['textLabel'])
  }
}

