import { Component, OnInit } from '@angular/core';
import {MatDialog, MatDialogRef, MAT_DIALOG_DATA} from '@angular/material/dialog';
import{CustomerService} from '../service/customer.service'

@Component({
  selector: 'app-customer',
  templateUrl: './customer.component.html',
  styleUrls: ['./customer.component.css']
})
export class CustomerComponent implements OnInit {
 customerId:string
  constructor(
    public dialogRef: MatDialogRef<CustomerComponent>,private customerService: CustomerService
    ) {}
    ngOnInit(){
        this.customerId="9782"
        this.customerService.get("9782").subscribe((res:any)=>{
        })
      
    }
  onNoClick(): void {
    this.dialogRef.close();
  }

}
