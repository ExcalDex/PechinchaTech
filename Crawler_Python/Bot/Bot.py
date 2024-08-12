import Bot.Kabum
from Model.ManageProduto import Tipo_Produto


def run() -> dict:
    bot = Bot.Kabum.ScraperKabum(Tipo_Produto.GPU)
    data = bot.get_produtos()
    return data
