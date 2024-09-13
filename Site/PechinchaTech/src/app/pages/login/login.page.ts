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

  passwordType: string = "password";
  iconName: string = "eye-off";

  constructor(private navController: NavController, private formBuilder: FormBuilder, private userService: UserService) { 
    this.user = new User();
    this.formGroup = this.formBuilder.group({
      emailOrUsername: ['', Validators.compose([Validators.required])],
      senha: ['', Validators.compose([Validators.required])]
    })
  }

  ngOnInit() {
    this.userService.encerrarSessao();
  }

  togglePasswordVisibility() {
    if (this.passwordType === 'password') {
      this.passwordType = 'text';
      this.iconName = 'eye';
    } else {
      this.passwordType = 'password';
      this.iconName = 'eye-off';
    }
  }

}
