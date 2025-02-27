import { Injectable } from '@angular/core';
import { ToastController } from '@ionic/angular';

@Injectable({
  providedIn: 'root',
})
export class SseService {
  private eventSource: EventSource | null = null;

  constructor(private toastController: ToastController) {}

  connect(url: string) {
    this.eventSource = new EventSource(url);

    this.eventSource.onmessage = (event) => {
      this.exibirMensagem(event.data);
      alert(event.data);
      console.log(event);
    }

    this.eventSource.onerror = (error) => {
      console.error("Erro ao receber evento SSE", error);
    }
  }


  disconnect() {
    if (this.eventSource) {
      this.eventSource.close();
      this.eventSource = null;
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
