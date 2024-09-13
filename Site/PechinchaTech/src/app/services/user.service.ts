import { Injectable } from '@angular/core';
import { User } from 'src/app/model/user';
import { firstValueFrom } from 'rxjs';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})

export class UserService {

  httpHeaders = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })
  }

  url: string = 'http://localhost:8087/api/usuario'

  constructor(private httpClient: HttpClient) { }

  async listarUser(): Promise<User[]> {
    return await firstValueFrom(this.httpClient.get<User[]>(this.url));
  }

  async consultarUser(id: number): Promise<User> {
    let urlAuxiliar = this.url + "/" + id;
    return await firstValueFrom(this.httpClient.get<User>(urlAuxiliar));
  }

  async cadastrarUser(user: User): Promise<User> {
    return await firstValueFrom(this.httpClient.post<User>(this.url, user));
  }

  async autenticar(emailOrUsername: string, senha: string): Promise<User> {
   let urlAuxiliar = this.url + "/" + emailOrUsername + "/" + senha + "/autenticar";
   return await firstValueFrom(this.httpClient.get<User>(urlAuxiliar));
  }

  async editarUser(user: User): Promise<User> {
    return await firstValueFrom(this.httpClient.put<User>(this.url, user));
  }

  async excluirUser(id: number): Promise<User> {
    let urlAuxiliar = this.url + "/" + id;
    return await firstValueFrom(this.httpClient.delete<User>(urlAuxiliar));
  }

  registraUserAutenticado(user: User) {
    localStorage.setItem('userAutenticado', JSON.stringify(user));
  }

  recuperarAutenticacao(): User {
    let user = new User();
    user = JSON.parse(localStorage.getItem('userAutenticado') || "{}");
    return user;
  }

  encerrarSessao() {
    localStorage.removeItem('userAutenticado');
  }

}
