import { AppComponent } from './app.component';
import { AppRoutingModule } from './app-routing.module';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { BrowserModule } from '@angular/platform-browser';
import { CommissionDetailsComponent } from './commission-details/commission-details.component';
import { ConsultantDetailsComponent } from './consultant-details/consultant-details.component';
import { CustomerDetailsComponent } from './customer-details/customer-details.component';
import { CustomerHistoryComponent } from './customer-history/customer-history.component';
import { HttpClientModule } from '@angular/common/http';
import { MatDialogModule } from '@angular/material/dialog';
import { MatPaginatorModule } from '@angular/material/paginator';
import { MatTableModule } from '@angular/material/table';
import { NgModule } from '@angular/core';

@NgModule({
  declarations: [
    AppComponent,
    CommissionDetailsComponent,
    ConsultantDetailsComponent,
    CustomerDetailsComponent,
    CustomerHistoryComponent,
  ],
  imports: [
    AppRoutingModule,
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
