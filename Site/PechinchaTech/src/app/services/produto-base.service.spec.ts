import { TestBed } from '@angular/core/testing';

import { ProdutoBaseService } from './produto-base.service';

describe('ProdutoBaseService', () => {
  let service: ProdutoBaseService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ProdutoBaseService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
