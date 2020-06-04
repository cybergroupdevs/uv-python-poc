import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { CustomerHistoryComponent } from '../app/customer-history/customer-history.component'
import { TransactionDetailComponent } from '../app/transaction-detail/transaction-detail.component'
import { HomeComponent } from './home/home.component'
const routes: Routes = [
  {path: 'customer/history' , component: CustomerHistoryComponent},
  {path: '',component:HomeComponent},
  {path: 'transaction',component:TransactionDetailComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
