# email_bot.py
import smtplib
from email.mime.text import MIMEText
from config import EMAIL, EMAIL_PASSWORD, SMTP_SERVER, SMTP_PORT, PERGUNTAS

def enviar_perguntas_por_email(destinatario):
    corpo = "\n\n".join(PERGUNTAS)
    msg = MIMEText(corpo)
    msg["Subject"] = "Entrevista Automática - Responda por gentileza"
    msg["From"] = EMAIL
    msg["To"] = destinatario

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as servidor:
            servidor.starttls()
            servidor.login(EMAIL, EMAIL_PASSWORD)
            servidor.send_message(msg)
        print(f"✔️ E-mail enviado para {destinatario}")
    except Exception as e:
        print(f"❌ Erro ao enviar e-mail: {e}")
