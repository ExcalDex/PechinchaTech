package br.cefet.pechinchatech.dao;

import java.util.List;

import org.jdbi.v3.sqlobject.config.RegisterBeanMapper;
import org.jdbi.v3.sqlobject.customizer.Bind;
import org.jdbi.v3.sqlobject.customizer.BindBean;
import org.jdbi.v3.sqlobject.statement.SqlQuery;
import org.jdbi.v3.sqlobject.statement.SqlUpdate;
import org.springframework.stereotype.Repository;

import br.cefet.pechinchatech.model.Notif;

@Repository
@RegisterBeanMapper(Notif.class)
public interface NotifDao {

    @SqlUpdate(" insert into notif (id_produto_base, id_usuario) "
            + " values (:idProdutoBase, :idUsuario);")
    public void inserir(@BindBean Notif n);

    @SqlQuery("SELECT * FROM notif;")
    public List<Notif> consultar();

    @SqlQuery("SELECT * FROM notif WHERE :idpb = notif.id_produto_base AND :idu = notif.id_usuario;")
    public Notif consultar(@Bind("idpb") Long idpb, @Bind("idu") Long idu);

    @SqlQuery("DELETE FROM notif WHERE :idpb = notif.id_produto_base AND :idu = notif.id_usuario;")
    public int excluir(@Bind("idpb") Long idpb, @Bind("idu") Long idu);

    @SqlQuery("SELECT * FROM notif WHERE :idu = notif.id_usuario")
    public List<Notif> consultar(@Bind("idu") Long idu);

}
