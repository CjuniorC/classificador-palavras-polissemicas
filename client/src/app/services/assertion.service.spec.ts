import { TestBed } from '@angular/core/testing';

import { AssertionService } from './assertion.service';

describe('AssertionService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: AssertionService = TestBed.get(AssertionService);
    expect(service).toBeTruthy();
  });
});
