import { Component, OnInit, Inject } from '@angular/core';
import { CustomerService } from '../service/customer.service';
import { PageEvent } from '@angular/material/paginator';
import {
  MatDialog,
  MatDialogRef,
  MAT_DIALOG_DATA,
} from '@angular/material/dialog';
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
  history: boolean;
  count: Number;

  constructor(
    public dialogRef: MatDialogRef<CustomerHistoryComponent>,
    @Inject(MAT_DIALOG_DATA) public data: any,
    private _customerService: CustomerService,
    public dialog: MatDialog
  ) {}

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
    this.toggle = true;
    let pageIndex = 0;
    let pageSize = 5;
    this.phone = this.phoneNoForm.value['phoneNo'];
    if (this.phone != '') {
      this._customerService
        .list(this.phone, pageIndex, pageSize)
        .subscribe((res: any) => {
          console.log(res);
          this.customerData = res['customerHistory'];
          this.count = res['count'];
          if (this.count != 0) {
            this.history = true;
          }
        });
    }
  }
}
