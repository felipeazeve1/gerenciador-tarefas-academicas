from arquivos import salvar_tarefas

def adicionar_tarefas(lista_de_tarefas):
    print("\n--- Cadastrando Nova Tarefa ---")

    titulo = input("Título da tarefa (ex: Prova de Cálculo)")
    materia = input("Matéria (ex: ED)")
    prazo = input("Prazo de entrega (ex: 21/05/2026)")

    nova_tarefa = {
        "titulo": titulo,
        "materia": materia,
        "prazo": prazo,
        "concluida": False
    }

    lista_de_tarefas.append(nova_tarefa)
    salvar_tarefas(lista_de_tarefas)
    print("\n🎉 Tarefa adicionada com sucesso!")


def listar_tarefas(lista_de_tarefas):
    print("\n--- SUAS TAREFAS AGENDADAS ---")

    if len(lista_de_tarefas) == 0:
        print("Você não tem nenhuma tarefa cadastrada ainda! Use a opção 1.")

    else:
        for posicao, tarefa in enumerate(lista_de_tarefas):
            print(f"\n🔢 [Tarefa {posicao + 1}]") 
            print(f"   📌 Título: {tarefa['titulo']}")
            print(f"   📚 Matéria: {tarefa['materia']}")
            print(f"   📅 Prazo: {tarefa['prazo']}")

            if tarefa['concluida']:
                print(f"    Status: Concluída ✅")
            else:
                print(f"    Status: Pendente ❌")
            print("-" * 30)
    

def concluir_tarefa(lista_de_tarefas):
    listar_tarefas(lista_de_tarefas)

    if len(lista_de_tarefas) == 0:
        return
    
    try:
        escolha = int(input("\nDigite o número da tarefa que deseja concluir:"))

        indice = escolha - 1

        if 0 <= indice < len(lista_de_tarefas):
            lista_de_tarefas[indice]['concluida'] = True

            salvar_tarefas(lista_de_tarefas)
            print(f"\n🎉 Maravilha! A tarefa '{lista_de_tarefas[indice]['titulo']}' foi concluída!")
        else:
            print("\n⚠️ Esse número de tarefa não existe na listagem!")
    
    except ValueError:
        print("\n⚠️ Entrada inválida! Por favor, digite um número inteiro.")


def deletar_tarefa(lista_de_tarefas):
    listar_tarefas(lista_de_tarefas)
    
    if len(lista_de_tarefas) == 0:
        return 
        
    try:
        escolha = int(input("\nDigite o número da tarefa que deseja EXCLUIR: "))
        indice = escolha - 1
        
        if 0 <= indice < len(lista_de_tarefas):
            titulo_deletado = lista_de_tarefas[indice]['titulo']
            
            lista_de_tarefas.pop(indice)
            
            salvar_tarefas(lista_de_tarefas)
            print(f"\n🗑️ A tarefa '{titulo_deletado}' foi removida com sucesso!")
        else:
            print("\n⚠️ Esse número de tarefa não existe na listagem!")
            
    except ValueError:
        print("\n⚠️ Entrada inválida! Por favor, digite um número inteiro.")


def buscar_tarefa_por_texto(lista_de_tarefas):
    print("\n--- BUSCAR TAREFA ---")
    termo_busca = input("Digite o título ou parte dele para buscar: ").lower()

    encontrou = False
    print("\n--- RESULTADOS DA BUSCA ---")

    for posicao, tarefa in enumerate(lista_de_tarefas):
        if termo_busca in tarefa["titulo"].lower():
            encontrou = True
            print(f"\n🔢 [Tarefa {posicao + 1}]")
            print(f"   📌 Título: {tarefa['titulo']}")
            print(f"   📚 Matéria: {tarefa['materia']}")
            print(f"   Status: {'✅ Concluída' if tarefa['concluida'] else '❌ Pendente'}")
            print("-" * 30)
        
        if not encontrou:
            print("❌ Nenhum tarefa encontrada com esse termo.")


def filtrar_tarefas_pendentes(lista_de_tarefas):
    print("\n--- TAREFAS PENDENTES ❌ ---")
    encontrou = False

    for posicao, tarefa in enumerate(lista_de_tarefas):
        if not tarefa["concluida"]:
            encontrou = True
            print(f"\n🔢 [Tarefa {posicao + 1}]")
            print(f"   📌 Título: {tarefa['titulo']}")
            print(f"   📚 Matéria: {tarefa['materia']}")
            print(f"   📅 Prazo: {tarefa['prazo']}")
            print("-" * 30)

        if not encontrou:
            print("🎉 Nenhuma tarefa pendente! Você está em dia.")