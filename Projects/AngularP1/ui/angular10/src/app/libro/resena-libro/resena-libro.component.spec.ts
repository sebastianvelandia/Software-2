import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ResenaLibroComponent } from './resena-libro.component';

describe('ResenaLibroComponent', () => {
  let component: ResenaLibroComponent;
  let fixture: ComponentFixture<ResenaLibroComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ResenaLibroComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ResenaLibroComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
