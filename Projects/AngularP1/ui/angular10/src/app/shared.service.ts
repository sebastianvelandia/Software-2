import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http'
import {Observable} from 'rxjs'


@Injectable({
  providedIn: 'root'
})
export class SharedService {
readonly APIUrl = "http://127.0.0.1:8000";
readonly PhotoUrl = "http://127.0.0.1:8000/";
  constructor(private http:HttpClient) { }

  getLibrosList():Observable<any[]>{
    return this.http.get<any[]>(this.APIUrl+'/libro');
  }
  getLibroIsbn(val:any):Observable<any[]>{
    return this.http.get<any[]>(this.APIUrl+'/libro?isbn='+val);
  }

  addResena(val:any){
    return this.http.post(this.APIUrl+'/resena/', val);
  }

  deleteLibro(val:any){
    return this.http.delete(this.APIUrl+'/libro'+val);
  }
}
