package br.cefet.pechinchatech.controller;

import java.util.List;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import br.cefet.pechinchatech.model.User;
import br.cefet.pechinchatech.service.UserService;
import jakarta.validation.Valid;

@RestController
@RequestMapping("/api/usuario")
public class UserController {

	private final UserService uService;

    public UserController(UserService uService){
		this.uService = uService;
	}

    @GetMapping({"/", ""})
	public ResponseEntity<List<User>> listaUser() {
		return ResponseEntity.ok(uService.consultar());
	}

    @GetMapping({"/{id}"})
	public ResponseEntity<User> consultaUser(@PathVariable Long id) {
		return ResponseEntity.ok(uService.consultar(id));
	}

	@PostMapping({"/", ""})
	public ResponseEntity<User> inserir(@Valid @RequestBody User p) {
		return ResponseEntity.ok(uService.inserir(p));
	}

	@PutMapping({"/", ""})
	public ResponseEntity<User> alterar(@RequestBody User p){
		return ResponseEntity.ok(uService.alterar(p));
	}

	@DeleteMapping({"/{id}"})
	public ResponseEntity<User> excluir(@PathVariable Long id){
		return ResponseEntity.ok(uService.excluir(id));
	}
    
}
