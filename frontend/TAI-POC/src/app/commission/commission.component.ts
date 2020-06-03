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
  commissionHeading = []
  

  ngOnInit() {
    this._commissionService.get('2996*25*7652').subscribe((data) =>{
      this.commissionData = data['commissionList']
      this.commissionHeading = Object.keys(this.commissionData[0])
      
    })
  }

}
