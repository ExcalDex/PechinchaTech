package br.cefet.pechinchatech.dao;

import java.util.List;

import org.jdbi.v3.sqlobject.config.RegisterBeanMapper;
import org.jdbi.v3.sqlobject.customizer.Bind;
import org.jdbi.v3.sqlobject.customizer.BindBean;
import org.jdbi.v3.sqlobject.statement.GetGeneratedKeys;
import org.jdbi.v3.sqlobject.statement.SqlQuery;
import org.jdbi.v3.sqlobject.statement.SqlUpdate;
import org.springframework.stereotype.Repository;

import br.cefet.pechinchatech.model.Produto;

@Repository
@RegisterBeanMapper(Produto.class)
public interface ProdutoDao {

    @GetGeneratedKeys
    @SqlUpdate(" insert into produto (nome, preco, link, loja, tipo, id_produto_base) "
            + " values (:nome, :preco, :link, :loja, :tipoProduto, :idProdutoBase);")
    public Long inserir(@BindBean Produto p);

    @SqlQuery("SELECT * FROM produto;")
    public List<Produto> consultar();

    @SqlQuery("SELECT * FROM produto WHERE produto.id = :id;")
    public Produto consultar(@Bind("id") Long id);

    @SqlUpdate("UPDATE produto SET nome = :nome, preco = :preco, link = :link, loja = :loja, tipo = :tipoProduto, id_produto_base = :idProdutoBase WHERE id = :id;")
    public int alterar(@BindBean Produto p);

    @SqlUpdate("DELETE FROM produto WHERE id = :id;")
    public int excluir(@Bind("id") Long id);
}
