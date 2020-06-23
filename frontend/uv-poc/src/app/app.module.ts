import { AppComponent } from './app.component';
import { AppRoutingModule } from './app-routing.module';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { BrowserModule } from '@angular/platform-browser';
import { CommissionDetailsComponent } from './commission-details/commission-details.component';
import { ConsultantDetailsComponent } from './consultant-details/consultant-details.component';
import { CustomerDetailsComponent } from './customer-details/customer-details.component';
import { CustomerHistoryComponent } from './customer-history/customer-history.component';
import { HomeComponent } from './home/home.component';
import { HttpClientModule } from '@angular/common/http';
import { NgModule } from '@angular/core';
import { OrderComponent } from './order/order.component';
import { MatDialogModule } from '@angular/material/dialog';
import { MatIconModule } from '@angular/material/icon';
import { MatPaginatorModule } from '@angular/material/paginator';
import { MatTableModule } from '@angular/material/table';
import { MatTabsModule } from '@angular/material/tabs';
import { ReactiveFormsModule } from '@angular/forms';
import { TransactionComponent } from './transaction/transaction.component';
import { TransactionDetailComponent } from './transaction-detail/transaction-detail.component';
@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    CommissionDetailsComponent,
    ConsultantDetailsComponent,
    CustomerDetailsComponent,
    CustomerHistoryComponent,
    OrderComponent,
    TransactionComponent,
    TransactionDetailComponent,
  ],
  imports: [
    AppRoutingModule,
    ReactiveFormsModule,
    BrowserAnimationsModule,
    BrowserModule,
    HttpClientModule,
    MatDialogModule,
    MatIconModule,
    MatPaginatorModule,
    MatTableModule,
    MatTabsModule,
    ReactiveFormsModule,
  ],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
