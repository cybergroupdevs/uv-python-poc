import { Component, OnInit } from '@angular/core';
import { CustomerService } from '../service/customer.service';
import { CommissionService } from '../service/commission.service';
import { MatDialog } from '@angular/material/dialog';
import { CustomerHistoryComponent } from '../customer-history/customer-history.component';

@Component({
  selector: 'app-customer-details',
  templateUrl: './customer-details.component.html',
  styles: [],
})
export class CustomerDetailsComponent implements OnInit {
  customerId: string;
  customerData : any;
  customerKeys: any;
  constructor(
    private _customerService: CustomerService,
    private _commissionService: CommissionService,
    public dialog: MatDialog
  ) {}

  ngOnInit(): void {
    this._commissionService.activeTab.subscribe((data) => {
      if (data.toString() == 'Customer') {
        this.customerId = '646-863-0718';
        this._customerService.get(this.customerId).subscribe((res: any) => {
          this.customerData = [res];
          this.customerKeys = Object.keys(this.customerData[0]);
        });
      }
    });
  }
  openDialog(phoneNo): void {
    const dialogRef = this.dialog.open(CustomerHistoryComponent, {
      width: '600px',
      data: { phoneNo: phoneNo },
    });
  }
}
