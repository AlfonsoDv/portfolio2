import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv
from flask import (
    Blueprint, g, render_template, request, url_for, redirect, flash
)

bp = Blueprint('portfolio', __name__, url_prefix='/')

# Cargar variables de entorno
load_dotenv()

# Configuración
SMTP_CONFIG = {
    "server": "smtp.ionos.es",
    "port": 587,
    "sender_email": os.getenv("EMAIL_USER"),
    "password": os.getenv("EMAIL_PASSWORD")
}

@bp.route('/', methods = ['GET'])
def index():
    return render_template('portfolio/index.html')

@bp.route('/mail', methods = ['GET','POST'])
def mail():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    if request.method == 'POST':
        send_email(name,email,message)
        return render_template('portfolio/sent_mail.html')
    
    return redirect(url_for('portfolio.index'))


def send_email(name, email, message):
    subject = f"Nuevo mensaje de {name} <{email}>"
    body = f"Nombre: {name}\nEmail: {email}\n\nMensaje:\n{message}"

    msg = MIMEMultipart()
    msg['From'] = SMTP_CONFIG["sender_email"]  # Tu correo
    msg['To'] = SMTP_CONFIG["sender_email"]  # Enviar a ti mismo
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP(SMTP_CONFIG["server"], SMTP_CONFIG["port"]) as server:
            server.starttls()
            server.login(SMTP_CONFIG["sender_email"], SMTP_CONFIG["password"])
            server.send_message(msg)
        print("Correo enviado con éxito")
        return True
    except Exception as e:
        print(f"Error al enviar el correo: {e}")
        return False