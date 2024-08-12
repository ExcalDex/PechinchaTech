import Bot.Mercado_Livre
import json

def run() -> dict:
    bot = Bot.Kabum_Galery.Scraper("placa de video")
    data = bot.get_produtos()
    with open("gpu_kabum_galery.json", "w") as json_file:
        json.dump(data, json_file, indent=4)
    return data
