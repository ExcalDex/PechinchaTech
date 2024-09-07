import Bot.Kabum
import Bot.Mercado_Livre
from Model.ManageProduto import Tipo_Produto, Lojas


def run() -> dict:
    data = {"Nome": [], "Valor": [], "Link": [], "Tipo": [], "Loja": [], "Imagem": []}
    for tipo_produto in Tipo_Produto:
        data_k = Bot.Kabum.Scraper(tipo_produto).get_produtos()
        data_ml = Bot.Mercado_Livre.Scraper(tipo_produto).get_produtos()

        for chave in data:
            if chave == "Loja":
                data[chave] = data[chave] + [Lojas.KABUM for i in range(len(data_k["Nome"]))] + [Lojas.MERCADO_LIVRE for i in range(len(data_ml["Nome"]))]
            else:
                data[chave] = data[chave] + data_k[chave] + data_ml[chave]

    return data
