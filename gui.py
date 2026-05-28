import tkinter as tk
from tkinter import messagebox
from arquivos import carregar_tarefas, salvar_tarefas

def criar_janela():
    janela = tk.Tk()
    janela.title("Gerenciador de Tarefas Acadêmicas")
    janela.geometry("500x650") 
    
    dados_tarefas = carregar_tarefas()
    
    lbl_titulo = tk.Label(janela, text="Título da Tarefa:", font=("Arial", 10, "bold"))
    lbl_titulo.pack(pady=(10, 0))
    ent_titulo = tk.Entry(janela, width=40)
    ent_titulo.pack(pady=5)
    
    lbl_materia = tk.Label(janela, text="Matéria:", font=("Arial", 10, "bold"))
    lbl_materia.pack()
    ent_materia = tk.Entry(janela, width=40)
    ent_materia.pack(pady=5)
    
    lbl_prazo = tk.Label(janela, text="Prazo de Entrega:", font=("Arial", 10, "bold"))
    lbl_prazo.pack()
    ent_prazo = tk.Entry(janela, width=40)
    ent_prazo.pack(pady=5)
    
    #FUNÇÃO: ATUALIZAR LISTA VISUAL 
    def atualizar_lista_visual():
        lista_visual.delete(0, tk.END)
        for tarefa in dados_tarefas:
            status = "✅" if tarefa["concluida"] else "❌"
            texto_linha = f"{status} {tarefa['titulo']} ({tarefa['materia']}) - Prazo: {tarefa['prazo']}"
            lista_visual.insert(tk.END, texto_linha)

    #LÓGICA DO BOTÃO ADICIONAR 
    def acao_adicionar():
        t = ent_titulo.get()
        m = ent_materia.get()
        p = ent_prazo.get()
        
        if t == "" or m == "" or p == "":
            messagebox.showwarning("⚠️ Atenção", "Por favor, preencha todos os campos!")
            return
            
        nova_tarefa = {
            "titulo": t,
            "materia": m,
            "prazo": p,
            "concluida": False
        }
        
        dados_tarefas.append(nova_tarefa)
        salvar_tarefas(dados_tarefas)
        atualizar_lista_visual()
        
        messagebox.showinfo("🎉 Sucesso", f"Tarefa '{t}' adicionada com sucesso!")
        ent_titulo.delete(0, tk.END)
        ent_materia.delete(0, tk.END)
        ent_prazo.delete(0, tk.END)

    #BOTÃO ADICIONAR 
    btn_adicionar = tk.Button(janela, text="Adicionar Tarefa", bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), command=acao_adicionar)
    btn_adicionar.pack(pady=15)

    #LISTA VISUAL NO APP 
    lbl_suas_tarefas = tk.Label(janela, text="Suas Tarefas (Clique para selecionar):", font=("Arial", 10, "bold"))
    lbl_suas_tarefas.pack(pady=(10, 0))

    lista_visual = tk.Listbox(janela, width=55, height=10, font=("Arial", 10))
    lista_visual.pack(pady=5)

    
    def acao_concluir():
        try:
            # lista_visual.curselection() devolve o índice da linha que o usuário clicou
            indice_selecionado = lista_visual.curselection()[0]
            
            dados_tarefas[indice_selecionado]["concluida"] = True
            
            salvar_tarefas(dados_tarefas)
            atualizar_lista_visual()

        except IndexError:
            # Se o usuário clicar no botão sem ter selecionado nada na lista, dá IndexError
            messagebox.showwarning("⚠️ Erro", "Por favor, selecione uma tarefa da lista primeiro!")

    def acao_excluir():
        try:
            indice_selecionado = lista_visual.curselection()[0]
            
            #Remoção da lista usando o pop()
            dados_tarefas.pop(indice_selecionado)
            
            salvar_tarefas(dados_tarefas)
            atualizar_lista_visual()
            messagebox.showinfo("🗑️ Removida", "Tarefa excluída com sucesso!")

        except IndexError:
            messagebox.showwarning("⚠️ Erro", "Por favor, selecione uma tarefa da lista primeiro!")

    # Criação do 'Frame' (uma caixinha invisível) para colocar os dois botões lado a lado
    frame_botoes = tk.Frame(janela)
    frame_botoes.pack(pady=10)

    btn_concluir = tk.Button(frame_botoes, text="Concluir Tarefa", bg="#2196F3", fg="white", font=("Arial", 10, "bold"), command=acao_concluir)
    btn_concluir.pack(side=tk.LEFT, padx=10) # side=tk.LEFT alinha à esquerda dentro do frame

    btn_excluir = tk.Button(frame_botoes, text="Excluir Tarefa", bg="#F44336", fg="white", font=("Arial", 10, "bold"), command=acao_excluir)
    btn_excluir.pack(side=tk.LEFT, padx=10)

    atualizar_lista_visual()

    janela.mainloop()

if __name__ == "__main__":
    criar_janela()