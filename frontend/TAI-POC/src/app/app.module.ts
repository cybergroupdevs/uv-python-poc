import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import {MatTableModule} from '@angular/material/table';
import {MatDialogModule} from '@angular/material/dialog';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { TransactionDetailComponent,customerDialog,consultantDialog} from './transaction-detail/transaction-detail.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MainpageComponent } from './mainpage/mainpage.component';
import { CutomerHistoryComponent } from './cutomer-history/cutomer-history.component';

@NgModule({
  declarations: [
    AppComponent,
    TransactionDetailComponent,
    MainpageComponent,
    customerDialog,
    consultantDialog,
    CutomerHistoryComponent
    
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MatTableModule,
    MatDialogModule

  ],
  providers: [],
  bootstrap: [AppComponent],
  entryComponents:[customerDialog,consultantDialog],
})
export class AppModule { }
