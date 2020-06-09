import { Component, OnInit } from '@angular/core';
import { OrderDetailService } from '../service/order-detail.service';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-order',
  templateUrl: './order.component.html',
  styleUrls: ['./order.component.css'],
})
export class OrderComponent implements OnInit {
  constructor(
    private orderDetailService: OrderDetailService,
    private activatedRoute: ActivatedRoute
  ) {}
  orderNo: string;
  shipDate;
  shipTo: string;
  method: string;
  address: string;
  carrier: string;
  csz: string;
  traceNo: number;
  commentLabel: number;
  audit: string;
  returnAddress: string;
  email: string;
  transactionId;
  errorMessage;
  ngOnInit() {
    this.activatedRoute.queryParams.subscribe((params) => {
      let transactionHeaderDetails = JSON.parse(params['transactionData']);
      this.transactionId =
        transactionHeaderDetails.customerDetails['transactionId'];
    });

    this.orderDetailService.get(this.transactionId).subscribe(
      (res: any) => {
        this.setValues(res['orderDetail']);
      },
      (error) => {
        this.errorMessage = error.error['error'];
      }
    );
  }
  setValues(data) {
    this.orderNo = data.orderNo;
    this.shipDate = data.shipDate;
    this.method = data.method;
    this.address = data.shipToAddress;
    this.carrier = data.carrier;
    this.csz = data.csz;
    this.traceNo = data.traceNo;
    this.commentLabel = data.commentLabel;
    this.audit = data.auditFlag;
    this.returnAddress = data.returnIds;
    this.email = data.email;
  }
}
