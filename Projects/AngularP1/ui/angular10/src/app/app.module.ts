import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { AutorComponent } from './autor/autor.component';
import { ShowAutorComponent } from './autor/show-autor/show-autor.component';
import { LibroComponent } from './libro/libro.component';
import { ShowLibroComponent } from './libro/show-libro/show-libro.component';
import { SharedService } from './shared.service';

import {HttpClientModule} from '@angular/common/http';
import {FormsModule, ReactiveFormsModule} from '@angular/forms';
import { ResenaLibroComponent } from './libro/resena-libro/resena-libro.component';
import { ResenaComponent } from './resena/resena.component';
import { CalificaionComponent } from './calificaion/calificaion.component';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap'

@NgModule({
  declarations: [
    AppComponent,
    AutorComponent,
    ShowAutorComponent,
    LibroComponent,
    ShowLibroComponent,
    ResenaLibroComponent,
    ResenaComponent,
    CalificaionComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule,
    NgbModule
  ],
  providers: [SharedService],
  bootstrap: [AppComponent]
})
export class AppModule { }
