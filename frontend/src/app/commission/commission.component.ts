import { Component, OnInit } from '@angular/core';
import { CommissionService } from '../service/commission.service'

@Component({
  selector: 'commission',
  templateUrl: './commission.component.html',
  styleUrls: ['./commission.component.css']
})
export class CommissionComponent implements OnInit {

  constructor(private _commissionService: CommissionService) { }
  commissionData;
  commissionAmount: number;
  retailAmount: number;
  commissionHeading = []
  errorMsg : string = null
  

  ngOnInit() {
    this._commissionService.activeTab.subscribe((data) =>{
      if(data.toString() == 'Commission'){
        this._commissionService.get('4830*35*1672').subscribe((data) =>{
          if(data['error']){
            console.log('error')
            this.errorMsg = data['error']
          }
          else{
            this.commissionData = data['commissionList']
            this.retailAmount = data['retailAmount']
            this.commissionAmount = data['commissionAmount']
            this.commissionHeading = Object.keys(this.commissionData[0])
          }
        })
      }
    })
  }
}
