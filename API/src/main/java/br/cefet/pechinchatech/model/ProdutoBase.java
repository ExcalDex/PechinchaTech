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
public class ProdutoBase {
    @NotNull(message = "Insira um score!")
    int score;

    @NotNull(message = "Insira um rank!")
    int rank;

    Long id;

    @NotBlank(message = "Insira um nome!")
    String nome_benchmark;

    @NotNull(message = "Insira um tipo!")
    TipoProduto tipo;

    @NotNull(message = "Insira um número da linha csv!")
    int csvRow;

    @NotBlank(message = "Insira uma marca!")
    @Size(max = 16)
    String marca;
}
