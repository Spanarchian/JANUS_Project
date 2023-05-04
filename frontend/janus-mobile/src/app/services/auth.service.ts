import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { API_URL } from './constants';
import { switchMap } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  constructor(private http: HttpClient) { }

  register(email : string, password : string ) {
    return this.http.post(`${API_URL}/users`, {email, password}).pipe(
      switchMap((_) => {
        return this.login(email, password);
      })
    );
  }


  login(email : string, password : string ){
    return this.http.post(`${API_URL}/auth`, {email, password});
  }

}
