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

    private final SseService sService;
    
    private final ProdutoDao produtoDao;

    public ProdutoService(Jdbi jdbi, SseService sService) {
        this.produtoDao = jdbi.onDemand(ProdutoDao.class);
        this.sService = sService;
    }

    public Produto inserir(Produto p) {
        if (p.getId() != null) {
            throw new ResponseStatusException(HttpStatus.NOT_ACCEPTABLE, "Não insira Id!");
        }

        Long id = produtoDao.inserir(p);
        p.setId(id);
        return p;
    }

    // Update completo usando o bot. Preciso testar depois, mas provavelmente funciona melhor do que ativar a notificação SSE pra cada vez que um objeto é adicionado ao banco
    public List<Produto> inserir(List<Produto> pl) {
        for (Produto p : pl) {
            if (p.getId() != null) {
                throw new ResponseStatusException(HttpStatus.NOT_ACCEPTABLE, "Não insira Id!");
            }
    
            Long id = produtoDao.inserir(p);
            p.setId(id);
        }
        this.sService.notificarClientes(pl);
        return pl;
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
