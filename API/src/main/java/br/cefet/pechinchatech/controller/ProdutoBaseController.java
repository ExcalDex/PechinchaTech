package br.cefet.pechinchatech.controller;

import java.util.List;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import br.cefet.pechinchatech.model.ProdutoBase;
import br.cefet.pechinchatech.service.ProdutoBaseService;
import jakarta.validation.Valid;

@CrossOrigin
@RestController
@RequestMapping("/api/produtobase")
public class ProdutoBaseController {
    private final ProdutoBaseService pbService;

    public ProdutoBaseController(ProdutoBaseService pbService){
        this.pbService = pbService;
    }

    @GetMapping({"/", ""})
    public ResponseEntity<List<ProdutoBase>> consultar() {
        return ResponseEntity.ok(pbService.consultar());
    }

    @PostMapping({"/", ""})
	public ResponseEntity<ProdutoBase> inserir(@Valid @RequestBody ProdutoBase p) {
		return ResponseEntity.ok(pbService.inserir(p));
	}

    @GetMapping("/match/{nome}")
    public ResponseEntity<Long> matchNomeId(@PathVariable String nome) {
        return ResponseEntity.ok(pbService.match_id(nome));
    }

    @GetMapping("/{id}")
    public ResponseEntity<ProdutoBase> consultar(@PathVariable Long id) {
        return ResponseEntity.ok(pbService.consultar(id));
    }
    
    
}
