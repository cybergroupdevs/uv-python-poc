import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import {MatTableModule} from '@angular/material/table';
import {MatDialogModule} from '@angular/material/dialog';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule, } from '@angular/common/http'
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { TransactionDetailComponent,customerDialog,consultantDialog} from './transaction-detail/transaction-detail.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MainpageComponent } from './mainpage/mainpage.component';
import { CutomerHistoryComponent } from './cutomer-history/cutomer-history.component';
import {Observable} from 'rxjs';
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
    HttpClientModule,
    MatDialogModule,
    FormsModule,
    ReactiveFormsModule

  ],
  providers: [],
  bootstrap: [AppComponent],
  entryComponents:[customerDialog,consultantDialog],
})
export class AppModule { }
