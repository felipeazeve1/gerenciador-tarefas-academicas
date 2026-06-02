# 📌 Gerenciador de Tarefas Acadêmicas

Este projeto foi desenvolvido como um **laboratório de estudos pessoal** com o objetivo de aprofundar meus conhecimentos práticos em Python. A ideia principal foi sair dos scripts simples de terminal e entender como construir um ecossistema de software integrado, aplicando conceitos reais de banco de dados, comunicação com APIs externas, segurança e desenvolvimento de interfaces gráficas.

---

## 🎯 Objetivos do Estudo
O projeto foi estruturado para consolidar o aprendizado em quatro pilares do desenvolvimento de software:
* **Interface Gráfica (GUI):** Criação de uma experiência visual moderna e responsiva utilizando o `CustomTkinter` (com suporte a modo escuro).
* **Persistência de Dados (SQL):** Substituição de arquivos de texto locais (JSON) por um banco de dados relacional robusto (`SQLite3`), aprendendo na prática comandos como `CREATE TABLE`, `INSERT`, `SELECT`, `UPDATE` e `DELETE`.
* **Consumo de APIs Externas:** Integração com a API oficial do Telegram (via biblioteca `requests`) para disparar notificações e lembretes em tempo real diretamente para o celular do usuário.
* **Segurança e Boas Práticas:** Implementação de variáveis de ambiente usando um arquivo `.env` (através da `python-dotenv`) para macronizar e proteger tokens e credenciais privadas, simulando o padrão utilizado em ambientes de produção.

---

## 🏗️ Estrutura e Arquitetura do Projeto
O sistema foi modularizado para seguir boas práticas de organização de código, dividindo as responsabilidades de forma clara:
* `main.py`: Ponto de entrada do sistema e interface via linha de comando (Terminal).
* `gui.py`: Painel visual do aplicativo construído em CustomTkinter.
* `banco.py`: Camada de persistência isolada que gerencia todas as transações SQL com o arquivo `sistema_tarefas.db`.
* `api.py`: Módulo responsável pela comunicação HTTP e formatação das mensagens enviadas para a API do Telegram.
* `.env.example`: Modelo que orienta outros desenvolvedores a configurarem suas próprias chaves sem expor dados sensíveis no repositório.

---

## 🛠️ Tecnologias e Ferramentas Utilizadas
* **Python 3**
* **CustomTkinter** (Interface Visual)
* **SQLite3** (Banco de Dados Relacional Nativo)
* **Requests** (Protocolo HTTP para consumo de API)
* **Python-Dotenv** (Gerenciamento de Variáveis de Ambiente)
* **Git & GitHub** (Versionamento de Código)

---

## 🚀 Como Executar este Projeto Localmente

### 1. Clonar o Repositório e Entrar na Pasta
Use o comando 'git clone' seguido do link do seu repositório e depois 'cd gerenciador_tarefas' para entrar na pasta pelo terminal.

### 2. Configurar o Ambiente Virtual (Venv)
Crie a venv rodando 'python -m venv venv'. No Windows, ative usando o comando 'venv\Scripts\activate'. Depois, instale as dependências com 'pip install -r requirements.txt'.

### 3. Configurar as Variáveis de Ambiente
Duplique o arquivo `.env.example`, renomeie a cópia para `.env`, abra o arquivo e coloque suas chaves do Telegram (TELEGRAM_TOKEN e TELEGRAM_CHAT_ID) sem aspas.

### 4. Rodar a Aplicação
Você pode testar o sistema de duas formas:
* Para rodar o menu em modo texto no terminal: execute 'python main.py'
* Para rodar o aplicativo com a tela visual escura: execute 'python gui.py'