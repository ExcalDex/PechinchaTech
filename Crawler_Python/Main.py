from Model.ManageProduto import *
from Bot import Bot
import json
import requests
from requests.adapters import HTTPAdapter


def create_http_session():
    adapter = HTTPAdapter()
    session = requests.Session()
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    return session


if __name__ == "__main__":
    data = Bot.run()  # Dados puros dos produtos
    #with open("teste.json", "w", encoding="utf-8") as f:
    #    f.write(json.dumps(data))
    p_list: list[Produto] = []
    for i in range(len(data["Nome"])):
        p_list.append(
            Produto(
                data["Nome"][i],
                data["Tipo"][i],
                float(data["Valor"][i]),
                data["Link"][i],
                data["Loja"][i],
                data["Imagem"][i],
            )
        )

    p_list = [p for p in p_list if not p.get_nome() == ""]

    json_list = []
    session = create_http_session()
    try:
        for p in p_list:
            json_obj = p.to_dict()
            if json_obj["id_produto_base"] != -1:
                json_list.append(json_obj)
        session.post(
            "http://localhost:8087/api/produto/batch",
            data=json.dumps(json_list),
            headers={"Content-Type": "application/json"},
        )
    finally:
        session.close()
