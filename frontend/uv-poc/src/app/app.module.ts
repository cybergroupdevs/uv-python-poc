import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from "@angular/common/http";
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { TransactionDetailComponent } from './transaction-detail/transaction-detail.component';
import { ConsultantDetailsComponent } from "./consultant-details/consultant-details.component";

@NgModule({
  declarations: [
    AppComponent,
    TransactionDetailComponent,
    ConsultantDetailsComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule { }
