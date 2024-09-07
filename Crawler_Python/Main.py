from Model.ManageProduto import *
from Bot import Bot
import json
import requests


if __name__ == "__main__":
    data = Bot.run()  # Dados puros dos produtos
    p_list: list[Produto] = []
    for i in range(len(data["Nome"])):
        p_list.append(
            Produto(
                data["Nome"][i],
                data["Tipo"][i],
                data["Valor"][i],
                data["Link"][i],
                data["Loja"][i],
                data[
                    "Imagem"
                ],  # Só falta o bot do Mercado livre extrair as imagens também
            )
        )
    for i in range(len(p_list)):
        if p_list[i].get_nome().isspace():
            p_list.pop(i)

    json_list = []
    i: int = 0
    for p in p_list:
        json_list.append((p.to_dict()))
        i += 1
        if i == 100: #Pode chegar a consumir 8 gigas de RAM. Por isso o limite.
            requests.post(
                "localhost:8087/api/produto/batch", data=json.dumps(json_list)
            )
            json_list.clear() #Libera memória RAM
