package br.cefet.pechinchatech.service;

    import java.util.List;

import org.jdbi.v3.core.Jdbi;
import org.springframework.http.HttpStatus;
import org.springframework.stereotype.Service;
import org.springframework.web.server.ResponseStatusException;

import br.cefet.pechinchatech.dao.ProdutoBaseDao;
import br.cefet.pechinchatech.model.ProdutoBase;

@Service
public class ProdutoBaseService {

    
    private final ProdutoBaseDao produtoBaseDao;

    public ProdutoBaseService(Jdbi jdbi) {
        this.produtoBaseDao = jdbi.onDemand(ProdutoBaseDao.class);
    }

    public ProdutoBase inserir(ProdutoBase p) {
        if (p.getId() != null) {
            throw new ResponseStatusException(HttpStatus.NOT_ACCEPTABLE, "Não insira Id!");
        }

        Long id = produtoBaseDao.inserir(p);
        p.setId(id);
        return p;
    }

    // Update completo usando o bot. Preciso testar depois, mas provavelmente funciona melhor do que ativar a notificação SSE pra cada vez que um objeto é adicionado ao banco

    public List<ProdutoBase> consultar() {
        return produtoBaseDao.consultar();
    }

    public Long match_id(String p_nome){
        if (p_nome == null || p_nome.isBlank()) {
            throw new ResponseStatusException(HttpStatus.NOT_ACCEPTABLE, "Insira um nome!");
        }

        return produtoBaseDao.encontrar_id(p_nome);
    }
}

