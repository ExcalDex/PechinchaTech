package br.cefet.pechinchatech.dao;

import java.util.List;

import org.jdbi.v3.sqlobject.config.RegisterBeanMapper;
import org.jdbi.v3.sqlobject.customizer.Bind;
import org.jdbi.v3.sqlobject.customizer.BindBean;
import org.jdbi.v3.sqlobject.statement.GetGeneratedKeys;
import org.jdbi.v3.sqlobject.statement.SqlQuery;
import org.jdbi.v3.sqlobject.statement.SqlUpdate;
import org.springframework.stereotype.Repository;

import br.cefet.pechinchatech.model.User;

@Repository
@RegisterBeanMapper(User.class)
public interface UserDao {

    @SqlUpdate("INSERT INTO usuario (username, email, senha) values(:username, :email, :senha);")
    @GetGeneratedKeys
    public Long inserir(@BindBean User u);

    @SqlQuery("SELECT * FROM usuario;")
    public List<User> consultar();

    @SqlQuery("SELECT * FROM usuario WHERE usuario.id = :id ")
    public User consultar(@Bind("id") Long id);

    @SqlUpdate("UPDATE usuario SET username = :username, senha = :senha, email = :email WHERE id = :id")
    public int atualizar(@BindBean User u);

    @SqlUpdate("DELETE FROM usuario WHERE id = :id")
    public int deletar(@Bind("id") Long id);
}
