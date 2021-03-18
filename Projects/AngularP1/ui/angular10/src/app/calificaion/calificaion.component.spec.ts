import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CalificaionComponent } from './calificaion.component';

describe('CalificaionComponent', () => {
  let component: CalificaionComponent;
  let fixture: ComponentFixture<CalificaionComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CalificaionComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(CalificaionComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
