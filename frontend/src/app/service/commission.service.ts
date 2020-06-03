import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class CommissionService {
  baseUri:string = environment.baseUrl

  constructor(private _http: HttpClient) { }

  get(transitionId: string){
    return this._http.get(`http://127.0.0.1:5000/commission/${transitionId}`)
  }
}
