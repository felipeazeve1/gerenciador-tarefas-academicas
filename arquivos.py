import json

def salvar_tarefas(lista_de_tarefas):
    with open("tarefas.json", "w", encoding = "utf-8") as arquivo:
        json.dump(lista_de_tarefas, arquivo, indent=4, ensure_ascii=False)


def carregar_tarefas():
    try:
        with open("tarefas.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []