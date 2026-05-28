import sqlite3

def conectar_banco():
    #Conecta ao arquivo do banco (se não existir, ele cria o arquivo automaticamente)
    conexao = sqlite3.connect("sistema_tarefas.db")
    return conexao


def criar_tabela():
    conexao = conectar_banco()
    cursor = conexao.cursor() 
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tarefas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        materia TEXT NOT NULL,
        prazo TEXT NOT NULL,
        concluida INTEGER DEFAULT 0
    );
    """)
    
    conexao.commit() 
    conexao.close()  


def inserir_tarefa(titulo, materia, prazo):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    cursor.execute("""
    INSERT INTO tarefas (titulo, materia, prazo)
    VALUES (?, ?, ?);
    """, (titulo, materia, prazo))
    
    conexao.commit()
    conexao.close()


def listar_tarefas():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    cursor.execute("SELECT id, titulo, materia, prazo, concluida FROM tarefas;")
    linhas = cursor.fetchall() 
    
    conexao.close()
    return linhas 


def marcar_como_concluida(id_tarefa):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    cursor.execute("UPDATE tarefas SET concluida = 1 WHERE id = ?;", (id_tarefa,))
    
    conexao.commit()
    conexao.close()


def deletar_tarefa(id_tarefa):
    conexao = conectar_banco()
    cursor = cursor = conexao.cursor()
    
    cursor.execute("DELETE FROM tarefas WHERE id = ?;", (id_tarefa,))
    
    conexao.commit()
    conexao.close()