import { Component, OnInit } from '@angular/core';
import {SharedService} from 'src/app/shared.service';

@Component({
  selector: 'app-show-libro',
  templateUrl: './show-libro.component.html',
  styleUrls: ['./show-libro.component.css']
})
export class ShowLibroComponent implements OnInit {

  constructor(private service:SharedService) { }

  LibroList:any=[];

  ModalTitle:string;
  ActivateResenaComp:boolean=false;
  res:any;

  ngOnInit(): void {
    this.refreshLibroList();
  }

  addClick(item){
    console.log(item)
    this.res={
    
      resenaId: 0,
      comentario: "",
      libro: item
    }
    this.ModalTitle = "Añadir Reseña";
    this.ActivateResenaComp=true;
  }

  closeClick(){
    this.ActivateResenaComp=false
  }

  refreshLibroList(){
    this.service.getLibrosList().subscribe(data=>{
      this.LibroList = data;
    })
  }

}
