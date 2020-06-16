import { Component, OnInit, Inject } from '@angular/core';
import { CustomerService } from '../service/customer.service';
import { PageEvent } from '@angular/material/paginator';
import { FormGroup, FormControl, Validators } from '@angular/forms';

@Component({
  selector: 'app-customer-history',
  templateUrl: './customer-history.component.html',
  styleUrls: ['./customer-history.component.css'],
})
export class CustomerHistoryComponent implements OnInit {
  phoneNoForm = new FormGroup({
    phoneNo: new FormControl('', [Validators.required]),
  });
  toggle: boolean = false;
  phone: string;
  customerHeading: any;
  pageSize = 5;
  pageEvent: PageEvent;
  pageIndex = 0;
  length: number;
  customerData: [];
  history: boolean = false;
  empty: boolean = true;
  check: boolean = false;

  constructor(private _customerService: CustomerService) {}

  ngOnInit(): void {}
  pagination(event) {
    this.pageIndex = event.pageIndex;
    this.pageSize = event.pageSize;
    let phone = this.phone;
    this.paginateCustomer(phone);
  }
  paginateCustomer(phone) {
    this._customerService
      .list(phone, this.pageIndex, this.pageSize)
      .subscribe((res: any) => {
        this.customerData = res['customerHistory'];
      });
  }
  customerHistory() {
    this.history = false;
    let pageIndex = 0;
    let pageSize = 5;
    this.check = true;
    this.phone = this.phoneNoForm.value['phoneNo'];
    if (this.phone != '') {
      this.check = true;
      this._customerService
        .list(this.phone, pageIndex, pageSize)
        .subscribe((res: any) => {
          this.toggle = true;
          this.customerData = res['customerHistory'];
          this.customerHeading = Object.keys(res['customerHistory'][0]);
          this.length = res['count'];
          if (this.length != 0) {
            this.history = true;
          } else this.history = false;
        });
    } else this.toggle = !this.toggle;
  }
}
