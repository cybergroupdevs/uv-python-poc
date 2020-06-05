import { Injectable } from "@angular/core";
import { HttpClient, HttpParams } from "@angular/common/http";
import { environment } from "../../environments/environment";

@Injectable({
  providedIn: "root",
})
export class ConsultantService {
  constructor(private http: HttpClient) {}
  baseUri: string = environment.baseUrl;
  get(consultantId) {
    let params = new HttpParams();
    params = params.append("transactionId", consultantId);
    return this.http.get(this.baseUri + "/consultant", {
      params: params,
    });
  }
}
