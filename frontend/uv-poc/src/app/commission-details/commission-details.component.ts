import { Component, OnInit, Input } from '@angular/core';
import { CommissionService } from '../service/commission.service';

@Component({
  selector: 'app-commission-details',
  templateUrl: './commission-details.component.html',
  styles: [],
})
export class CommissionDetailsComponent implements OnInit {
  constructor(private _commissionService: CommissionService) {}
  commissionData: any;
  commissionAmount: number;
  retailAmount: number;
  commissionHeading = [];
  commissionErrorMsg: string = null;
  @Input() transactionId : string;

  ngOnInit() {
    this._commissionService.activeTab.subscribe((data) => {
      if (data.toString() == 'Commission') {
        this._commissionService.get(this.transactionId).subscribe((data) => {
          if (data['error']) {
            this.commissionErrorMsg = data['error'];
          } else {
            this.commissionData = data['commissionList'];
            this.retailAmount = data['retailAmount'];
            this.commissionAmount = data['commissionAmount'];
            this.commissionHeading = Object.keys(this.commissionData[0]);
          }
        });
      }
    });
  }
}
