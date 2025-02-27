import { Component, OnInit } from '@angular/core';
import { User } from 'src/app/model/user';
import { ProdutoBase } from 'src/app/model/produto-base';
import { Produto } from 'src/app/model/produto';
import { Notif } from 'src/app/model/notif';
import { ProdutoBaseService } from 'src/app/services/produto-base.service'
import { ProdutoService } from 'src/app/services/produto.service';
import { NotifService } from 'src/app/services/notif.service';
import { UserService } from 'src/app/services/user.service';
import { ToastController } from '@ionic/angular';
import { NavController } from '@ionic/angular';
import { ActivatedRoute, Router } from '@angular/router';
import { BenchmarkService } from 'src/app/services/benchmark.service';

@Component({
  selector: 'app-produto',
  templateUrl: './produto.page.html',
  styleUrls: ['./produto.page.scss'],
})
export class ProdutoPage implements OnInit {

  userAutenticado: User;
  produto: Produto;
  scoreProdutoBase: number;
  sProdutos: Produto[];
  iProdutos: Produto[];
  selected: boolean;
  iSelected: boolean;

  constructor(public router: Router, private activatedRoute: ActivatedRoute, private toastController: ToastController, private navController: NavController, private userService: UserService, private produtoBaseService: ProdutoBaseService, private produtoService: ProdutoService, private notifService: NotifService, private benchmarkService: BenchmarkService) { 
    this.userAutenticado = new User();
    this.produto = new Produto();
    this.scoreProdutoBase = 0;
    this.sProdutos = [];
    this.iProdutos = [];
    this.selected = false;
    this.iSelected = false;
  }

  ngOnInit() {
    this.userAutenticado = this.userService.getUserAutenticado();
    let id = parseFloat(this.activatedRoute.snapshot.params['id']);
    if(!isNaN(id)) {
      this.consultaProduto(id);
    }
  }

  verificaUserAutenticado(): boolean {
    if (this.userAutenticado.id != null) {
      return true;
    }
    return false;
  }

  encerrarSessao() {
    this.userService.encerrarSessao();
    this.navController.navigateForward('/login');
  }

  async consultaProduto(id: number) {
    this.produto = await this.produtoService.consultarProduto(id);
    this.scoreProdutoBase = (await this.produtoBaseService.consultarProdutoBase(this.produto.id_produto_base)).score_userbenchmark;
    this.selected = this.produtoSelecionado();
    this.iSelected = this.produtoInteresse();
  }

  formatarPreco(preco: number) {
    return preco.toFixed(2).replace('.', ',');
  }

  produtoSelecionado(): boolean {
    this.sProdutos = this.benchmarkService.recuperarProdutosSelecionados();
    if (!!this.sProdutos.find(p => p.id == this.produto.id)) {
      return true;
    }
    return false;
  }

  produtoInteresse(): boolean {
    this.iProdutos = this.notifService.recuperarProdutosInteresse();
    if (!!this.iProdutos.find(p => p.id == this.produto.id)) {
      return true;
    }
    return false;
  }

  selecionarProduto() {
    if (!this.produtoSelecionado()) {
      this.benchmarkService.registrarProdutoSelecionado(this.produto);
      this.selected = true;
    }else {
      this.benchmarkService.removerProdutoSelecionado(this.produto);
      this.selected = false;
    }
  }

  selecionarProdutoInteresse() {
    if (!this.produtoInteresse()) {
      this.notifService.registrarProdutoInteresse(this.produto);
      this.iSelected = true;
    }else {
      this.notifService.removerProdutoInteresse(this.produto);
      this.iSelected = false;
    }
  }
}
