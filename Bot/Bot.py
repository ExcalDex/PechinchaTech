import Bot.Kabum
import Bot.Mercado_Livre
import json


def run() -> dict:
    bot = Bot.Kabum.Scraper("placa de video")
    data = bot.get_produtos()
    return data
