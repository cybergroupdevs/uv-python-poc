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
  transactionId;
  errorMessage;
  orderData;
  orderHeading;
  ngOnInit() {
    this.activatedRoute.queryParams.subscribe((params) => {
      let transactionHeaderDetails = JSON.parse(params['transactionData']);
      this.transactionId =
        transactionHeaderDetails.customerDetails['transactionId'];
    });

    this.orderDetailService.get(this.transactionId).subscribe(
      (res: any) => {
        this.orderData = [res.orderDetail];
        this.orderHeading = Object.keys(res.orderDetail);
      },
      (error) => {
        this.errorMessage = error.error['error'];
      }
    );
  }
}
