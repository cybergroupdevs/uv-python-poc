import { TestBed } from '@angular/core/testing';

import { CommissionService } from './commission.service';

describe('CommissionService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: CommissionService = TestBed.get(CommissionService);
    expect(service).toBeTruthy();
  });
});
