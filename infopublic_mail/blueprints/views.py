import os
from flask import Blueprint, redirect, url_for, render_template
from infopublic_mail.extras import functions
from infopublic_mail.extensions.forms import BuscarForm


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

@bp.route('/user/<int:id>')
def user(id):
    cursor = functions.connect(database_name)
    usuario = functions.consulta_id(cursor, id)

    telefone = None
    email = None
    senha_sistema = None

    if usuario['telefone']:
        telefone = usuario['telefone']
    if usuario['email']:
        email = usuario['email']
    if usuario['senha_sistema']:
        senha_sistema = usuario['senha_sistema'][0] 

    cpf = usuario['cpf']
    user_id = usuario['id']
    nome = usuario['nome']
    senha = usuario['senha']
    entidades = usuario['entidades']

    return render_template('usuario.html', id=user_id, email=email, senha=senha, entidades=entidades,
                        senha_sistema=senha_sistema, nome=nome, cpf=cpf, telefone=telefone)