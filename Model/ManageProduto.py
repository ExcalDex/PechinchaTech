import re, pandas as pd, os
from enum import Enum
import numpy


class Lojas(Enum):
    AMAZON = (1,)
    KABUM = (2,)
    PICHAU = (3,)
    MERCADO_LIVRE = (4,)
    TERABYTE = 5


class Tipo_Produto(Enum):
    CPU = (1,)
    GPU = (2,)
    HDD = (3,)
    RAM = (4,)
    SSD = 5


class Produto:

    benchmark_dir: str = f"{os.getcwd()}\\benchmark"
    tabela_cpu: pd.DataFrame = pd.read_csv(f"{benchmark_dir}\\CPU_UserBenchmarks.csv")
    tabela_gpu: pd.DataFrame = pd.read_csv(f"{benchmark_dir}\\GPU_UserBenchmarks.csv")
    tabela_hdd: pd.DataFrame = pd.read_csv(f"{benchmark_dir}\\HDD_UserBenchmarks.csv")
    tabela_ram: pd.DataFrame = pd.read_csv(f"{benchmark_dir}\\RAM_UserBenchmarks.csv")
    tabela_ssd: pd.DataFrame = pd.read_csv(f"{benchmark_dir}\\SSD_UserBenchmarks.csv")
    tabela_geral: numpy.ndarray

    def __init__(
        self, nome_prov: str, tipo: Tipo_Produto, valor: float, link: str, loja: Lojas
    ) -> None:
        self.__tipo: Tipo_Produto = tipo
        self.__valor: float = valor
        self.__link: str = link
        self.__loja: Lojas = loja
        self.__nome: str = self.__identificar_produto(nome_prov)

    def get_tipo(self) -> str:
        return self.__tipo.name

    def get_valor(self) -> float:
        return self.__valor

    def get_link(self) -> str:
        return self.__link

    def get_loja(self) -> str:
        return self.__loja.name

    def get_nome(self) -> str:
        return self.__nome

    def __identificar_produto(self, nome_prov: str) -> str:

        if self.__tipo == Tipo_Produto.CPU:
            Produto.tabela_geral = Produto.tabela_cpu.to_numpy()

        if self.__tipo == Tipo_Produto.GPU:
            Produto.tabela_geral = Produto.tabela_gpu.to_numpy()

        if self.__tipo == Tipo_Produto.HDD:
            Produto.tabela_geral = Produto.tabela_hdd.to_numpy()

        if self.__tipo == Tipo_Produto.RAM:
            Produto.tabela_geral = Produto.tabela_ram.to_numpy()

        if self.__tipo == Tipo_Produto.SSD:
            Produto.tabela_geral = Produto.tabela_ssd.to_numpy()

        if self.__tipo == None:
            return ""

        largest_match: int = 0
        final_model: str = ""
        curr_match: int
        for j in range(len(Produto.tabela_geral)):
            curr_match = 0
            splitted_text: list[str] = (
                str(Produto.tabela_geral[j][1]).replace("-", " ").split(" ")
            )
            splitted_text.extend(str(Produto.tabela_geral[j][3]).split())

            if "3060" in str(Produto.tabela_geral[j][3]):
                ...

            for s in splitted_text:
                if s in nome_prov and len(s) > 1:
                    curr_match += len(s)

            if curr_match > largest_match:
                largest_match = curr_match
                final_model = Produto.tabela_geral[j][3]

        return final_model
