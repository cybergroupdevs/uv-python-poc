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
  length: Number;
  consultantData = [];
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
            this.keys = Object.keys(res);
            this.length = this.keys.length;
            this.keys.forEach((element) => {
              var data = {};
              data['type'] = element;
              data['value'] = res[element];
              this.consultantData.push(data);
              this.keys = Object.keys(this.consultantData[0]);
            });
          });
      }
    });
  }
}
