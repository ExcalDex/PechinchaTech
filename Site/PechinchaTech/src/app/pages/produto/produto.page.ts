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

@Component({
  selector: 'app-produto',
  templateUrl: './produto.page.html',
  styleUrls: ['./produto.page.scss'],
})
export class ProdutoPage implements OnInit {

  userAutenticado: User;
  produto: Produto;
  scoreProdutoBase: number;

  constructor(public router: Router, private activatedRoute: ActivatedRoute, private toastController: ToastController, private navController: NavController, private userService: UserService, private produtoBaseService: ProdutoBaseService, private produtoService: ProdutoService, private notifService: NotifService) { 
    this.userAutenticado = new User();
    this.produto = new Produto();
    this.scoreProdutoBase = 0;
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
  }

  formatarPreco(preco: number) {
    return preco.toFixed(2).replace('.', ',');
  }

  produtoSelecionado() {
    
  }

  selecionarProduto() {
    if (1 == 1) {
      
    }
  }
}
