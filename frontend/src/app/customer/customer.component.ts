import { Component, OnInit } from '@angular/core';
import{CustomerService} from '../service/customer.service'

@Component({
  selector: 'app-customer',
  templateUrl: './customer.component.html',
  styleUrls: ['./customer.component.css']
})
export class CustomerComponent implements OnInit {
 customerId:string
 customerDetails:any
  constructor(
    private customerService: CustomerService
    ) {}
    ngOnInit(){
        
    }
    get(){
      this.customerId="9782"
        this.customerService.get("9782").subscribe((res:any)=>{
          console.log(res)
          this.customerDetails=Object.values(res[0])
        })
    }

}
