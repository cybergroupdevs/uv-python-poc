import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CutomerHistoryComponent } from './cutomer-history.component';

describe('CutomerHistoryComponent', () => {
  let component: CutomerHistoryComponent;
  let fixture: ComponentFixture<CutomerHistoryComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CutomerHistoryComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CutomerHistoryComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
