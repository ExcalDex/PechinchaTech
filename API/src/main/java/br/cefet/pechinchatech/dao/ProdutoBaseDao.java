package br.cefet.pechinchatech.dao;

import java.util.List;

import org.springframework.stereotype.Repository;
import org.jdbi.v3.sqlobject.config.RegisterBeanMapper;
import org.jdbi.v3.sqlobject.customizer.Bind;
import org.jdbi.v3.sqlobject.customizer.BindBean;
import org.jdbi.v3.sqlobject.statement.GetGeneratedKeys;
import org.jdbi.v3.sqlobject.statement.SqlQuery;
import org.jdbi.v3.sqlobject.statement.SqlUpdate;

import br.cefet.pechinchatech.model.ProdutoBase;

@Repository
@RegisterBeanMapper(ProdutoBase.class)
public interface ProdutoBaseDao {

    @SqlUpdate(" insert into produto_base (nome, csv_row, tipo, marca, rank_userbenchmark, score_userbenchmark) "
            + " values (:nome, :csv_row, :tipo, :marca, :rank_userbenchmark, :score_usuerbenchmark);")
    @GetGeneratedKeys
    public Long inserir(@BindBean ProdutoBase p);

    @SqlQuery("SELECT * FROM produto_base;")
    public List<ProdutoBase> consultar();

    @SqlQuery("SELECT * FROM produto_base WHERE :id = produto_base.id;")
    public ProdutoBase consultar(@Bind("id") Long id);

    @SqlQuery("SELECT id FROM produto_base WHERE :nome = produto_base.nome")
    public Long encontrar_id(@Bind("nome") String nome);

}
