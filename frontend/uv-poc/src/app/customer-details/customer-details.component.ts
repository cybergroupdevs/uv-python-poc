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
        this.customerId = '9782';
        this._customerService.get(this.customerId).subscribe((res: any) => {
          this.customerData = res;
          this.customerData['Phone number'] = this.customerData['phoneNo'];
          this.customerData['First name'] = this.customerData['firstName'];
          this.customerData['Last name'] = this.customerData['lastName'];
          this.customerData['Address'] = this.customerData['address'];
          this.customerData['City'] = this.customerData['city'];
          this.customerData['Zip code'] = this.customerData['zipCode'];
          this.customerData['PFID'] = this.customerData['pfid'];
          this.customerData['Alternate phone number'] = this.customerData[
            'altPhoneNo'
          ];
          delete this.customerData['phoneNo'];
          delete this.customerData['firstName'];
          delete this.customerData['lastName'];
          delete this.customerData['address'];
          delete this.customerData['city'];
          delete this.customerData['zipCode'];
          delete this.customerData['pfid'];
          delete this.customerData['altPhoneNo'];
          this.customerKeys = Object.keys(this.customerData);
        });
      }
    });
  }
}
