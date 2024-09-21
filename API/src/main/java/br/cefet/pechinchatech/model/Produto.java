package br.cefet.pechinchatech.model;

import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;
import jakarta.validation.constraints.Size;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class Produto {
	Long id;

	@NotBlank(message = "Insira o nome do produto!")
	@Size(min = 2)
	String nome;
	
	@NotBlank(message = "Insira um link para o produto!")
	String link;

	@NotNull(message = "Insira um preço para o produto!")
	double preco;

	@NotNull(message = "Insira uma loja!")
	Lojas loja;
	
	@NotNull(message = "Insira um tipo de produto!")
	TipoProduto tipo;

	@NotNull(message = "Insira um id de produto base!")
	Long id_produto_base;

	@NotBlank(message = "Insira a imagem do produto!")
	@Size(min = 2)
	String link_imagem;
}
