from banco import criar_tabela, inserir_tarefa, listar_tarefas, marcar_como_concluida, deletar_tarefa

def main():
    criar_tabela()

    print("=== GERENCIADOR DE TAREFAS ACADÊMICAS (TERMINAL) ===\n")

    while True:
        print("\n=== MENU DO GERENCIADOR ===")
        print("1. Adicionar Nova Tarefa")
        print("2. Listar Minhas Tarefas")
        print("3. Marcar Tarefa como Concluída")
        print("4. Excluir Tarefa")
        print("5. Sair do Programa")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            t = input("Título da tarefa: ")
            m = input("Matéria: ")
            p = input("Prazo (dd/mm/aaaa): ")
            if t and m and p:
                inserir_tarefa(t, m, p)
                print("🎉 Tarefa adicionada com sucesso no Banco de Dados!")
            else:
                print("⚠️ Todos os campos são obrigatórios!")

        elif opcao == "2":
            tarefas = listar_tarefas()
            if not tarefas:
                print("\n📭 Nenhuma tarefa cadastrada.")
            else:
                print("\n📋 SUAS TAREFAS NO BANCO:")
                for t in tarefas:
                    status = "✅" if t[4] == 1 else "❌"
                    print(f"ID: {t[0]} | {status} {t[1]} ({t[2]}) - Prazo: {t[3]}")

        elif opcao == "3":
            id_tarefa = input("Digite o ID da tarefa que deseja concluir: ")
            if id_tarefa.isdigit():
                marcar_como_concluida(int(id_tarefa))
                print(f"✅ Tarefa ID {id_tarefa} atualizada para concluída!")
            else:
                print("⚠️ ID inválido!")

        elif opcao == "4":
            id_tarefa = input("Digite o ID da tarefa que deseja excluir: ")
            if id_tarefa.isdigit():
                deletar_tarefa(int(id_tarefa))
                print(f"🗑️ Tarefa ID {id_tarefa} removida do banco!")
            else:
                print("⚠️ ID inválido!")

        elif opcao == "5":
            print("Até logo!")
            break

        else:
            print("\n⚠️ Opção inválida!")


if __name__ == "__main__":
    main()