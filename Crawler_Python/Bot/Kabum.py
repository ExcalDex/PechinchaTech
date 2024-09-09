import asyncio
import aiohttp
import requests
from Model.ManageProduto import Tipo_Produto
from bs4 import BeautifulSoup
import json
from typing import Any

NUMERO_DE_REQUESTS_AO_MESMO_TEMPO: int = 100

class Scraper:
    def __init__(self, produto: Tipo_Produto) -> None:
        self.__produto: Tipo_Produto = produto
        self.__data: dict[str, list[Any]] = {"Nome": [], "Valor": [], "Link": [], "Tipo": [], "Imagem": []}
        self.__semaphore = asyncio.Semaphore(NUMERO_DE_REQUESTS_AO_MESMO_TEMPO)

    def get_produtos(self) -> dict[str, list[str]]:
        """Retorna um dict com os dados dos produtos, igual no self.__data

        Returns:
            dict[str, list[str]]: dados dos produtos
        """
        loop = asyncio.new_event_loop()

        if loop.is_running():
            loop.run_until_complete(self.__get_all_products())
        else:
            asyncio.run(self.__get_all_products())

        return {
            "Nome": self.__data["Nome"].copy(),
            "Valor": self.__data["Valor"].copy(),
            "Link": self.__data["Link"].copy(),
            "Tipo": self.__data["Tipo"].copy(),
            "Imagem": self.__data["Imagem"].copy()
        }

    def set_produto(self, produto: Tipo_Produto) -> None:
        self.__produto = produto

    async def __fetch(self, session, url: str) -> str:
        """Função para limitar o número de requisições web assíncronas ao mesmo tempo (alguns sites tem limite de acessos)

        Args:
            session (_type_): seção assíncrona
            url (_type_): link

        Returns:
            str: código html da página
        """
        async with self.__semaphore:
            async with session.get(url, ssl=False) as response:
                return await response.text()

    async def __get_all_products(self) -> None:
        """Reúne os dados dos produtos desejados."""
        tasks = []
        produto = ""
        if self.__produto == Tipo_Produto.CPU:
            produto = "processadores"
        if self.__produto == Tipo_Produto.GPU:
            produto = "placa-de-video-vga"
        if self.__produto == Tipo_Produto.HDD:
            produto = "disco-rigido-hd"
        if self.__produto == Tipo_Produto.RAM:
            produto = "memoria-ram"
        if self.__produto == Tipo_Produto.SSD:
            produto = "ssd-2-5"
        page = requests.get(
            f"https://www.kabum.com.br/hardware/{produto}"
        )  # Precisa fazer essa requisição de forma síncrona para retirar a quantidade de páginas
        primeira_pagina = BeautifulSoup(page.content, "html.parser")
        paginas = primeira_pagina.find_all("a", class_="page")
        qtd_pages = int(paginas[-1].string)

        async with aiohttp.ClientSession() as session:
            for i in range(1, qtd_pages + 1):
                url: str = f"{page.url}?&page_number={i}&facet_filters=&sort=-price"
                tasks.append(self.__fetch(session, url))
            responses = await asyncio.gather(*tasks)

        for page in responses:
            bs_page = BeautifulSoup(page, "html.parser")
            links = bs_page.find_all("script")[-1].string
            kabum_json = json.loads(links)
            try:
                produtos = kabum_json["props"]["pageProps"]["data"]["catalogServer"]["data"]
            except:
                produtos = json.loads(kabum_json["props"]["pageProps"]["data"])["catalogServer"]["data"]

            for produto in produtos:
                self.__data["Nome"].append(produto["name"])

                valor = (
                    produto["priceWithDiscount"]
                    if produto["priceWithDiscount"] > 0
                    else produto["price"]
                )
                self.__data["Valor"].append(valor)

                self.__data["Link"].append(
                    f"https://www.kabum.com.br/produto/{produto['code']}"
                )

                self.__data["Tipo"].append(self.__produto.name)

                self.__data["Imagem"].append(produto["image"])
