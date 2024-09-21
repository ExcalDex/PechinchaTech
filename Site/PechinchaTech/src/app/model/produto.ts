enum Loja {
    "KABUM",
    "MERCADO_LIVRE"
}

enum Tipo {
    "SSD",
    "HDD",
    "GPU",
    "CPU",
    "RAM"
}

export class Produto {
    id: number;
    nome: string;
    preco: number;
    link: string;
    loja: Loja;
    tipo: Tipo;
    id_produto_base: number;
    link_imagem: string;

    constructor() {
        this.id = 0;
        this.nome = "";
        this.preco = 0;
        this.link = "";
        this.loja = Loja.KABUM;
        this.tipo = Tipo.SSD;
        this.id_produto_base = 0;
        this.link_imagem = "";
    }

}
