package br.cefet.pechinchatech.controller;

import java.util.List;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import br.cefet.pechinchatech.model.Notif;
import br.cefet.pechinchatech.service.NotifService;
import jakarta.validation.Valid;

@RestController
@RequestMapping("/api/notif")
public class NotifController {
    private final NotifService nService;

    public NotifController(NotifService nService){
		this.nService = nService;
	}

    @GetMapping({"/", ""})
	public ResponseEntity<List<Notif>> listaNotif() {
		return ResponseEntity.ok(nService.consultar());
	}

    @GetMapping({"/produtobase/{idpb}/usuario/{idu}"})
	public ResponseEntity<Notif> consultaNotif(@PathVariable Long idpb, @PathVariable Long idu) {
		return ResponseEntity.ok(nService.consultar(idpb, idu));
	}

	@PostMapping({"/", ""})
	public ResponseEntity<Notif> inserir(@Valid @RequestBody Notif n) {
		return ResponseEntity.ok(nService.inserir(n));
		
	}

	@DeleteMapping({"/produtobase/{idpb}/usuario/{idu}"})
	public ResponseEntity<Notif> excluir(@PathVariable Long idpb, @PathVariable Long idu){
		return ResponseEntity.ok(nService.excluir(idpb, idu));
	}
}
