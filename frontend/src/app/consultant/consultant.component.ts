import { Component, OnInit } from '@angular/core';
import{ConsultantService} from '../service/consultant.service'

@Component({
  selector: 'app-consultant',
  templateUrl: './consultant.component.html',
  styleUrls: ['./consultant.component.css']
})
export class ConsultantComponent implements OnInit {
  transactionId:any
  operator:any
  type:any
  constructor(
    private consultantService:ConsultantService
    ) {}
    ngOnInit() { }
}
