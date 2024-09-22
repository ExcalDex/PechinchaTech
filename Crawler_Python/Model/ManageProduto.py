import pandas as pd, os
from enum import Enum
import numpy
from typing import Any
import requests
import difflib
import nltk
nltk.download('punkt_tab')
import string


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
        self,
        nome_prov: str,
        tipo: str,
        valor: float,
        link: str,
        loja: str,
        link_img: str,
    ) -> None:
        self.__tipo: str = tipo
        self.__valor: float = valor
        self.__link: str = link
        self.__loja: str = loja
        self.__nome: str = self.__identificar_produto(nome_prov)
        self.__link_img: str = link_img

    def get_tipo(self) -> str:
        return self.__tipo

    def get_valor(self) -> float:
        return self.__valor

    def get_link(self) -> str:
        return self.__link

    def get_loja(self) -> str:
        return self.__loja

    def get_nome(self) -> str:
        return self.__nome

    def get_img(self) -> str:
        return self.__link_img

    def __preprocess(self, text: str) -> str:
        text = text.lower()
        text = text.translate(str.maketrans("", "", string.punctuation))
        # Tokenize
        tokens = nltk.word_tokenize(text)
        return " ".join(tokens)

    def __identificar_produto(self, nome_prov: str) -> str:
        if self.__tipo == Tipo_Produto.CPU.name:
            Produto.__tabela_geral = Produto.__tabela_cpu.to_numpy()

        if self.__tipo == Tipo_Produto.GPU.name:
            Produto.__tabela_geral = Produto.__tabela_gpu.to_numpy()

        if self.__tipo == Tipo_Produto.HDD.name:
            Produto.__tabela_geral = Produto.__tabela_hdd.to_numpy()

        if self.__tipo == Tipo_Produto.RAM.name:
            Produto.__tabela_geral = Produto.__tabela_ram.to_numpy()

        if self.__tipo == Tipo_Produto.SSD.name:
            Produto.__tabela_geral = Produto.__tabela_ssd.to_numpy()

        if self.__tipo == None:
            return ""

        lista_nomes_produtos_base: list[str] = []
        for p in Produto.__tabela_geral:
            lista_nomes_produtos_base.append(p[3])
        lista_nomes_produtos_base = [
            self.__preprocess(name) for name in lista_nomes_produtos_base
        ]
        best_match: str = ''
        highest_score: float = 0
        for p in lista_nomes_produtos_base:
            score: float = difflib.SequenceMatcher(None, nome_prov, p).ratio()
            if score > highest_score:
                highest_score = score
                best_match = p

        return best_match

    def to_dict(self) -> dict[str, Any]:
        return {
            "nome": self.get_nome(),
            "preco": self.get_valor(),
            "link": self.get_link(),
            "loja": self.get_loja(),
            "tipoProduto": self.get_tipo(),
            "idProdutoBase": self.get_idProdutoBase(),
            "imageLink": self.get_img(),
        }

    def get_idProdutoBase(self) -> int:
        session = session = requests.Session()
        if not self.__nome.isspace() and len(self.__nome) > 3:
            try:
                r = session.get(
                    f"http://localhost:8087/api/produtobase/match/{self.__nome}"
                )
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
