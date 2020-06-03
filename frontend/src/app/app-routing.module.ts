import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {CutomerHistoryComponent} from '../app/cutomer-history/cutomer-history.component'
import {TransactionDetailComponent} from '../app/transaction-detail/transaction-detail.component'
import {MainpageComponent} from '../app/mainpage/mainpage.component'
const routes: Routes = [
  {path: 'customer/history' , component: CutomerHistoryComponent},
  {path: '',component:MainpageComponent},
  {path: 'transaction',component:TransactionDetailComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
