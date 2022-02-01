import os
from flask import Blueprint, redirect, url_for, render_template, flash
from infopublic_mail.extensions import login
from infopublic_mail.extras import functions
from infopublic_mail.extensions.forms import BuscarForm, Cadastro, EnviaButton, Cadastro_user_entidade
from infopublic_mail.extensions.email import send_email
from infopublic_mail.extensions.db import Enviados, db, Ticket
from datetime import datetime
from flask_login import login_required


bp = Blueprint("blueprints", __name__)
database_name = 'infopublic.db'


@bp.route('/cadastro', methods=['GET', 'POST'])
@login_required
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
        cadastrado = form.cadastrado.data
        d = datetime.now()
        data = d.strftime("%d-%m-%Y - %H:%M")
        dados = dict(cpf=cpf, nome=nome, tel=tel, rg=rg, 
                    email=email, senha=senha, ativo=ativo, adm=adm, data=data,
                                                        cadastrado=cadastrado)
        cursor, conn = functions.connect(database_name)
        
        if functions.insere_usuario(cursor, conn, **dados):
            flash("Usuário cadastrado com sucesso!")
        else:
            flash("Erro ao cadastrar usuário")
    
        return redirect(url_for('blueprints.cadastro'))
        
    return render_template('cadastro.html', form=form, dados=dados)

@bp.route('/', methods=['GET', 'POST'])
@login_required
def index():
    form = BuscarForm()
    tickets = Ticket.query.all()
    num_abertos = []
    num_fechados = []
    for ticket in tickets:
        if ticket.fechado:
            num_fechados.append(ticket)
        else:
            num_abertos.append(ticket)
    if form.validate_on_submit():
        cpf = form.cpf.data
        cursor, _ = functions.connect(database_name)
        user_id = functions.cpf_retornaId(cursor, cpf)
        if user_id != None:
            return redirect(url_for('blueprints.user', id=user_id[0]))
        else:
            return render_template('404.html'), 404 
    return render_template('index.html', form=form, current_time=datetime.utcnow(),
                            num_abertos=len(num_abertos), num_fechados=len(num_fechados))

@bp.route('/user/<int:id>', methods=['GET', 'POST'])
@login_required
def user(id):
    form = EnviaButton()
    form2 = Cadastro_user_entidade()
    cursor, conn = functions.connect(database_name)
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

    if form2.validate_on_submit():
        entidade = form2.entidade.data
        senha_sistema = form2.senha_sistema.data
        dados = dict(id_user=id, entidade=entidade, senha=senha_sistema)

        if functions.insere_entidade_usuario(cursor, conn, **dados):
            flash(f'Entidade cadastrada com sucesso para {nome}')
        else:
            flash('Erro ao cadastrar entidade.') 
        return redirect(url_for('blueprints.user', id=id))

    if form.validate_on_submit():
        if pode_enviar:
            cpf_tratado = functions.trata_cpf(cpf)
            send_email(email, nome, cpf_tratado, senha, senha_sistema)
            email_enviado = Enviados(cpf=cpf_tratado, email=email)
            db.session.add(email_enviado)
            db.session.commit()
            flash('Mensagem enviada para {}'.format(email))
        else:
            flash('O campo email do usuário está vazio!')
        return redirect(url_for('blueprints.user', id=id))


    return render_template('usuario.html', id=user_id, email=email, senha=senha, entidades=entidades,
                        senha_sistema=senha_sistema, nome=nome, cpf=cpf, telefone=telefone, form=form,
                        pode_enviar=pode_enviar, form2=form2)