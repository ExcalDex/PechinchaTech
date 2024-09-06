package br.cefet.pechinchatech.model;

import jakarta.validation.constraints.NotBlank;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class Notif {
    @NotBlank
    Long idProdutoBase;

    @NotBlank
    Long idUsuario;
}
