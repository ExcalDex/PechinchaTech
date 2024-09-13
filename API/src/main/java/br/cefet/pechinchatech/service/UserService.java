package br.cefet.pechinchatech.service;

import java.util.List;

import org.jdbi.v3.core.Jdbi;
import org.springframework.http.HttpStatus;
import org.springframework.stereotype.Service;
import org.springframework.web.server.ResponseStatusException;

import br.cefet.pechinchatech.dao.UserDao;
import br.cefet.pechinchatech.model.User;

@Service
public class UserService {
    private final UserDao uDao;

    public UserService(Jdbi jdbi) {
        this.uDao = jdbi.onDemand(UserDao.class);
    }

    public User login(String loginStr, String password, boolean tipoDeLogin){
        if(loginStr.isBlank() || password.isBlank() || loginStr == null || password == null){
            throw new ResponseStatusException(HttpStatus.NOT_ACCEPTABLE, "Insira todos os dados!");
        }

        if(tipoDeLogin)
            return uDao.loginU(loginStr, password);
        else 
            return uDao.loginE(loginStr, password);
    }

    public User inserir(User p) {
        if (p.getId() != null) {
            throw new ResponseStatusException(HttpStatus.NOT_ACCEPTABLE, "Não insira Id!");
        }

        Long id = uDao.inserir(p);
        p.setId(id);
        return p;
    }

    public List<User> consultar() {
        return uDao.consultar();
    }

    public User consultar(Long id) {
        return uDao.consultar(id);
    }
    
    public User alterar(User p) {
        Long id = p.getId();
        if (id == null) {
            throw new ResponseStatusException(HttpStatus.PRECONDITION_FAILED, "Insira um Id!");
        }
        User pAux = uDao.consultar(id);
        if (pAux == null){
            throw new ResponseStatusException(HttpStatus.NOT_FOUND, "User nao encontrado com o id: " +id+ ".");
        }
        int qtd = uDao.atualizar(p);
        if (qtd != 1){
            throw new ResponseStatusException(HttpStatus.CONFLICT, "A quantidade de entidades alteradas é: " +qtd+ ".");
        }
        pAux = uDao.consultar(id);
        return pAux;
    }

    public User excluir(Long id) {
        User pAux = uDao.consultar(id);
        if (pAux == null){
            throw new ResponseStatusException(HttpStatus.NOT_FOUND, "User nao encontrado com o id: " +id+ ".");
        }
        int qtd = uDao.deletar(id);
        if (qtd != 1){
            throw new ResponseStatusException(HttpStatus.CONFLICT, "A quantidade de entidades alteradas é " +qtd+ ".");
        }
        return pAux;
    }
}
