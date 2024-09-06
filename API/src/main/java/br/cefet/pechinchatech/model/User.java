package br.cefet.pechinchatech.model;

import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.Size;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class User {
    private Long id;

    @NotBlank(message = "Insira um username!")
    private String username;

    @NotBlank(message = "Insira um email!")
    private String email;
    
    @NotBlank(message = "Insira uma senha!")
    @Size(min = 8, max = 20)
    private String senha;
}
