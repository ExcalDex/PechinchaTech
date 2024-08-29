import asyncio
from typing import Any
import requests
from lxml import html
import re
from Model.ManageProduto import Tipo_Produto


class Scraper:
    def __init__(self, produto: Tipo_Produto) -> None:
        self.__produto: Tipo_Produto = produto
        self.__data: dict[str, list[str]] = {"Nome": [], "Valor": [], "Link": [], "Tipo": []}

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
            "Tipo": self.__data["Tipo"].copy()
        }

    def set_produto(self, produto: Tipo_Produto) -> None:
        self.__produto = produto

    async def __get_all_products(self) -> None:
        produto = ""
        if self.__produto == Tipo_Produto.CPU:
            produto = "processadores/processador"
        if self.__produto == Tipo_Produto.GPU:
            produto = "placas/placa-video/placa-de-video"
        if self.__produto == Tipo_Produto.HDD:
            produto = "discos-acessorios/hds-ssds/hd"
        if self.__produto == Tipo_Produto.RAM:
            produto = "memorias-ram/ram"
        if self.__produto == Tipo_Produto.SSD:
            produto = "discos-acessorios/hds-ssds/ssd"

        page = requests.get(
            f"https://lista.mercadolivre.com.br/informatica/componentes-pc/{produto}_Desde_48_NoIndex_True"
        )
        tree = html.fromstring(page.content)
        qtd_pages = 1

        for i in range(2, 13):
            temp_last_page = tree.xpath(
                f"/html/body/main/div/div[3]/section/nav/ul/li[{i}]/a/@href"
            )
            if not temp_last_page:
                qtd_pages = i - 3
                break
            elif i >= 12:
                page_10 = requests.get(f"{page.url}_Desde_433_NoIndex_True")
                qtd_pages = html.fromstring(page_10.content).xpath(
                    f"/html/body/main/div/div[3]/section/nav/ul/li[16]/a/text()"
                )
                qtd_pages = int(qtd_pages[0])

        for i in range(1, qtd_pages + 1):
            page = requests.get(f"{page.url}_Desde_{i * 48}_NoIndex_True")
            tree = html.fromstring(page.content)
            nomes: list = tree.xpath(f"//*[@class='ui-search-item__title']/text()")
            valores: list = tree.xpath(
                f"//*/div[(@class='ui-search-item__group__element ui-search-price__part-without-link') or (@class='ui-search-item__group ui-search-item__group--pds')]/div[(@class='ui-search-price ui-search-price--size-x-tiny ui-search-item__pds-best-price ui-search-item__group__element ui-search-color--black') or (@class='ui-search-price ui-search-price--size-medium')]/div[@class='ui-search-price__second-line']/span[@aria-roledescription='Preço']/@aria-label"
            )
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

            links: list = tree.xpath(
                f"//*[@class='ui-search-item__group__element ui-search-link__title-card ui-search-link']/@href"
            )
            self.__data["Nome"] += nomes
            self.__data["Valor"] += valores
            self.__data["Link"] += links
            self.__data["Tipo"] += [self.__produto.name for i in range(len(nomes))]
