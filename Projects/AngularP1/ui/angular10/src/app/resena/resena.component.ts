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
  libro_id:any


  ngOnInit(): void {
    this.resenaId =this.res.resenaId;
    this.comentario = this.res.comentario;
    this.libro_id = this.libro_id;
  }
  addResena(){
    var val={resenaId:this.resenaId,
              comentario:this.comentario,
              libro_id:this.libro_id};
              this.service.addResena(val).subscribe(res=>{
                alert(res.toString());
              });
  }
}
