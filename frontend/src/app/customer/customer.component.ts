import { Component, OnInit,inject } from '@angular/core';
import{CustomerService} from '../service/customer.service'
import { CommissionService } from '../service/commission.service';
@Component({
  selector: 'app-customer',
  templateUrl: './customer.component.html',
  styleUrls: ['./customer.component.css']
})
export class CustomerComponent implements OnInit {
 customerId:string
 customerDetails:any
  customerkeys=["Phone number","First name","Last name","Address","City","Zip-code","Alternate Number","PFID"]
  constructor(
    private customerService: CustomerService ,private _commissionService: CommissionService
    ) {}
    ngOnInit(){
      this._commissionService.activeTab.subscribe((data) =>{
        if(data.toString() == 'Customer'){
          this.customerId="9782"
          this.customerService.get("9782").subscribe((res:any)=>{
            this.customerDetails=Object.values(res[0])
          })
        }
      })
    } 
}
