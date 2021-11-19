from flask import Blueprint, render_template, flash, redirect, url_for
from werkzeug.utils import redirect
from infopublic_mail.blueprints.tickets.ticket_forms import TicketForm
from flask_login import login_required, current_user
from infopublic_mail.extensions.db import Ticket, db
from datetime import date, time

ticket = Blueprint('ticket', __name__)

@ticket.route('/tickets', methods=['GET', 'POST'])
@login_required
def tickets():
    form = TicketForm()
    if form.validate_on_submit():
        ticket=Ticket(
            date=date.today(),
            cpf=current_user.cpf,
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
    return render_template('tickets/abertos.html')

@ticket.route('/tickets/fechados')
@login_required
def tickets_fechados():
    return render_template('tickets/fechados.html')