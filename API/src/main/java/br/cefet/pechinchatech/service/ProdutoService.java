package br.cefet.pechinchatech.service;

import java.util.List;

import org.jdbi.v3.core.Jdbi;
import org.springframework.http.HttpStatus;
import org.springframework.stereotype.Service;
import org.springframework.web.server.ResponseStatusException;

import br.cefet.pechinchatech.dao.ProdutoDao;
import br.cefet.pechinchatech.model.Produto;

@Service
public class ProdutoService {
    private final ProdutoDao produtoDao;

    public ProdutoService(Jdbi jdbi) {
        this.produtoDao = jdbi.onDemand(ProdutoDao.class);
    }

    public Produto inserir(Produto p) {
        if (p.getId() != null) {
            throw new ResponseStatusException(HttpStatus.NOT_ACCEPTABLE, "Não insira Id!");
        }

        Long id = produtoDao.inserir(p);
        p.setId(id);
        return p;
    }

    public List<Produto> consultar() {
        return produtoDao.consultar();
    }

    public Produto consultar(Long id) {
        return produtoDao.consultar(id);
    }
    
    public Produto alterar(Produto p) {
        Long id = p.getId();
        if (id == null) {
            throw new ResponseStatusException(HttpStatus.PRECONDITION_FAILED, "Insira um Id!");
        }
        Produto pAux = produtoDao.consultar(id);
        if (pAux == null){
            throw new ResponseStatusException(HttpStatus.NOT_FOUND, "Produto nao encontrado com o id: " +id+ ".");
        }
        int qtd = produtoDao.alterar(p);
        if (qtd != 1){
            throw new ResponseStatusException(HttpStatus.CONFLICT, "A quantidade de entidades alteradas é: " +qtd+ ".");
        }
        pAux = produtoDao.consultar(id);
        return pAux;
    }

    public Produto excluir(Long id) {
        Produto pAux = produtoDao.consultar(id);
        if (pAux == null){
            throw new ResponseStatusException(HttpStatus.NOT_FOUND, "Produto nao encontrado com o id: " +id+ ".");
        }
        int qtd = produtoDao.excluir(id);
        if (qtd != 1){
            throw new ResponseStatusException(HttpStatus.CONFLICT, "A quantidade de entidades alteradas eh " +qtd+ ".");
        }
        return pAux;
    }
}
