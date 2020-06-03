import { Component, OnInit } from '@angular/core';
import {MatDialog, MatDialogRef, MAT_DIALOG_DATA} from '@angular/material/dialog';
import { CommissionService } from '../service/commission.service'

const transactionData: Transaction[] = [
  {class: '0026', sku: '80000', retail: '16.00', qun:'1', desc:'PAINT WAIST-SEAT',qtrtn:''},
  {class: '0026', sku: '80000', retail: '13.00', qun:'1', desc:'PAINT PLAIN BOTTOM',qtrtn:''}
]

@Component({
  selector: 'transaction-detail',
  templateUrl: './transaction-detail.component.html',
  styleUrls: ['./transaction-detail.component.css']
})
export class TransactionDetailComponent implements OnInit {

  constructor(public dialog:MatDialog, private _commissionSerivce: CommissionService) { }

  ngOnInit() {
  }

  columnHeadings :string[] = ['class','sku','retail','qun','desc','qtrtn'];

  commissionData : Boolean = false;
  
  data = transactionData;

  commissionDetails(){
    this._commissionSerivce.get('2996*25*7652').subscribe((data) =>{
      this.commissionData = true;
      this.data = data['commissionList']
      this.columnHeadings = Object.keys(this.data[0])
    })
  }

  customerDialog(): void {
    const dialogRef = this.dialog.open(customerDialog, {
      width: '60%',
      
    });
}
consultantDialog():void{
  const dialogRef =this.dialog.open(consultantDialog,{
    width:'450px',
  });
}
}
@Component({
  selector: 'dialog-overview-example-dialog',
  templateUrl: 'customerDialog.html',
})
export class customerDialog {
  constructor(
    public dialogRef: MatDialogRef<customerDialog>,
    ) {}
  onNoClick(): void {
    this.dialogRef.close();
  }
}
@Component({
  selector: 'dialog-overview-example-dialog',
  templateUrl: 'consultantDialog.html',
})
export class consultantDialog {
  constructor(
    public dialogRef: MatDialogRef<consultantDialog>,
    ) {}
  onNoClick(): void {
    this.dialogRef.close();
  }
}
export interface Transaction{
  class: String,
  sku: String,
  retail: String,
  qun: String,
  desc: String,
  qtrtn: String
}
