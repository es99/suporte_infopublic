import os
from flask import Blueprint, redirect, url_for, render_template, flash
from infopublic_mail.extras import functions, msg_text_plain
from infopublic_mail.extensions.forms import BuscarForm, EnviaButton
from infopublic_mail.extensions.email import send_email



bp = Blueprint("blueprints", __name__)
database_name = 'infopublic.db'

@bp.route('/', methods=['GET', 'POST'])
def index():
    form = BuscarForm()
    if form.validate_on_submit():
        cpf = form.cpf.data
        cursor = functions.connect(database_name)
        user_id = functions.cpf_retornaId(cursor, cpf)
        if user_id != None:
            return redirect(url_for('blueprints.user', id=user_id[0]))
        else:
            return render_template('404.html'), 404 
    return render_template('index.html', form=form)

@bp.route('/user/<int:id>', methods=['GET', 'POST'])
def user(id):
    form = EnviaButton()
    cursor = functions.connect(database_name)
    usuario = functions.consulta_id(cursor, id)

    telefone = None
    email = None
    senha_sistema = None
    pode_enviar = False

    if usuario['telefone']:
        telefone = usuario['telefone']
    if usuario['email']:
        email = usuario['email']
        pode_enviar = True
    if usuario['senha_sistema']:
        senha_sistema = usuario['senha_sistema'][0] 

    cpf = usuario['cpf']
    user_id = usuario['id']
    nome = usuario['nome']
    senha = usuario['senha']
    entidades = usuario['entidades']

    if form.validate_on_submit():
        if pode_enviar:
            cpf_tratado = functions.trata_cpf(cpf)
            send_email(email, nome, cpf_tratado, senha, senha_sistema)
            flash('Mensagem enviada para {}'.format(email))
        else:
            flash('O campo email do usuário está vazio!')
        return redirect(url_for('blueprints.user', id=id))


    return render_template('usuario.html', id=user_id, email=email, senha=senha, entidades=entidades,
                        senha_sistema=senha_sistema, nome=nome, cpf=cpf, telefone=telefone, form=form,
                        pode_enviar=pode_enviar)