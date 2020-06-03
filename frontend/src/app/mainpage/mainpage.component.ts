import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, FormBuilder,  Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { TransactionDetailService } from '../service/transaction-detail.service'
@Component({
  selector: 'app-mainpage',
  templateUrl: './mainpage.component.html',
  styleUrls: ['./mainpage.component.css']
})
export class MainpageComponent implements OnInit {
  constructor(private router: Router, private fb: FormBuilder, private transactionDetailService: TransactionDetailService) { }
  transactionForm = new FormGroup({
    transactionId : new FormControl('',[Validators.required])
 });
  ngOnInit(): void {
  }
  async getTransactionDetails(){
    var transactionId = this.transactionForm.value.transactionId
     var data = await this.transactionDetailService.getTransactionData(transactionId)
  }
}
