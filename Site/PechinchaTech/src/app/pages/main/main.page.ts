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
import { Router } from '@angular/router';

@Component({
  selector: 'app-main',
  templateUrl: './main.page.html',
  styleUrls: ['./main.page.scss'],
})
export class MainPage implements OnInit {

  userAutenticado: User;
  constructor(public router: Router, private toastController: ToastController, private navController: NavController, private userService: UserService, private produtoBaseService: ProdutoBaseService, private produtoService: ProdutoService, private notifService: NotifService) { 
    this.userAutenticado = new User();
    this.userAutenticado = this.userService.getUserAutenticado();
  }

  ngOnInit() {
    this.carregarListaProdutos();
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

  async carregarListaProdutos() {

  }
}
