import tkinter as tk
import customtkinter as ctk 
from tkinter import messagebox
from arquivos import carregar_tarefas, salvar_tarefas
from api import enviar_lembrete_telegram

# Configuração global do tema:
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

def criar_janela():
    janela = ctk.CTk()
    janela.title("Gerenciador de Tarefas Acadêmicas")
    janela.geometry("550x650")
    
    dados_tarefas = carregar_tarefas()
    
    #CAMPOS DE ENTRADA 
    lbl_titulo = ctk.CTkLabel(janela, text="Título da Tarefa:", font=("Arial", 12, "bold"))
    lbl_titulo.pack(pady=(15, 0))
    ent_titulo = ctk.CTkEntry(janela, width=350, placeholder_text="Ex: Estudar para a prova")
    ent_titulo.pack(pady=5)
    
    lbl_materia = ctk.CTkLabel(janela, text="Matéria:", font=("Arial", 12, "bold"))
    lbl_materia.pack()
    ent_materia = ctk.CTkEntry(janela, width=350, placeholder_text="Ex: Estrutura de Dados")
    ent_materia.pack(pady=5)
    
    lbl_prazo = ctk.CTkLabel(janela, text="Prazo de Entrega:", font=("Arial", 12, "bold"))
    lbl_prazo.pack()
    ent_prazo = ctk.CTkEntry(janela, width=350, placeholder_text="Ex: 30/05/2026")
    ent_prazo.pack(pady=5)
    
    def atualizar_lista_visual():
        lista_visual.delete(0, tk.END)
        for tarefa in dados_tarefas:
            status = "✅" if tarefa["concluida"] else "❌"
            texto_linha = f" {status}  {tarefa['titulo']} ({tarefa['materia']}) - Prazo: {tarefa['prazo']}"
            lista_visual.insert(tk.END, texto_linha)

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
        enviar_lembrete_telegram(t, p)
        
        atualizar_lista_visual()
        
        messagebox.showinfo("🎉 Sucesso", f"Tarefa '{t}' adicionada com sucesso!")
        ent_titulo.delete(0, ctk.END)
        ent_materia.delete(0, ctk.END)
        ent_prazo.delete(0, ctk.END)

    btn_adicionar = ctk.CTkButton(janela, text="Adicionar Tarefa", font=("Arial", 12, "bold"), command=acao_adicionar)
    btn_adicionar.pack(pady=20)

    lbl_suas_tarefas = ctk.CTkLabel(janela, text="Suas Tarefas (Clique para selecionar):", font=("Arial", 12, "bold"))
    lbl_suas_tarefas.pack(pady=(10, 0))

    lista_visual = tk.Listbox(janela, width=60, height=10, font=("Arial", 11), bg="#2a2a2a", fg="white", bd=0, highlightthickness=1, highlightbackground="#4a4a4a")
    lista_visual.pack(pady=10)

    def acao_concluir():
        try:
            indice_selecionado = lista_visual.curselection()[0]
            dados_tarefas[indice_selecionado]["concluida"] = True
            salvar_tarefas(dados_tarefas)
            atualizar_lista_visual()
        except IndexError:
            messagebox.showwarning("⚠️ Erro", "Por favor, selecione uma tarefa da lista primeiro!")

    def acao_excluir():
        try:
            indice_selecionado = lista_visual.curselection()[0]
            dados_tarefas.pop(indice_selecionado)
            salvar_tarefas(dados_tarefas)
            atualizar_lista_visual()
            messagebox.showinfo("🗑️ Removida", "Tarefa excluída com sucesso!")
        except IndexError:
            messagebox.showwarning("⚠️ Erro", "Por favor, selecione uma tarefa da lista primeiro!")

    frame_botoes = ctk.CTkFrame(janela, fg_color="transparent") 
    frame_botoes.pack(pady=15)

    btn_concluir = ctk.CTkButton(frame_botoes, text="Concluir Tarefa", fg_color="#2196F3", hover_color="#1976D2", font=("Arial", 12, "bold"), command=acao_concluir)
    btn_concluir.pack(side=tk.LEFT, padx=15)

    btn_excluir = ctk.CTkButton(frame_botoes, text="Excluir Tarefa", fg_color="#F44336", hover_color="#D32F2F", font=("Arial", 12, "bold"), command=acao_excluir)
    btn_excluir.pack(side=tk.LEFT, padx=15)

    atualizar_lista_visual()

    janela.mainloop()

if __name__ == "__main__":
    criar_janela()