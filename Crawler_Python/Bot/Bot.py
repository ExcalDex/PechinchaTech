import Bot.Kabum
import Bot.Mercado_Livre
import json


def run() -> dict:
    bot = Bot.Kabum.ScraperKabum("placa de video")
    data = bot.get_produtos()
    return data
