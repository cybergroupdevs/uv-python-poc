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
  keys:any
  data:any
  constructor(
    private consultantService:ConsultantService
    ) {}
    ngOnInit() {
      this.transactionId="5334*24*1373"
          this.consultantService.get(this.transactionId).subscribe((res:any)=>{
            this.data=res[0]
            this.keys = Object.keys(res[0])
          })
      
    }



}
