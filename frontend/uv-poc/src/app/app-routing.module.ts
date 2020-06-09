import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { TransactionDetailComponent } from '../app/transaction-detail/transaction-detail.component';

const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'transaction', component: TransactionDetailComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
