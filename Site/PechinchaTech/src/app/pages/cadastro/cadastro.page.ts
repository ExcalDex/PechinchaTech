import { Component, OnInit } from '@angular/core';

import { User } from 'src/app/model/user';
import { UserService } from 'src/app/services/user.service';
import { ToastController } from '@ionic/angular';
import { NavController } from '@ionic/angular';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-cadastro',
  templateUrl: './cadastro.page.html',
  styleUrls: ['./cadastro.page.scss'],
})
export class CadastroPage implements OnInit {

  user: User;
  formGroup: FormGroup;

  senhaType: string = "password";
  iconName: string = "eye-off";

  constructor(private toastController: ToastController, private navController: NavController, private formBuilder: FormBuilder, private userService: UserService) {
    this.user = new User();
    this.formGroup = this.formBuilder.group({
      username: ['', Validators.compose([Validators.required])],
      email: ['', Validators.compose([Validators.required, Validators.email])],
      senha: ['', Validators.compose([Validators.required, Validators.minLength(8)])],
      confirmSenha: ['', Validators.compose([Validators.required])]
    })
  }

  ngOnInit() {
  }

  senhasBatem() {
    const senha = this.formGroup.get('senha')?.value;
    const confirmSenha = this.formGroup.get('confirmSenha')?.value;
    if (senha === confirmSenha) {
      return true;
    } else {
      return false;
    }
  }
  toggleVisibilidadeSenha() {
    if (this.senhaType === "password") {
      this.senhaType = "text";
      this.iconName = "eye";
    } else {
      this.senhaType = "password";
      this.iconName = "eye-off";
    }
  }

  async cadastrarUser() {
    this.user.username = this.formGroup.value.username;
    this.user.email = this.formGroup.value.email;
    this.user.senha = this.formGroup.value.senha;
    this.userService.cadastrarUser(this.user);
    this.exibirMensagem('Usuário cadastrado com sucesso!');
    this.navController.navigateForward('login');
  }

  async exibirMensagem(texto: string) {
    const toast = await this.toastController.create({
      message: texto,
      duration: 1500
    });
    toast.present();
  }
}
