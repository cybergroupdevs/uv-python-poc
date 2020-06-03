import { Injectable } from '@angular/core';
import { HttpClient,HttpParams } from '@angular/common/http' 
import {environment} from '../../environments/environment'

@Injectable({
  providedIn: 'root'
})
export class CustomerService {

  constructor(private http:HttpClient) { }
  baseUri:string=environment.baseUrl;
  get(customerId){
    let params= new HttpParams();
    params=params.append("customerId",customerId)
    return this.http.get(this.baseUri+'api/customer',{
      params:params
    });
  }
}
