from arquivos import carregar_tarefas, salvar_tarefas
from operacoes import adicionar_tarefas, listar_tarefas, concluir_tarefa, deletar_tarefa, buscar_tarefa_por_texto, filtrar_tarefas_pendentes
from banco import criar_tabela


def main():
    criar_tabela()

    print("=== GERENCIADOR DE TAREFAS ACADÊMICAS ===\n")

    lista_de_tarefas = carregar_tarefas()

    while True:
        print("\n=== MENU DO GERENCIADOR ===")
        print("1. Adicionar Nova Tarefa")
        print("2. Listar Minhas Tarefas")
        print("3. Marcar Tarefa como Concluída")
        print("4. Excluir Tarefa")
        print("5. Buscar Tarefa por Título")
        print("6. Filtrar Apenas Pendentes")
        print("7. Sair do Programa")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_tarefas(lista_de_tarefas)

        elif opcao == "2":
            listar_tarefas(lista_de_tarefas)

        elif opcao == "3":
            concluir_tarefa(lista_de_tarefas)

        elif opcao == "4":
            deletar_tarefa(lista_de_tarefas)

        elif opcao == "5":
            buscar_tarefa_por_texto(lista_de_tarefas)
        
        elif opcao == "6":
            filtrar_tarefas_pendentes(lista_de_tarefas)

        elif opcao == "7":
            print("Até logo!")
            break

        else:
            print("\n⚠️ Opção inválida!")

    
    

if __name__ == "__main__":
    main()