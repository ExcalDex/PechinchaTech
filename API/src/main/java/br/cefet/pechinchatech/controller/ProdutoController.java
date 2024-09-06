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

import br.cefet.pechinchatech.model.Produto;
import br.cefet.pechinchatech.service.ProdutoService;
import jakarta.validation.Valid;

@RestController
@RequestMapping("/api/produto")
public class ProdutoController {

	private final ProdutoService pService;

    public ProdutoController(ProdutoService pService){
		this.pService = pService;
	}

    @GetMapping({"/", ""})
	public ResponseEntity<List<Produto>> listaProduto() {
		return ResponseEntity.ok(pService.consultar());
	}

    @GetMapping({"/{id}"})
	public ResponseEntity<Produto> consultaProduto(@PathVariable Long id) {
		return ResponseEntity.ok(pService.consultar(id));
	}

	@PostMapping({"/", ""})
	public ResponseEntity<Produto> inserir(@Valid @RequestBody Produto p) {
		return ResponseEntity.ok(pService.inserir(p));
		
	}

	@PostMapping({"/", ""})
	public ResponseEntity<List<Produto>> inserir(@Valid @RequestBody List<Produto> p) {
		return ResponseEntity.ok(pService.inserir(p));
		
	}

	@PutMapping({"/", ""})
	public ResponseEntity<Produto> alterar(@RequestBody Produto p){
		return ResponseEntity.ok(pService.alterar(p));
	}

	@DeleteMapping({"/{id}"})
	public ResponseEntity<Produto> excluir(@PathVariable Long id){
		return ResponseEntity.ok(pService.excluir(id));
	}
    
}

