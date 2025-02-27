from Model.ManageProduto import *
from Bot import Bot
import json
import requests
from requests.adapters import HTTPAdapter
import time
from datetime import datetime
import subprocess


def create_http_session():
    adapter = HTTPAdapter()
    session = requests.Session()
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    return session

def run_script():
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
                
        #teste de notificação
        with open("teste.json", "w") as f:
            f.write(json.dumps(json_list))
        session.post(
            "http://localhost:8087/api/produto/batch",
            data=json.dumps(json_list),
            headers={"Content-Type": "application/json"},
        )
    finally:
        session.close()

def time_bf_next_execution():
    now = datetime.now()
    minutes_remaining = (10 - (now.minute % 10)) % 10
    seconds_remaining = (60 - now.second) % 60
    return (minutes_remaining * 60) + seconds_remaining
    
if __name__ == "__main__":
    subprocess.run(["python", "InserirProdutoBase.py"])
    v_request = create_http_session()
    while  True: #v_request.get("http://localhost:8087/api/produto/").status_code == 200:
        run_script()
        time.sleep(time_bf_next_execution())
