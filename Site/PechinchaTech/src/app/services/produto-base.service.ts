import { HttpHeaders, HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { firstValueFrom } from 'rxjs';
import { ProdutoBase } from '../model/produto-base';

@Injectable({
  providedIn: 'root'
})
export class ProdutoBaseService {
  httpHeaders = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })
  }

  url: string = "http://localhost:8087/api/produto-base"
  constructor(private httpClient: HttpClient) { }

  async consultarProdutoBase(idProdutoBase: number): Promise<ProdutoBase> {
    let urlAuxiliar = this.url + "/" + idProdutoBase;
    return await firstValueFrom(this.httpClient.get<ProdutoBase>(urlAuxiliar));
  }
}
