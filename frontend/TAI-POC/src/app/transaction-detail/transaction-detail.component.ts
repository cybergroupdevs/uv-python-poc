import { Component, OnInit } from '@angular/core';
import { Router , ActivatedRoute, NavigationExtras} from '@angular/router';
import { map, filter } from 'rxjs/operators';
import {Observable} from 'rxjs';
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
private sub;
state$: Observable<object>;
  constructor(public dialog:MatDialog, private activatedRoute: ActivatedRoute) { }

  // ngOnInit() {
    // this.sub = this.activatedRoute
    // .data
    // .subscribe(v => console.log(v));
    // this.state$ = this.activatedRoute.paramMap
    // .pipe(map(() => window.history.state))
  // }
  ngOnInit(): void {

      this.activatedRoute.queryParams.subscribe(params => {
        console.log(JSON.parse(params["user"]));
      });
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
