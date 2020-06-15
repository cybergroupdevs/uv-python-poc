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
  customerData = {};
  customerKeys: any;
  constructor(
    private _customerService: CustomerService,
    private _commissionService: CommissionService
  ) {}

  ngOnInit(): void {
    this._commissionService.activeTab.subscribe((data) => {
      if (data.toString() == 'Customer') {
        this.customerId = '9782';
        this._customerService.get(this.customerId).subscribe((res: any) => {
          this.customerData['Phone number'] = res['phoneNo'];
          this.customerData['First name'] = res['firstName'];
          this.customerData['Last name'] = res['lastName'];
          this.customerData['Address'] = res['address'];
          this.customerData['City'] = res['city'];
          this.customerData['Zip code'] = res['zipCode'];
          this.customerData['PFID'] = res['pfid'];
          this.customerData['Alternate phone number'] = res['altPhoneNo'];
          this.customerKeys = Object.keys(this.customerData);
        });
      }
    });
  }
}
