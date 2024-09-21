import { Injectable } from '@angular/core';
<<<<<<< HEAD
=======
import { Produto } from 'src/app/model/produto';
import { firstValueFrom } from 'rxjs';
import { HttpClient, HttpHeaders } from '@angular/common/http';
>>>>>>> 9ac4af2cce610e5be57a3e4583a90fbcb5e61161

@Injectable({
  providedIn: 'root'
})
export class ProdutoService {

<<<<<<< HEAD
  constructor() { }
=======
  httpHeaders = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json'})
  }

  url: string = "http://localhost:8087/api/produto"
  constructor(private httpClient: HttpClient) { }

  async listarProdutos(): Promise<Produto[]> {
    return await firstValueFrom(this.httpClient.get<Produto[]>(this.url));
  }

  async consultarProduto(id: number): Promise<Produto> {
    let urlAuxiliar = this.url + "/" + id;
    return await firstValueFrom(this.httpClient.get<Produto>(urlAuxiliar));
  }
>>>>>>> 9ac4af2cce610e5be57a3e4583a90fbcb5e61161
}
