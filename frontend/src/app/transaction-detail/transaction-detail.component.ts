import { Component, OnInit } from '@angular/core';
import { CommissionService } from '../service/commission.service';
import { Router , ActivatedRoute, NavigationExtras} from '@angular/router';
import { map, filter } from 'rxjs/operators';
import {Observable} from 'rxjs';

@Component({
  selector: 'transaction-detail',
  templateUrl: './transaction-detail.component.html',
  styleUrls: ['./transaction-detail.component.css']
})
export class TransactionDetailComponent implements OnInit {
  private sub;
  transactionId;
  phoneNo;
  transactionType;
  name;
  operator;
  pfid;
  saleCns;
  constructor(private _commissionService: CommissionService, private activatedRoute: ActivatedRoute) { }

  ngOnInit() {
    this.activatedRoute.queryParams.subscribe(params => {
      this.sub = JSON.parse(params["user"]);
      console.log(this.sub)
      this.setValues(this.sub)
    });
   }

   setValues(details){
    this.transactionId = details.customerDetails.transactionId;
    this.phoneNo = details.customerDetails.phoneNo;
    this.transactionType = details.customerDetails.transactionType;
    this.operator = details.customerDetails.operator;
    this.name = details.customerDetails.name;
    this.pfid = details.customerDetails.pfid;
    this.saleCns = details.customerDetails.saleCns;

  }
  onChangeTab(event){
    this._commissionService.changeActiveTab(event['tab']['textLabel'])
  }
}

