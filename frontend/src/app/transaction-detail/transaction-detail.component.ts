import { Component, OnInit,Inject } from '@angular/core';
import { CommissionService } from '../service/commission.service';
import {MatDialog, MatDialogRef, MAT_DIALOG_DATA} from '@angular/material/dialog';
import{CustomerService} from '../service/customer.service'
""

@Component({
  selector: 'transaction-detail',
  templateUrl: './transaction-detail.component.html',
  styleUrls: ['./transaction-detail.component.css']
})
export class TransactionDetailComponent implements OnInit {

  constructor(private _commissionService: CommissionService,public dialog:MatDialog,private _CustomerService:CustomerService) { }
  data=[]
  ngOnInit() { }

  onChangeTab(event){
    this._commissionService.changeActiveTab(event['tab']['textLabel'])
  }
  openDialog(): void {
    this._CustomerService.list("415-566-9525","0","5").subscribe((res:any)=>{
      this.data=res
    })
    const dialogRef = this.dialog.open(TransactionDetailComponent, {
      width: '250px',
      data: {data:this.data}
    });
  }
}
// @Component({
//   selector: 'customer-dialog',
//   templateUrl: '../customer-history/customer-history.html',
// })
// export class customerHistory {

//   constructor(
//     public dialogRef: MatDialogRef<customerHistory>,
//     @Inject(MAT_DIALOG_DATA) public data:any) {}

//   onNoClick(): void {
//     this.dialogRef.close();
//   }
// }
