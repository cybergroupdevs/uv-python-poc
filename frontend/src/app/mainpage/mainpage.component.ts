import { Component, OnInit } from '@angular/core';
import {FormControl} from '@angular/forms'
@Component({
  selector: 'app-mainpage',
  templateUrl: './mainpage.component.html',
  styleUrls: ['./mainpage.component.css']
})
export class MainpageComponent implements OnInit {
  transactionId = new FormControl('');
  constructor() { }

  ngOnInit(): void {
  }

}
