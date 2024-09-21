import { Injectable } from '@angular/core';
import { Produto } from 'src/app/model/produto';
import { firstValueFrom } from 'rxjs';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ProdutoService {

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
}
