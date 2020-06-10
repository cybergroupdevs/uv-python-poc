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
  dataLength: any;
  customerDetails = new Map();
  customerkeys = [
    'Phone number',
    'First name',
    'Last name',
    'Address',
    'City',
    'Zip-code',
    'Alternate Number',
    'PFID',
  ];
  constructor(
    private _customerService: CustomerService,
    private _commissionService: CommissionService
  ) {}

  ngOnInit(): void {
    this._commissionService.activeTab.subscribe((data) => {
      if (data.toString() == 'Customer') {
        this.customerId = '9782';
        this._customerService.get(this.customerId).subscribe((res: any) => {
          this.customerData = Object.values(res);
          this.dataLength = this.customerData.length;
          for (let values = 0; values < this.dataLength; values++) {
            this.customerDetails.set(
              this.customerkeys[values],
              this.customerData[values]
            );
          }
        });
      }
    });
  }
}
