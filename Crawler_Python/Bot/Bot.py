import Bot.Kabum
import Bot.Mercado_Livre
from Model.ManageProduto import Tipo_Produto


def run() -> dict:
    data = {"Nome": [], "Valor": [], "Link": [], "Tipo": []}
    for tipo_produto in Tipo_Produto:
        data_k = Bot.Kabum.Scraper(tipo_produto).get_produtos()
        # data_ml = Bot.Mercado_Livre.Scraper(tipo_produto).get_produtos()

        for chave in data:
            data[chave] = data[chave] + data_k[chave] # + data_ml[chave]

    return data
