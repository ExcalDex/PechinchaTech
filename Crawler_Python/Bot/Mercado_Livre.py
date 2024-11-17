import asyncio
import requests
import aiohttp
from lxml import html
import re
from typing import Any
from Model.ManageProduto import Tipo_Produto
from bs4 import BeautifulSoup

NUMERO_DE_REQUESTS_AO_MESMO_TEMPO: int = 100


class Scraper:
    def __init__(self, produto: Tipo_Produto) -> None:
        self.__produto: Tipo_Produto = produto
        self.__data: dict[str, list[Any]] = {
            "Nome": [],
            "Valor": [],
            "Link": [],
            "Tipo": [],
            "Imagem": [],
        }
        self.__semaphore = asyncio.Semaphore(NUMERO_DE_REQUESTS_AO_MESMO_TEMPO)

    def get_produtos(self) -> dict[str, list[str]]:
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
            "Imagem": self.__data["Imagem"].copy(),
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
        produto = ""
        if self.__produto == Tipo_Produto.CPU:
            produto = "processadores/processador"
        if self.__produto == Tipo_Produto.GPU:
            produto = "placas/placa-video/placa-de-video"
        if self.__produto == Tipo_Produto.HDD:
            produto = "discos-acessorios/hds-ssds/hd"
        if self.__produto == Tipo_Produto.SSD:
            produto = "discos-acessorios/hds-ssds/ssd"

        tasks = []
        async with aiohttp.ClientSession() as session:
            for i in range(1, 43):
                url: str = f"https://lista.mercadolivre.com.br/informatica/componentes-pc/{produto}_Desde_{((i-1) * 48) + 1}_NoIndex_True"
                tasks.append(self.__fetch(session, url))
            responses = await asyncio.gather(*tasks)

        for page in responses:
            bs_page = BeautifulSoup(page, "html.parser")
            products = bs_page.find_all('li', class_='ui-search-layout__item')
            
            nomes: list = []
            valores: list = []
            links: list = []
            imagens: list = []

            for product in products:
                h2 = product.find('h2', class_='poly-box poly-component__title')
                a = h2.find('a')
                div = product.find('div', class_='poly-price__current')
                span = div.find('span', class_='andes-money-amount andes-money-amount--cents-superscript')
                img = product.find('img', class_='poly-component__picture')
                
                nomes.append(a.text)
                valores.append(span.get('aria-label'))
                links.append(a.get('href'))
                imagens.append(img.get('src'))

            
            for j in range(len(valores)):
                valores[j] = (
                    valores[j]
                    .replace(" ", "")
                    .replace("reais", " ")
                    .replace("com", "")
                    .replace("centavos", "")
                )
                numeros = re.findall(r"\d+", valores[j])
                if len(numeros) == 1:
                    reais = int(numeros[0])
                    centavos = 0
                else:
                    reais = int(numeros[0])
                    centavos = int(numeros[1])
                valores[j] = reais + (centavos / 100)


            self.__data["Nome"] += nomes
            self.__data["Valor"] += valores
            self.__data["Link"] += links
            self.__data["Tipo"] += [self.__produto.name for i in range(len(nomes))]
            self.__data["Imagem"] += imagens
