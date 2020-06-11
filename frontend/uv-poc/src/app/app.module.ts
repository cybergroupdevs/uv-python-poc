import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { ReactiveFormsModule } from '@angular/forms';
import { MatPaginatorModule } from '@angular/material/paginator';
import { MatTableModule } from '@angular/material/table';
import { MatDialogModule } from '@angular/material/dialog';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import { HomeComponent } from './home/home.component';
import { TransactionDetailComponent } from './transaction-detail/transaction-detail.component';
import { CommissionDetailsComponent } from './commission-details/commission-details.component';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { CustomerHistoryComponent } from './customer-history/customer-history.component';
import { ConsultantDetailsComponent } from './consultant-details/consultant-details.component';
@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    CommissionDetailsComponent,
    ConsultantDetailsComponent,
    TransactionDetailComponent,
    CustomerHistoryComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    ReactiveFormsModule,
    BrowserAnimationsModule,
    HttpClientModule,
    MatPaginatorModule,
    MatTableModule,
    MatDialogModule,
  ],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
