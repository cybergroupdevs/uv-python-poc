import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { TransactionDetailComponent } from '../app/transaction-detail/transaction-detail.component';
import { HomeComponent } from './home/home.component';
const routes: Routes = [
  { path: 'transaction', component: TransactionDetailComponent },
  { path: '', component: HomeComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
