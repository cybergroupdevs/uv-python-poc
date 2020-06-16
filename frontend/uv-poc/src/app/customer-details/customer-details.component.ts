import { Component, OnInit } from '@angular/core';
import { CustomerService } from '../service/customer.service';
import { CommissionService } from '../service/commission.service';

@Component({
  selector: 'app-customer-details',
  templateUrl: './customer-details.component.html',
  styles: [],
})
export class CustomerDetailsComponent implements OnInit {
  customerId: string;
  customerData: any;
  customerKeys: any;
  constructor(
    private _customerService: CustomerService,
    private _commissionService: CommissionService
  ) {}

  ngOnInit(): void {
    this._commissionService.activeTab.subscribe((data) => {
      if (data.toString() == 'Customer') {
        this.customerId = '4626';
        this._customerService.get(this.customerId).subscribe((res: any) => {
          this.customerData = [res];
          console.log(this.customerData);
          // this.customerData['Firstname'] = res['firstName'];
          // this.customerData['Lastname'] = res['lastName'];
          // this.customerData['Address'] = res['address'];
          // this.customerData['City'] = res['city'];
          // this.customerData['Zipcode'] = res['zipCode'];
          // this.customerData['PFID'] = res['pfid'];
          // this.customerData['Alternatephonenumber'] = res['altPhoneNo'];
          this.customerKeys = Object.keys(this.customerData[0]);
        });
      }
    });
  }
}
