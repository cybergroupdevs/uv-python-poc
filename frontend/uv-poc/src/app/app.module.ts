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

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
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
    ReactiveFormsModule,
  ],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
