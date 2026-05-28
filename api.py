import os
import requests
from dotenv import load_dotenv 

load_dotenv()


def enviar_lembrete_telegram(titulo_tarefa, prazo):
    TOKEN_BOT = os.getenv("TELEGRAM_TOKEN")
    SEU_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

    if not TOKEN_BOT or not SEU_CHAT_ID:
        print("⚠️ Chaves do Telegram não configuradas no arquivo .env")
        return False

    mensagem = f"🔔 *LEMBRETE DE TAREFA* 🔔\n\nNão esqueça de entregar:\n\n📌 *{titulo_tarefa}*\n📅 Prazo: {prazo}\n\n"

    url_api = f"https://api.telegram.org/bot{TOKEN_BOT}/sendMessage"

    dados = {
        "chat_id": SEU_CHAT_ID,
        "text": mensagem,
        "parse_mode": "Markdown"  
    }

    try:
        resposta = requests.post(url_api, data=dados, timeout=10)
        return resposta.status_code == 200
    
    except Exception as e:
        print(f"Erro ao conectar com a API do Telegram: {e}")
        return False