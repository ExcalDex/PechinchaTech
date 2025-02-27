import { Component, OnDestroy, OnInit } from '@angular/core';
import { User } from 'src/app/model/user';
import { ProdutoBase } from 'src/app/model/produto-base';
import { Produto } from 'src/app/model/produto';
import { Notif } from 'src/app/model/notif';
import { ProdutoBaseService } from 'src/app/services/produto-base.service'
import { ProdutoService } from 'src/app/services/produto.service';
import { NotifService } from 'src/app/services/notif.service';
import { UserService } from 'src/app/services/user.service';
import { MenuController, ToastController } from '@ionic/angular';
import { NavController } from '@ionic/angular';
import { ActivatedRoute, Router } from '@angular/router';
import { SseService } from 'src/app/services/sse.service';

@Component({
  selector: 'app-main',
  templateUrl: './main.page.html',
  styleUrls: ['./main.page.scss'],
})
export class MainPage implements OnInit {

  userAutenticado: User;
  produtos: Produto[];
  copiaProdutos: Produto[];
  produtosPaginados: Produto[];
  currentPage: number;
  maxPage: number;
  tipoSimulado: string;
  quantNotif: number;
  notifs: Produto[];

  constructor(private menu: MenuController, public router: Router, private activatedRoute: ActivatedRoute, private toastController: ToastController, private navController: NavController, private userService: UserService, private produtoBaseService: ProdutoBaseService, private produtoService: ProdutoService, public notifService: NotifService, private sseService: SseService) {
    this.userAutenticado = new User();
    this.produtos = [];
    this.copiaProdutos = [];
    this.produtosPaginados = [];
    this.currentPage = 1;
    this.maxPage = 1;
    this.tipoSimulado = 'TODOS';
    this.quantNotif = 0;
    this.notifs = [];
  }

  async ngOnInit() {
    this.userAutenticado = this.userService.getUserAutenticado();
    this.sseService.connect("http://localhost:8087/api/sse/subscribe");
    this.notifs = await this.notifService.verificarPromocao()
    if (this.notifs) {
      this.quantNotif = this.notifs.length;
    }
  }

  async ionViewWillEnter() {
    await this.recuperarListaProdutos();
    this.carregarProdutosPaginados();
  }

  async recuperarListaProdutos() {
    this.produtos = await this.produtoService.listarProdutos();
    this.copiaProdutos = this.produtos;
  }
  carregarProdutosPaginados() {
    this.produtosPaginados = this.filtrarListaProdutos(this.copiaProdutos);
    this.maxPage = Math.ceil(this.copiaProdutos.length / 60);
  }

  filtrarListaProdutos(produtos: Produto[]) {
    return produtos.slice((this.currentPage - 1) * 60, this.currentPage * 60);
  }

  pesquisarProduto(event: Event) {
    this.mudarListagem(this.tipoSimulado);
    const input = (event.target as HTMLInputElement).value.toLowerCase();
    this.copiaProdutos = this.copiaProdutos.filter((p: Produto) => {
      return p.nome.toLowerCase().includes(input);
    });
    this.carregarProdutosPaginados();
    this.mudarPagina(1);
  }

  mudarListagem(tipo: string) {
    if (tipo != 'TODOS') {
      this.copiaProdutos = this.produtos.filter((p: Produto) => {
        return p.tipo === tipo;
      });
    } else {
      this.copiaProdutos = this.produtos;
    }
    if (this.tipoSimulado != tipo) {
      const clearButton = document.querySelector('.searchbar-clear-button');
      if (clearButton) {
        (clearButton as HTMLElement).click();
      }
    }
    this.tipoSimulado = tipo;
    this.carregarProdutosPaginados();
    this.mudarPagina(1);
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

  formatarPreco(preco: number) {
    return preco.toFixed(2).replace('.', ',');
  }

  mudarPagina(num: number) {
    this.currentPage = num;
    this.carregarProdutosPaginados();
  }

  async exibirMensagem(texto: string) {
    const toast = await this.toastController.create({
      message: texto,
      duration: 1500
    });
    toast.present();
  }

  openMenu() {
    this.menu.open('fisrt');
  }

  limparNotif(notif: Produto) {
    this.notifService.removerProdutoInteresse(notif)
  }
}
