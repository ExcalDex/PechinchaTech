from Model.ManageProduto import *
from Bot import Bot
import json
import requests
from requests.adapters import HTTPAdapter


# def create_http_session():
#     adapter = HTTPAdapter()
#     session = requests.Session()
#     session.mount("http://", adapter)
#     session.mount("https://", adapter)
#     return session


if __name__ == "__main__":
    data = Bot.run()  # Dados puros dos produtos
    with open("teste.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(data))
    # p_list: list[Produto] = []
    # for i in range(len(data["Nome"])):
    #     p_list.append(
    #         Produto(
    #             data["Nome"][i],
    #             data["Tipo"][i],
    #             data["Valor"][i],
    #             data["Link"][i],
    #             data["Loja"][i],
    #             data["Imagem"][i],  # Só falta o bot do Mercado livre extrair as imagens também
    #         )
    #     )

    # p_list = [p for p in p_list if not p.get_nome().isspace()]

    # json_list = []
    # session = create_http_session()
    # try:
    #     for i, p in enumerate(p_list):
    #         json_obj = p.to_dict()
    #         if json_obj['idProdutoBase'] != -1:
    #             json_list.append(json_obj)
    #         if (i + 1) % 100 == 0 or i == len(p_list) - 1:
    #             try:
    #                 response = session.post(
    #                     "http://localhost:8087/api/produto/batch",
    #                     data=json.dumps(json_list),
    #                     headers={"Content-Type": "application/json"}
    #                 )
    #                 response.raise_for_status()
    #             except requests.exceptions.RequestException as e:
    #                 print(f"Request failed: {e}")
    #             json_list.clear()  # Libera memória RAM
    # finally:
    #     session.close()
