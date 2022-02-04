import re
from flask import Blueprint, render_template
from flask_login import login_required
from infopublic_mail.extras import functions

servidor = Blueprint('servidor', __name__)
database_name = 'infopublic.db'

@servidor.route('/srv01', methods=['GET', 'POST'])
@login_required
def srv01():
    cursor, _ = functions.connect(database_name)
    records = functions.sistemas_por_servidor(cursor, 3)
    return render_template('servidores/srv01.html', records=records)

@servidor.route('/srv01/<int:sistema>', methods=['GET', 'POST'])
@login_required
def srv01_sistema(sistema):
    cursor, _  = functions.connect(database_name)
    records = functions.gera_relatorio_sistema(cursor, 3, sistema)
    return render_template('servidores/srv01_sistema.html', records=records)

@servidor.route('/srv02', methods=['GET', 'POST'])
@login_required
def srv02():
    cursor, _ = functions.connect(database_name)
    records = functions.sistemas_por_servidor(cursor, 2)
    return render_template('servidores/srv02.html', records=records)

@servidor.route('/rd_server', methods=['GET', 'POST'])
@login_required
def rd_server():
    cursor, _ = functions.connect(database_name)
    records = functions.sistemas_por_servidor(cursor, 1)
    return render_template('servidores/rd_server.html', records=records)

@servidor.route('/entidades_local', methods=['GET', 'POST'])
@login_required
def local():
    cursor, _ = functions.connect(database_name)
    records = functions.sistemas_por_servidor(cursor, 5)
    return render_template('servidores/local.html', records=records)