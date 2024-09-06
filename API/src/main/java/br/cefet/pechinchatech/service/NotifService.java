package br.cefet.pechinchatech.service;

import java.util.List;

import org.jdbi.v3.core.Jdbi;
import org.springframework.http.HttpStatus;
import org.springframework.stereotype.Service;
import org.springframework.web.server.ResponseStatusException;

import br.cefet.pechinchatech.dao.NotifDao;
import br.cefet.pechinchatech.model.Notif;

@Service
public class NotifService {
    
    private final NotifDao NotifDao;

    public NotifService(Jdbi jdbi) {
        this.NotifDao = jdbi.onDemand(NotifDao.class);
    }

    public Notif inserir(Notif n) {
        NotifDao.inserir(n);
        return n;
    }

    public List<Notif> consultar() {
        return NotifDao.consultar();
    }

    public Notif consultar(Long idpb, Long idu) {
        return NotifDao.consultar(idpb, idu);
    }
    

    public Notif excluir(Long idpb, Long idu) {
        Notif nAux = NotifDao.consultar(idpb, idu);
        if (nAux == null){
            throw new ResponseStatusException(HttpStatus.NOT_FOUND, "Notif nao encontrada com os ids: " +idpb+ " " +idu+ ".");
        }
        int qtd = NotifDao.excluir(idpb, idu);
        if (qtd != 1){
            throw new ResponseStatusException(HttpStatus.CONFLICT, "A quantidade de entidades alteradas eh " +qtd+ ".");
        }
        return nAux;
    }
}
