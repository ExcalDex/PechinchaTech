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
import { BenchmarkService } from 'src/app/services/benchmark.service';

@Component({
  selector: 'app-benchmark',
  templateUrl: './benchmark.page.html',
  styleUrls: ['./benchmark.page.scss'],
})
export class BenchmarkPage implements OnInit {

  userAutenticado: User;
  items: Produto[];
  scoreMedio: string;
  classificacao: string;
  resumo: string;
  cpu: string;
  gpu: string;

  constructor(public router: Router, private toastController: ToastController, private navController: NavController, private userService: UserService, private produtoBaseService: ProdutoBaseService, private produtoService: ProdutoService, private notifService: NotifService, private benchmarkService: BenchmarkService) {
    this.userAutenticado = new User();
    this.userAutenticado = this.userService.getUserAutenticado();
    this.items = [];
    this.scoreMedio = "0";
    this.classificacao = "N/A";
    this.resumo = "Aguardando seleção das peças..."
    this.cpu = "";
    this.gpu = "";
  }

  ngOnInit() {
    this.carregarDados();
  }

  async carregarDados() {
    this.items = this.benchmarkService.recuperarProdutosSelecionados();
    if (this.items[1].id != null) {
      let scores: number[] = [];
      for (const produto of this.items) {
        const score = await this.getScoreProdutoBase(produto.id_produto_base);
        scores.push(score);
        if (produto.tipo == "CPU") {
          this.cpu = produto.nome
        }else {
          this.gpu = produto.nome
        }
      }
      let minScore = Math.min(...scores);
      let maxScore = Math.max(...scores);
      let IB = minScore / maxScore;
      this.scoreMedio = (IB * 100).toFixed();
      this.resumo = "Aguardando resposta do Llama 3.2...";
      // if (IB < 0.5) {
      //   this.classificacao = "Ruim - Gargalo Grave! ";
      //   this.resumo = "Sua configuração apresenta um gargalo severo entre a CPU e a GPU. Um dos componentes está muito abaixo do nível do outro, limitando drasticamente o desempenho geral do sistema. Isso significa que, em jogos e aplicações exigentes, o componente mais forte não será aproveitado ao máximo, resultando em quedas bruscas de FPS, uso irregular da GPU/CPU e stuttering. Se sua GPU for muito fraca em relação à CPU, jogos poderão apresentar baixa taxa de quadros mesmo com uso baixo do processador. Se o problema for o contrário (CPU fraca), você poderá notar engasgos e quedas de desempenho, mesmo com a GPU rodando abaixo da capacidade máxima. Para obter um melhor equilíbrio, é recomendável substituir o componente mais fraco por um modelo mais próximo ao desempenho do outro."
      // }
      // if (IB < 0.75 && IB >= 0.5) {
      //   this.classificacao = "Bom - Gargalo Moderado!";
      //   this.resumo = "Sua configuração apresenta um pequeno desequilíbrio entre CPU e GPU. Embora o desempenho geral seja bom para a maioria dos usos, você pode notar que um dos componentes está sendo subutilizado em determinadas situações. Se a CPU for muito superior à GPU, jogos podem rodar com FPS abaixo do esperado, mesmo que o processador esteja ocioso. Se for o contrário (GPU muito forte para a CPU), você pode observar travamentos e quedas ocasionais de desempenho em jogos e aplicações pesadas devido ao processamento limitado. Esse gargalo não impedirá o uso do sistema, mas um pequeno upgrade no componente mais fraco pode garantir um melhor aproveitamento do desempenho total do PC."
      // }
      // if (IB >= 0.75) {
      //   this.classificacao = "Ótimo - Sem Gargalo Perceptível!";
      //   this.resumo = "Parabéns! Sua CPU e GPU estão bem balanceadas, garantindo que ambos os componentes operem de maneira eficiente e sem restrições mútuas. Isso significa que o processador consegue alimentar a GPU com os dados necessários, evitando quedas de desempenho e aproveitando ao máximo o potencial da placa de vídeo. Em jogos e aplicações pesadas, o uso da CPU e GPU será próximo ao ideal, proporcionando FPS estáveis e boa responsividade. Sua configuração está otimizada e não há necessidade de upgrades imediatos. Aproveite seu PC para jogar, trabalhar ou criar sem preocupações!"
      // }
      
      this.resumo = (await this.benchmarkService.getResumo(this.cpu, this.gpu))["response"]
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
