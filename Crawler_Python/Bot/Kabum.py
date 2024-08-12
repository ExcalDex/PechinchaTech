import asyncio
import aiohttp
import requests
from lxml import html
from Model.ManageProduto import Tipo_Produto


class Scraper:
    def __init__(self, produto: Tipo_Produto) -> None:
        self.__produto: Tipo_Produto = produto
        self.__links: list[str] = []
        self.__data: dict[str, list[str]] = {"Nome": [], "Valor": [], "Link": []}
        self.__semaphore = asyncio.Semaphore(80)

    def get_produtos(self) -> dict[str, list[str]]:
        """Retorna um dict com os dados dos produtos, igual no self.__data

        Returns:
            dict[str, list[str]]: dados dos produtos
        """
        loop = (
            asyncio.get_event_loop()
        )  # Checar a utilização do loop do asyncio para ter certeza que não vai dar problema no acesso de memória.
        if loop.is_running():
            return loop.run_until_complete(self.__main())
        else:
            return asyncio.run(self.__main())

    def set_produto(self, produto: Tipo_Produto) -> None:
        self.__produto = produto

    async def __main(self) -> dict[str, list[str]]:
        """Executa os códigos assíncronos

        Returns:
            dict[str, list[str]]: dados dos produtos
        """
        await self.__fetch_product_links()  # Prefiro deixar os dois métodos dentro dessa mesma função a fim de deixar o código mais plausível.
        await self.__get_content_from_links()
        return {
            "Nome": self.__data["Nome"].copy(),
            "Valor": self.__data["Valor"].copy(),
            "Link": self.__data["Link"].copy(),
        }

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

    async def __fetch_product_links(self) -> None:
        """Salva no self.__links todos os links que existem nas páginas de pesquisas, ou seja, salva todos os links dos produtos"""
        tasks = []
        pages = []
        produto = ""
        if self.__produto == Tipo_Produto.CPU:
            produto = "processador"
        if self.__produto == Tipo_Produto.GPU:
            produto = "placa de video"
        if self.__produto == Tipo_Produto.HDD:
            produto = "hd"
        if self.__produto == Tipo_Produto.RAM:
            produto = "ram"
        if self.__produto == Tipo_Produto.SSD:
            produto = "ssd"
        page = requests.get(
            f"https://www.kabum.com.br/busca/{produto}"
        )  # Precisa fazer essa requisição de forma síncrona para retirar a quantidade de páginas
        qtd_pages = html.fromstring(page.content).xpath(
            "/html/body/div[1]/div/div/div[1]/div[3]/div/div/div[2]/div[1]/div[3]/ul/li[12]/a/text()"
        )  # Acha aquele número do final da página pra achar a qtd total de páginas que tem que iterar
        qtd_pages = int(qtd_pages[0]) if qtd_pages else 1

        async with aiohttp.ClientSession() as session:
            for i in range(1, qtd_pages + 1):
                url: str = f"{page.url}?&page_number={i}"
                tasks.append(self.__fetch(session, url))
            responses = await asyncio.gather(*tasks)
            for response in responses:
                pages.append(response)

        for page in pages:
            tree = html.fromstring(page)
            for i in range(1, 21):
                link = tree.xpath(
                    f"/html/body/div[1]/div/div/div[1]/div[3]/div/div/div[2]/div[1]/main/article[{i}]/a/@href"
                )
                if link:
                    self.__links.append(
                        f"https://www.kabum.com.br{link[0]}"
                    )  # precisa colocar esse www.kabum antes pq na página principal os links vem sem.
                else:
                    break

    async def __get_content_from_links(self) -> None:
        """Acessa os links em self.__links e pega os dados de cada produto: nome e valor em reais."""
        tasks = []
        responses = []
        pages = []
        async with aiohttp.ClientSession() as session:
            for link in self.__links:
                tasks.append(self.__fetch(session, link))
            responses = await asyncio.gather(*tasks)
            for response in responses:
                pages.append(response)

        for page, link in zip(pages, self.__links):
            tree = html.fromstring(page)
            nome: list = tree.xpath(
                "/html/body/div[1]/div/div/main/article/section/div[3]/div[1]/div/h1/text()"
            )  # Localização do nome se tiver um aviso que tem desconto
            if not nome:
                nome = tree.xpath(
                    "/html/body/div[1]/div/div/main/article/section/div[2]/div[1]/div/h1/text()"
                )  # Localização do nome se não tiver um aviso que tem desconto
            if nome:
                valor: list = tree.xpath(
                    "/html/body/div[1]/div/div/main/article/section/div[3]/div[1]/div/div[1]/div[2]/div[1]/div[3]/div[1]/div/h4/text()"
                )  # Localização do valor se tiver um aviso que tem desconto
                if not valor:
                    valor = tree.xpath(
                        "/html/body/div[1]/div/div/main/article/section/div[2]/div[1]/div/div[1]/div[2]/div[1]/div[2]/div[1]/div/h4/text()"
                    )  # Localização do valor se não tiver um aviso que tem desconto
                if valor:
                    self.__data["Nome"].append(nome[0])
                    self.__data["Valor"].append(valor[0])
                    self.__data["Link"].append(link)
