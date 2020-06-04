import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { MatTableModule } from '@angular/material/table';
import { MatDialogModule } from '@angular/material/dialog';
import { HttpClientModule } from '@angular/common/http';
import { MatTabsModule } from '@angular/material/tabs';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { TransactionDetailComponent} from './transaction-detail/transaction-detail.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { HomeComponent } from './home/home.component';
import { CommissionComponent } from './commission/commission.component';
import { CustomerComponent } from './customer/customer.component';
import { ConsultantComponent } from './consultant/consultant.component';
import { CustomerHistoryComponent } from './customer-history/customer-history.component';
import { CreditCardComponent } from './credit-card/credit-card.component';
import { TransactionComponent } from './transaction/transaction.component';
import { OrderComponent } from './order/order.component';

@NgModule({
  declarations: [
    AppComponent,
    TransactionDetailComponent,
    HomeComponent,
    CommissionComponent,
    CustomerComponent,
    ConsultantComponent,
    CustomerHistoryComponent,
    CreditCardComponent,
    TransactionComponent,
    OrderComponent,
    
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MatTableModule,
    MatDialogModule,
    HttpClientModule,
    MatTabsModule,
    FormsModule,
    ReactiveFormsModule
  ],
  providers: [],
  bootstrap: [AppComponent],
  entryComponents:[],
})
export class AppModule { }
