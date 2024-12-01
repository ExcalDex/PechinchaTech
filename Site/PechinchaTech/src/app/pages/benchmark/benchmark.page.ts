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
  selector: 'app-benchmark',
  templateUrl: './benchmark.page.html',
  styleUrls: ['./benchmark.page.scss'],
})
export class BenchmarkPage implements OnInit {

  userAutenticado: User;
  items: Produto[];
  scoreMedio: number;
  classificacao: string;
  resumo: string;

  constructor(public router: Router, private toastController: ToastController, private navController: NavController, private userService: UserService, private produtoBaseService: ProdutoBaseService, private produtoService: ProdutoService, private notifService: NotifService) { 
    this.userAutenticado = new User();
    this.userAutenticado = this.userService.getUserAutenticado();
    this.items = [];
    this.scoreMedio = 0;
    this.classificacao = "N/A";
    this.resumo = "Aguardando seleção de peças..."
  }

  async ngOnInit() {
    this.items = JSON.parse(localStorage.getItem('items') || '[]');
    if (this.items[0].id != null) {
      let sum = 0;
      for (let i = 0; i < this.items.length; i++) {
        sum += await this.getScoreProdutoBase(this.items[i].id_produto_base);
      }
      this.scoreMedio = sum / this.items.length;
      if (this.scoreMedio < 100) {
        this.classificacao = "Ruim!";
      }
      if (this.scoreMedio >= 100 && this.scoreMedio < 150) {
        this.classificacao = "Bom!";
      }
      if (this.scoreMedio >= 150) {
        this.classificacao = "Muito bom!";
      }

      // let scoreResumo = 0;
      // if (scoreResumo < x) {
      //   this.resumo = "Texto de Resumo"
      // }
    }
  }

  async getScoreProdutoBase(idProdutoBase: number): Promise<number> {
    let auxProdutoBase = await this.produtoBaseService.consultarProdutoBase(idProdutoBase);
    return auxProdutoBase.score_userbenchmark
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

}
