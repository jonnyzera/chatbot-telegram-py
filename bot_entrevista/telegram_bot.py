# telegram_bot.py
import telepot
from telepot.loop import MessageLoop
from config import TELEGRAM_TOKEN, PERGUNTAS
from sheet_writer import salvar_resposta

estado_usuarios = {}  # chat_id: índice_pergunta

bot = telepot.Bot(TELEGRAM_TOKEN)

def handle(msg):
    chat_id = msg['chat']['id']
    texto = msg.get('text', '')

    if texto.lower() == '/start':
        estado_usuarios[chat_id] = 0
        bot.sendMessage(chat_id, "👋 Olá! Vamos começar sua entrevista. Responda a pergunta abaixo:")
        bot.sendMessage(chat_id, PERGUNTAS[0])
    else:
        indice = estado_usuarios.get(chat_id, 0)
        if indice < len(PERGUNTAS):
            salvar_resposta(str(chat_id), PERGUNTAS[indice], texto)
            estado_usuarios[chat_id] += 1
            if estado_usuarios[chat_id] < len(PERGUNTAS):
                bot.sendMessage(chat_id, PERGUNTAS[estado_usuarios[chat_id]])
            else:
                bot.sendMessage(chat_id, "✅ Entrevista finalizada. Obrigado!")
        else:
            bot.sendMessage(chat_id, "🚨 Você já respondeu todas as perguntas. Envie /start para recomeçar.")

def iniciar_bot_telegram():
    MessageLoop(bot, handle).run_as_thread()
    print("🤖 Bot do Telegram ativo...")
