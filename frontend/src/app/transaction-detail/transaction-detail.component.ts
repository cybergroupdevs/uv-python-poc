import { Component, OnInit } from '@angular/core';
import { CommissionService } from '../service/commission.service';

@Component({
  selector: 'transaction-detail',
  templateUrl: './transaction-detail.component.html',
  styleUrls: ['./transaction-detail.component.css']
})
export class TransactionDetailComponent implements OnInit {

  constructor(private _commissionService: CommissionService) { }

  ngOnInit() { }

  onChangeTab(event){
    this._commissionService.changeActiveTab(event['tab']['textLabel'])
  }
}

