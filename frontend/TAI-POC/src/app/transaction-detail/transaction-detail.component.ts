import { Component, OnInit } from '@angular/core';
import {MatDialog, MatDialogRef, MAT_DIALOG_DATA} from '@angular/material/dialog';
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

  constructor(public dialog:MatDialog) { }

  ngOnInit() {
  }

  columnHeadings :string[] = ['class','sku','retail','qun','desc','qtrtn'];
  
  data = transactionData;

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
