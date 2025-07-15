from email_bot import enviar_perguntas_por_email
from telegram_bot import iniciar_bot_telegram
from utils import validar_email

def menu():
    print("""
💼 Bot de Entrevistas Automáticas

1 - Enviar perguntas por e-mail
2 - Ativar bot do Telegram
0 - Sair
""")
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        email = input("Digite o e-mail do candidato: ")
        if validar_email(email):
            enviar_perguntas_por_email(email)
        else:
            print("❌ E-mail inválido.")
    elif escolha == "2":
        iniciar_bot_telegram()
        input("Pressione Enter para encerrar o bot...")
    elif escolha == "0":
        print("Encerrando...")
    else:
        print("❌ Opção inválida.")

if __name__ == "__main__":
    menu()
