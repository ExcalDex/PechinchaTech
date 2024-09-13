import { ComponentFixture, TestBed } from '@angular/core/testing';
import { BenchmarkPage } from './benchmark.page';

describe('BenchmarkPage', () => {
  let component: BenchmarkPage;
  let fixture: ComponentFixture<BenchmarkPage>;

  beforeEach(() => {
    fixture = TestBed.createComponent(BenchmarkPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
