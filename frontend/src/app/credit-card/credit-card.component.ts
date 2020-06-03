import { Component, OnInit } from '@angular/core';
import { CommissionService } from '../service/commission.service';

@Component({
  selector: 'credit-card',
  templateUrl: './credit-card.component.html',
  styleUrls: ['./credit-card.component.css']
})
export class CreditCardComponent implements OnInit {

  constructor(private _commissionService: CommissionService) { }
  cardDetails : any
  creditCardHeading = []

  ngOnInit() {
    this._commissionService.creditCardDetails('4830*35*1672').subscribe((res) => {
      this.cardDetails = res['cardDetails']
      this.creditCardHeading = Object.keys(res['cardDetails'][0])
    })
  }

}
