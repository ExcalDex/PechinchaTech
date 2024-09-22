import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { BenchmarkPage } from './benchmark.page';

const routes: Routes = [
  {
    path: '',
    component: BenchmarkPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class BenchmarkPageRoutingModule {}
