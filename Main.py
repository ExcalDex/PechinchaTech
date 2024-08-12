from Model.ManageProduto import *
from Bot import Bot
import time

if __name__ == "__main__":
    start_time = time.time()
    data = Bot.run()
    end_time = time.time()
    print(f"Tempo de execução: {(end_time - start_time):.2f} segundos")
    p_list: list[Produto] = []
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
    print("Em uma busca por " + str(len(p_list)) + " produtos")