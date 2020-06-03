import { TestBed } from '@angular/core/testing';

import { TransactionDetailService } from './transaction-detail.service';

describe('TransactionDetailService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: TransactionDetailService = TestBed.get(TransactionDetailService);
    expect(service).toBeTruthy();
  });
});
