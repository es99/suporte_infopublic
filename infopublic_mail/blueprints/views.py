import os
from flask import render_template
import os
from flask import Blueprint
from infopublic_mail.extras import functions
from infopublic_mail.extensions.forms import BuscarForm


bp = Blueprint("blueprints", __name__)

@bp.route('/')
def index():
    path = os.getcwd()
    form = BuscarForm()
    return render_template('index.html', form=form, path=path)

@bp.route('/user/<int:id>')
def user(id):
    cursor = functions.connect('infopublic.db')
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