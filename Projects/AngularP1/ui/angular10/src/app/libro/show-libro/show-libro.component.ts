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

  ngOnInit(): void {
    this.refreshLibroList();
  }

  refreshLibroList(){
    this.service.getLibrosList().subscribe(data=>{
      this.LibroList = data;
    })
  }

}
