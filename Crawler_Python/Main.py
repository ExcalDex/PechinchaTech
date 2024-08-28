from Model.ManageProduto import *
from Bot import Bot
import json


if __name__ == "__main__":
    data = Bot.run()  # Dados puros dos produto
    with open("teste.json", 'w', encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    # p_list: list[Produto] = []  # Lista de produtos (classe)
    # for i in range(len(data["Nome"])):
    #     p_list.append(
    #         Produto(
    #             data["Nome"][i],
    #             Tipo_Produto.GPU,
    #             float(data["Valor"][i][3:].replace(".", "").replace(",", ".")),
    #             data["Link"][i],
    #             Lojas.KABUM,
    #         )
    #     )
    # for i in range(len(p_list)):
    #     if p_list[i].get_nome().isspace():
    #         p_list.pop(i)
