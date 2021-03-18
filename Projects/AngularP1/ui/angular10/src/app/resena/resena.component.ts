import { Component, Input, OnInit } from '@angular/core';
import {SharedService} from 'src/app/shared.service';

@Component({
  selector: 'app-resena',
  templateUrl: './resena.component.html',
  styleUrls: ['./resena.component.css']
})
export class ResenaComponent implements OnInit {

  constructor(private service:SharedService) { }

  @Input() res:any
  resenaId:string
  comentario:string
  libro:any


  ngOnInit(): void {
    this.resenaId =this.res.resenaId;
    this.comentario = this.res.comentario;
    this.libro = this.libro;
  }
  addResena(libro){

    console.log(libro)
    var val={libro:libro,
              comentario:this.comentario
              };
              this.service.addResena(val).subscribe(res=>{
                alert(res.toString());
              });
  }
}
