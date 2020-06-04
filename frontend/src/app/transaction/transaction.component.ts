import { Component, OnInit } from '@angular/core';
import { CommissionService } from '../service/commission.service';
import { Router , ActivatedRoute, NavigationExtras} from '@angular/router';


@Component({
  selector: 'app-transaction',
  templateUrl: './transaction.component.html',
  styleUrls: ['./transaction.component.css']
})
export class TransactionComponent implements OnInit {
  data;
  transactionHeading=[];
  transactionData;
  constructor(private _commissionService: CommissionService, private activatedRoute: ActivatedRoute) { }

  ngOnInit() {
    this.activatedRoute.queryParams.subscribe(params => {
      this.data = JSON.parse(params["user"]);
      this.transactionData = this.data['transactionDetails'];
      this.transactionHeading = Object.keys(this.transactionData[0])
    });
  }

}
