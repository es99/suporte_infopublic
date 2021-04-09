from flask_mail import Mail, Message
from flask import render_template
from infopublic_mail.extras import  msg_text_plain

mail = Mail()

def init_app(app):
    mail.init_app(app)

def send_email(to, nome, cpf, senha, senha_sistema):
    subject = '[Suporte Infopublic] - Dados de Acesso'
    sender = 'Suporte <suporte@infopublic.com.br>'

    msg = Message(subject, sender=sender, recipients=[to])
    msg.body = msg_text_plain.mensagem(nome, cpf, senha, senha_sistema)
    msg.html = render_template('template_envio_email.html', nome=nome, cpf=cpf,
                                senha=senha, senha_sistema=senha_sistema)
    mail.send(msg)