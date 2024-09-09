import pandas as pd, os
from enum import Enum
import numpy
from typing import Any
import requests


class Lojas(Enum):
    KABUM = (1,)
    MERCADO_LIVRE = 2


class Tipo_Produto(Enum):
    CPU = (1,)
    GPU = (2,)
    HDD = (3,)
    RAM = (4,)
    SSD = 5


class Produto:

    __benchmark_dir: str = f"{os.getcwd()}\\benchmark"
    __tabela_cpu: pd.DataFrame = pd.read_csv(
        f"{__benchmark_dir}\\CPU_UserBenchmarks.csv"
    )
    __tabela_gpu: pd.DataFrame = pd.read_csv(
        f"{__benchmark_dir}\\GPU_UserBenchmarks.csv"
    )
    __tabela_hdd: pd.DataFrame = pd.read_csv(
        f"{__benchmark_dir}\\HDD_UserBenchmarks.csv"
    )
    __tabela_ram: pd.DataFrame = pd.read_csv(
        f"{__benchmark_dir}\\RAM_UserBenchmarks.csv"
    )
    __tabela_ssd: pd.DataFrame = pd.read_csv(
        f"{__benchmark_dir}\\SSD_UserBenchmarks.csv"
    )
    __tabela_geral: numpy.ndarray

    def __init__(
        self, nome_prov: str, tipo: Tipo_Produto, valor: float, link: str, loja: Lojas, link_img: str
    ) -> None:
        self.__tipo: Tipo_Produto = tipo
        self.__valor: float = valor
        self.__link: str = link
        self.__loja: Lojas = loja
        self.__nome: str = self.__identificar_produto(nome_prov)
        self.__link_img: str = link_img

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
    
    def get_img(self) -> str:
        return self.__link_img

    def __identificar_produto(self, nome_prov: str) -> str:

        if self.__tipo == Tipo_Produto.CPU:
            Produto.__tabela_geral = Produto.__tabela_cpu.to_numpy()

        if self.__tipo == Tipo_Produto.GPU:
            Produto.__tabela_geral = Produto.__tabela_gpu.to_numpy()

        if self.__tipo == Tipo_Produto.HDD:
            Produto.__tabela_geral = Produto.__tabela_hdd.to_numpy()

        if self.__tipo == Tipo_Produto.RAM:
            Produto.__tabela_geral = Produto.__tabela_ram.to_numpy()

        if self.__tipo == Tipo_Produto.SSD:
            Produto.__tabela_geral = Produto.__tabela_ssd.to_numpy()

        if self.__tipo == None:
            return ""

        largest_match: int = 4
        final_model: str = ""
        curr_match: int
        for i in range(len(Produto.__tabela_geral)):
            curr_match = 0
            splitted_text: list[str] = (
                str(Produto.__tabela_geral[i][3]).split(" ")
            )

            for s in splitted_text:
                if s in nome_prov:
                    curr_match += len(s)

            if curr_match >=largest_match:
                largest_match = curr_match
                final_model = Produto.__tabela_geral[i][3]

        return final_model
    
    def to_dict(self) -> dict[str, Any]:
        return {
            'nome' : self.get_nome(),
            'preco' : self.get_valor(),
            'link' : self.get_link(),
            'loja' : self.get_loja(),
            'tipoProduto' : self.get_tipo(),
            'idProdutoBase' : self.get_idProdutoBase(),
            'imageLink' : self.get_img()
        }
    
    
    def get_idProdutoBase(self) -> int:
        session = session = requests.Session()
        if not self.__nome.isspace() and len(self.__nome) > 3:
            try:
                r = session.get(f'http://localhost:8087/api/produtobase/match/{self.__nome}')
                r.raise_for_status()  # Check for HTTP errors
                try:
                    return int(r.content)
                except ValueError:
                    print(f"Invalid response content: {r.content}")
                    return -1
            except requests.exceptions.RequestException as e:
                print(f"Request failed: {e}")
                return -1
        return -1
