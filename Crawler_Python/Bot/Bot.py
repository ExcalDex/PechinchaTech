import Bot.Kabum
import json


def run() -> dict:
    bot = Bot.Kabum.ScraperKabum("placa de video")
    data = bot.get_produtos()
    return data
