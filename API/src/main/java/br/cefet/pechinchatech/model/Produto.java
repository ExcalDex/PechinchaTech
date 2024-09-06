package br.cefet.pechinchatech.model;

import jakarta.validation.constraints.Min;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;
import jakarta.validation.constraints.Size;
import lombok.AllArgsConstructor;
import lombok.Data;

@Data
@AllArgsConstructor

public class Produto {
	Long id;

	@NotBlank(message = "Insira o nome do produto!")
	@Size(min = 2, max = 65)
	String nome;
	
	@NotBlank(message = "Insira um link para o produto!")
	String link;

	@NotBlank(message = "Insira um preço para o produto!")
	double preco;

	@NotNull(message = "Insira uma loja!")
	Lojas loja;
	
	@NotNull(message = "Insira um tipo de produto!")
	TipoProduto tipoProduto;

	@NotNull(message = "Insira um id de produto base!")
	@Min(1)
	Long idProdutoBase;

	@NotBlank(message = "Insira a imagem do produto!")
	@Size(min = 2)
	String imageLink;
}
