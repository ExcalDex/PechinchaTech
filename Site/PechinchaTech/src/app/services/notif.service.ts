import { Injectable } from '@angular/core';
import { Produto } from '../model/produto';
import { ProdutoBaseService } from './produto-base.service';
import { ProdutoService } from './produto.service';

@Injectable({
  providedIn: 'root'
})
export class NotifService {

  constructor(private produtoService: ProdutoService, private produtoBaseService: ProdutoBaseService) { }

  registrarProdutoInteresse(p: Produto) {
    let iProdutos: Produto[] = [];
    iProdutos = JSON.parse(localStorage.getItem('produtosInteresse') || '[]');
    iProdutos.push(p);
    localStorage.setItem('produtosInteresse', JSON.stringify(iProdutos));
  }

  removerProdutoInteresse(p: Produto) {
    let iProdutos: Produto[] = [];
    iProdutos = JSON.parse(localStorage.getItem('produtosInteresse') || '[]');
    iProdutos = iProdutos.filter(produto => produto.id != p.id);
    localStorage.setItem('produtosInteresse', JSON.stringify(iProdutos));
  }

  recuperarProdutosInteresse() {
    let iProdutos: Produto[] = [];
    iProdutos = JSON.parse(localStorage.getItem('produtosInteresse') || '[]');
    return iProdutos;
  }

  async verificarPromocao(): Promise<Produto[]> {
    let produtos: Produto[] = [];
    let iProdutos: Produto[] = [];
    let promoP: Produto[] = [];
    iProdutos = JSON.parse(localStorage.getItem('produtosInteresse') || '[]');
    produtos = await this.produtoService.listarProdutos();
    for (let pI of iProdutos) {
      for (let p of produtos) {
        if (p.id_produto_base == pI.id_produto_base) {
          if (pI.preco > p.preco) {
            promoP.push(p);
          }
        }
      }
    }
    return promoP;
  }
}
