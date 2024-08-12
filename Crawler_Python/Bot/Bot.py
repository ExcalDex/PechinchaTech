import Bot.Kabum
from Model.ManageProduto import Tipo_Produto


def run() -> dict:
    bot = Bot.Kabum.Scraper(Tipo_Produto.GPU)
    data = bot.get_produtos()
    return data
