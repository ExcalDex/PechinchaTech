from Model.ManageProduto import *
from Bot import Bot
import time


if __name__ == "__main__":
    start = time.time()
    data = Bot.run() # Dados puros dos produto
    print(time.time() - start)
    p_list: list[Produto] = [] # Lista de produtos (classe)
    for i in range(len(data["Nome"])):
        p_list.append(
            Produto(
                data["Nome"][i],
                Tipo_Produto.GPU,
                float(data["Valor"][i][3:].replace(".", "").replace(",", ".")),
                data["Link"][i],
                Lojas.KABUM,
            )
        )
    for i in range(len(p_list)):
        if p_list[i].get_nome().isspace():
            p_list.pop(i)