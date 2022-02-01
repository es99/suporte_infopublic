from flask import Blueprint, render_template, flash, redirect, url_for
from werkzeug.utils import redirect
from infopublic_mail.blueprints.tickets.ticket_forms import TicketForm
from flask_login import login_required, current_user
from infopublic_mail.extensions.db import Ticket, db, User
from datetime import date
import time

ticket = Blueprint('ticket', __name__)

@ticket.route('/tickets', methods=['GET', 'POST'])
@login_required
def tickets():
    form = TicketForm()
    if form.validate_on_submit():
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        ticket=Ticket(
            date=date.today(),
            cpf=current_user.cpf,
            hora=current_time,
            nome=current_user.nome,
            sistema=form.sistema.data,
            entidade=form.entidade.data,
            assunto=form.assunto.data,
            descricao=form.descricao.data,
            user=current_user
        )
        db.session.add(ticket)
        db.session.commit()
        flash('Ticket cadastrado com sucesso!')
        return redirect(url_for('ticket.tickets'))
    return render_template('tickets/tickets.html', form=form)

@ticket.route('/tickets/abertos')
@login_required
def tickets_abertos():
    user = User.query.filter_by(id=current_user.id).first()
    tickets = user.tickets.all()
    abertos = []
    for ticket in tickets:
        if ticket.fechado is False:
            abertos.append(ticket)
    numero = len(abertos)
    return render_template('tickets/abertos.html', numero=numero, tickets=abertos)

@ticket.route('/tickets/abertos/<int:id>')
def verifica_ticket_aberto(id):
    ticket = Ticket.query.filter_by(id=id).first()
    data = ticket.date
    hora = ticket.hora
    sistema = ticket.sistema
    entidade = ticket.entidade
    assunto = ticket.assunto
    descricao = ticket.descricao
    solucao = ticket.solucao
    nome = ticket.nome
    cpf = ticket.cpf
    return render_template('tickets/verifica_ticket.html', id=id, data=data,
                        hora=hora, sistema=sistema, entidade=entidade, assunto=assunto,
                        descricao=descricao, solucao=solucao, nome=nome, cpf=cpf)

@ticket.route('/tickets/fechados')
@login_required
def tickets_fechados():
    return render_template('tickets/fechados.html')