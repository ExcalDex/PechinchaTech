import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { BenchmarkPageRoutingModule } from './benchmark-routing.module';

import { BenchmarkPage } from './benchmark.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    BenchmarkPageRoutingModule
  ],
  declarations: [BenchmarkPage]
})
export class BenchmarkPageModule {}
