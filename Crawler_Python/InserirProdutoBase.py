import pandas as pd
import os
import numpy
import requests
import json


if __name__ == "__main__":
    benchmark_dir: str = f"{os.getcwd()}\\benchmark"
    tipo_tup: tuple = ("CPU", "GPU", "HDD", "SSD")
    for tipo in tipo_tup:
        tabela: pd.DataFrame = pd.read_csv(
            f"{benchmark_dir}\\{tipo}_UserBenchmarks.csv"
        )
        matriz: numpy.ndarray = tabela.to_numpy()
        del tabela
        for i in range(len(matriz)):
            data = {
                "tipo": matriz[i][0],
                "marca": matriz[i][2],
                "nome": matriz[i][3],
                "rank_userbenchmark": matriz[i][4],
                "score_userbenchmark": matriz[i][5],
                "csv_row": matriz[i][4] - 1,
            }
            requests.post(
                "http://localhost:8087/api/produtobase/",
                data=json.dumps(data),
                headers={"Content-Type": "application/json"},
            )
