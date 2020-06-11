import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { TransactionComponent } from './transaction/transaction.component';
import { TransactionDetailComponent } from './transaction-detail/transaction-detail.component';
import { HomeComponent } from './home/home.component';
import { ReactiveFormsModule } from '@angular/forms';
import { ConsultantDetailsComponent } from './consultant-details/consultant-details.component';
import { MatPaginatorModule } from '@angular/material/paginator';
import { MatTableModule } from '@angular/material/table';
import { MatDialogModule } from '@angular/material/dialog';
import { CommissionDetailsComponent } from './commission-details/commission-details.component';
import { CustomerHistoryComponent } from './customer-history/customer-history.component';
@NgModule({
  declarations: [
    AppComponent,
    TransactionComponent,
    TransactionDetailComponent,
    CommissionDetailsComponent,
    ConsultantDetailsComponent,
    HomeComponent,
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
