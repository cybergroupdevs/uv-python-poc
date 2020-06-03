import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../environments/environment';
import { BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class CommissionService {
  baseUri:string = environment.baseUrl

  activeTab: BehaviorSubject<string[]> = new BehaviorSubject<string[]>([]);

  constructor(private _http: HttpClient) { }

  get(transitionId: string){
    return this._http.get(`${this.baseUri}/commission/${transitionId}`)
  }

  changeActiveTab(value){
    this.activeTab.next(value);
  }

  creditCardDetails(transactionId: string){
    return this._http.get(`${this.baseUri}/transaction/${transactionId}/creditCard/authentication`)
  }
}
