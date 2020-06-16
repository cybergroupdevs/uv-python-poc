import { Component, OnInit } from '@angular/core';
import { ConsultantService } from '../service/consultant.service';
import { CommissionService } from '../service/commission.service';
@Component({
  selector: 'app-consultant-details',
  templateUrl: './consultant-details.component.html',
  styleUrls: ['./consultant-details.component.css'],
})
export class ConsultantDetailsComponent implements OnInit {
  transactionId: string;
  keys: any;
  data: any;
  length: Number;
  consultantHeadings = ['Type', 'Name'];
  details = {};
  values: any;
  consultant = [];
  constructor(
    private _consultantService: ConsultantService,
    private _commissionService: CommissionService
  ) {}

  ngOnInit(): void {
    this._commissionService.activeTab.subscribe((data) => {
      if (data.toString() == 'Consultant') {
        this.transactionId = '5334*24*1373';
        this._consultantService
          .get(this.transactionId)
          .subscribe((res: any) => {
            this.data = res;
            debugger;
            this.keys = Object.keys(res);
            this.length = this.keys.length;
            this.values = Object.values(res);
            for (let key = 0; key < this.length; key++) {
              this.details[this.consultantHeadings[key]] = this.values[key];
              this.consultant.push(this.details);
            }

            console.log(this.consultant);
          });
      }
    });
  }
}
