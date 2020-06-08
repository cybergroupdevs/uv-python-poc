import { Component, OnInit, Inject } from "@angular/core";
import { CustomerService } from "../service/customer.service";
import { PageEvent } from "@angular/material/paginator";
import {
  MatDialog,
  MatDialogRef,
  MAT_DIALOG_DATA,
} from "@angular/material/dialog";

@Component({
  selector: "app-customer-history",
  templateUrl: "./customer-history.component.html",
  styleUrls: ["./customer-history.component.css"],
})
export class CustomerHistoryComponent implements OnInit {
  customerHeading: any;
  pageSize = 5;
  pageEvent: PageEvent;
  pageIndex = 0;
  length: number;
  customerData: any;
  phoneNo: string;
  history: boolean;

  constructor(
    public dialogRef: MatDialogRef<CustomerHistoryComponent>,
    @Inject(MAT_DIALOG_DATA) public data: any,
    private _customerService: CustomerService
  ) {}

  ngOnInit(): void {
    this.length = this.data["count"];
    if (this.length == 0) {
      this.history = false;
      this.phoneNo = this.data["phoneNo"];
    } else {
      this.history = true;
      this.customerHeading = Object.keys(this.data["customerData"][0]);
      this.customerData = this.data["customerData"];
      this.phoneNo = this.data["phoneNo"];
    }
  }
  pagination(event) {
    this.pageIndex = event.pageIndex;
    this.pageSize = event.pageSize;
    let phone = this.phoneNo;
    this.paginateCustomer(phone);
  }
  paginateCustomer(phone) {
    this._customerService
      .list(phone, this.pageIndex, this.pageSize)
      .subscribe((res: any) => {
        this.customerData = res["customerHistory"];
      });
  }
}
