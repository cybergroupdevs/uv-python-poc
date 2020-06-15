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
import { MatDialogModule } from '@angular/material/dialog';
import { MatPaginatorModule } from '@angular/material/paginator';
import { MatTableModule } from '@angular/material/table';
import { NgModule } from '@angular/core';
import { ReactiveFormsModule } from '@angular/forms';
import { TransactionComponent } from './transaction/transaction.component';
import { TransactionDetailComponent } from './transaction-detail/transaction-detail.component';

@NgModule({
  declarations: [
    AppComponent,
    TransactionDetailComponent,
    CommissionDetailsComponent,
    ConsultantDetailsComponent,
    CustomerDetailsComponent,
    CustomerHistoryComponent,
    HomeComponent,
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
    MatPaginatorModule,
    MatTableModule,
  ],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
