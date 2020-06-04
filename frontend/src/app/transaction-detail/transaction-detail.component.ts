import { Component, OnInit, Inject } from '@angular/core';
import { CommissionService } from '../service/commission.service';
import { MatDialog, MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog';
import { CustomerService } from '../service/customer.service'
import { CustomerHistoryComponent } from '../customer-history/customer-history.component'
import { FormGroup, FormControl, Validators } from '@angular/forms';

@Component({
  selector: 'transaction-detail',
  templateUrl: './transaction-detail.component.html',
  styleUrls: ['./transaction-detail.component.css']
})
export class TransactionDetailComponent implements OnInit {

  constructor(private _commissionService: CommissionService, public dialog: MatDialog, private _CustomerService: CustomerService) { }
  customerData = []
  phone: string
  count: Number
  phoneNoForm = new FormGroup({
    phoneNo: new FormControl('',[Validators.required]),
  })
  ngOnInit() { }

  onChangeTab(event) {
    this._commissionService.changeActiveTab(event['tab']['textLabel'])
  }
  openDialog(): void {
    let pageIndex = 0
    let pageSize = 5
    this.phone = this.phoneNoForm.value["phoneNo"]
    this._CustomerService.list(this.phone, pageIndex, pageSize).subscribe((res: any) => {
      this.customerData = res["customerHistory"]
      this.count = res['count']
      const dialogRef = this.dialog.open(CustomerHistoryComponent, {
        width: '800px',
        data: { 'customerData': this.customerData, "phoneNo": this.phone, "count": this.count }
      });
    })

  }
}
