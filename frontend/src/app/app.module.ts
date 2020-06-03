import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import {MatTableModule} from '@angular/material/table';
import {MatDialogModule} from '@angular/material/dialog';
import { HttpClientModule } from '@angular/common/http';
import {MatTabsModule} from '@angular/material/tabs';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { TransactionDetailComponent} from './transaction-detail/transaction-detail.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MainpageComponent } from './mainpage/mainpage.component';
import { CommissionComponent } from './commission/commission.component';
import { CustomerComponent } from './customer/customer.component';
import { ConsultantComponent } from './consultant/consultant.component';
import { CustomerHistoryComponent } from './customer-history/customer-history.component';

@NgModule({
  declarations: [
    AppComponent,
    TransactionDetailComponent,
    MainpageComponent,
    CommissionComponent,
    CustomerComponent,
    ConsultantComponent,
    CustomerHistoryComponent,
    
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MatTableModule,
    MatDialogModule,
    HttpClientModule,
    MatTabsModule 
  ],
  providers: [],
  bootstrap: [AppComponent],
  entryComponents:[],
})
export class AppModule { }
