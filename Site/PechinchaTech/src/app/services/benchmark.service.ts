import { Injectable } from '@angular/core';
import { Produto } from '../model/produto';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { firstValueFrom } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class BenchmarkService {

  ordemTipo: string[] = ['CPU', 'GPU'];
  httpHeaders = {
    headers: new HttpHeaders({'Content-Type': 'application/json'})
  }

  url: string = "http://localhost:11434/api/generate"

  constructor(private httpClient: HttpClient) {}

  async getResumo(cpu: string, gpu: string) {
    const body = {
      "model": "llama3.2",
      "prompt": "Explique com detalhes se há e, caso sim, qual serão os problemas enfrentados para alguém com uma máquina com a CPU: " + cpu + " e a GPU: " + gpu + ", no quesito desempenho nas atividades diárias e jogos, ou seja, quero que diga se é uma boa combinação. Vale ressaltar que gostaria da resposta em um único bloco de texto apenas e sem as '*' características de suas respostas.",
      "stream": false
    }
    
    return await firstValueFrom(this.httpClient.post<any>(this.url, body));
  }
  registrarProdutoSelecionado(p: Produto) {
    let sProdutos: Produto[] = [];
    sProdutos = JSON.parse(localStorage.getItem('produtosSelecionados') || '[]');
    sProdutos = sProdutos.filter(produto => produto.tipo != p.tipo);
    sProdutos.push(p);
    sProdutos.sort((a, b) => {
      return this.ordemTipo.indexOf(a.tipo) - this.ordemTipo.indexOf(b.tipo);
    });
    localStorage.setItem('produtosSelecionados', JSON.stringify(sProdutos));
  }

  removerProdutoSelecionado(p: Produto) {
    let sProdutos: Produto[] = [];
    sProdutos = JSON.parse(localStorage.getItem('produtosSelecionados') || '[]');
    sProdutos = sProdutos.filter(produto => produto.id != p.id);
    localStorage.setItem('produtosSelecionados', JSON.stringify(sProdutos));
  }

  recuperarProdutosSelecionados(): Produto[] {
    let sProdutos: Produto[] = [];
    sProdutos = JSON.parse(localStorage.getItem('produtosSelecionados') || '[]');
    return sProdutos;
  }
}
