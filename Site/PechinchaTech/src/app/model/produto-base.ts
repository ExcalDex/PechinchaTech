enum Tipo {
    "SSD",
    "HDD",
    "GPU",
    "CPU",
    "RAM"
}

export class ProdutoBase {
    id: number;
    nome: string;
    csv_row: number;
    tipo: Tipo;
    marca: string;
    rank_userbenchmark: number;
    score_userbenchmark: number;

    constructor() {
        this.id = 0;
        this.nome = "";
        this.csv_row = 0;
        this.tipo = Tipo.SSD;
        this.marca = "";
        this.rank_userbenchmark = 0;
        this.score_userbenchmark = 0;
    }
}
