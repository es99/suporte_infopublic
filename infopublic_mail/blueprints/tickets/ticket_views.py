from flask import Blueprint, render_template
from infopublic_mail.blueprints.tickets.ticket_forms import TicketForm

ticket = Blueprint('ticket', __name__)

@ticket.route('/tickets')
def tickets():
    form = TicketForm()
    return render_template('tickets/tickets.html', form=form)

@ticket.route('/tickets/abertos')
def tickets_abertos():
    return render_template('tickets/abertos.html')

@ticket.route('/tickets/fechados')
def tickets_fechados():
    return render_template('tickets/fechados.html')