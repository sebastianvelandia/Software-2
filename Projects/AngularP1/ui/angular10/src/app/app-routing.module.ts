import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import {AutorComponent} from './autor/autor.component';
import {LibroComponent} from './libro/libro.component'

const routes: Routes = [
{path:'autor', component:AutorComponent},
{path:'libro',component:LibroComponent}

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
