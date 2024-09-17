import { Component, OnInit } from '@angular/core';

import { User } from 'src/app/model/user';
import { UserService } from 'src/app/services/user.service';
import { ToastController } from '@ionic/angular';
import { NavController } from '@ionic/angular';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-login',
  templateUrl: './login.page.html',
  styleUrls: ['./login.page.scss'],
})
export class LoginPage implements OnInit {

  user: User;
  formGroup: FormGroup;

  senhaType: string = "password";
  iconName: string = "eye-off";

  constructor(private toastController: ToastController, private navController: NavController, private formBuilder: FormBuilder, private userService: UserService) { 
    this.user = new User();
    this.formGroup = this.formBuilder.group({
      emailOrUsername: ['', Validators.compose([Validators.required])],
      senha: ['', Validators.compose([Validators.required])]
    })
  }

  ngOnInit() {
    this.userService.encerrarSessao();
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

  async autenticarUser() {
    const emailRegex = /^[^\s@]+@[^\s@]+$/;
    let emailOrUsername = this.formGroup.value.emailOrUsername;
    let senha = this.formGroup.value.senha;
    if (emailRegex.test(emailOrUsername)) {
      this.user = await this.userService.autenticarEmail(emailOrUsername, senha);
      if (this.user) {
        this.userService.registrarUserAutenticado(this.user)
        this.exibirMensagem('Login realizado com sucesso!');
        window.location.href = '/main';
      }else {
        this.exibirMensagem('Email ou Senha inválidos!');
      }
    }else {
      this.user = await this.userService.autenticarUsername(emailOrUsername, senha);
      if (this.user) {
        this.userService.registrarUserAutenticado(this.user);
        this.exibirMensagem('Login realizado com sucesso!');
        window.location.href = '/main';
      }else {
        this.exibirMensagem('Usuário ou Senha inválidos!');
      }
    }
  }

  async exibirMensagem(texto: string) {
    const toast = await this.toastController.create({
      message: texto,
      duration: 1500
    });
    toast.present();
  }
}
