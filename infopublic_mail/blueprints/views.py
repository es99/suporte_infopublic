import os
from flask import Blueprint, redirect, url_for, render_template, flash
from infopublic_mail.extras import functions, msg_text_plain
from infopublic_mail.extensions.forms import BuscarForm, Cadastro, EnviaButton, Cadastro_user_entidade
from infopublic_mail.extensions.email import send_email
from datetime import datetime



bp = Blueprint("blueprints", __name__)
database_name = 'infopublic.db'

@bp.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    form = Cadastro()
    dados = None
    if form.validate_on_submit():
        cpf = form.cpf.data
        nome = form.nome.data
        tel = form.telefone.data
        rg = form.rg.data
        email = form.email.data
        senha= form.senha.data
        ativo = form.ativo.data
        adm = form.adm.data
        d = datetime.now()
        data = d.strftime("%d-%m-%Y - %H:%M")
        dados = dict(cpf=cpf, nome=nome, tel=tel, rg=rg, 
                    email=email, senha=senha, ativo=ativo, adm=adm, data=data)
        cursor, conn = functions.connect(database_name)

        if functions.insere_usuario(cursor, conn, **dados):
            flash("Usuário cadastrado com sucesso!")
        else:
            flash("Erro ao cadastrar usuário")

        return redirect(url_for('blueprints.cadastro'))
    return render_template('cadastro.html', form=form, dados=dados)

@bp.route('/sucesso/<user>', methods=['GET', 'POST'])
def sucesso(user, dados):
    return render_template('sucesso.html', user=user, dados=dados)

@bp.route('/', methods=['GET', 'POST'])
def index():
    form = BuscarForm()
    if form.validate_on_submit():
        cpf = form.cpf.data
        cursor, _ = functions.connect(database_name)
        user_id = functions.cpf_retornaId(cursor, cpf)
        if user_id != None:
            return redirect(url_for('blueprints.user', id=user_id[0]))
        else:
            return render_template('404.html'), 404 
    return render_template('index.html', form=form)

@bp.route('/user/<int:id>', methods=['GET', 'POST'])
def user(id):
    form = EnviaButton()
    form2 = Cadastro_user_entidade()
    cursor, _ = functions.connect(database_name)
    usuario = functions.consulta_id(cursor, id)

    telefone = None
    email = None
    pode_enviar = False
    senha_sistema = '--'

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
                        pode_enviar=pode_enviar, form2=form2)