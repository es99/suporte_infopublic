import re
from flask import Blueprint, render_template
from flask_login import login_required
from infopublic_mail.extras import functions

servidor = Blueprint('servidor', __name__)
database_name = 'infopublic.db'

@servidor.route('/srv01', methods=['GET', 'POST'])
@login_required
def srv01():
    return render_template('servidores/srv01.html')

@servidor.route('/srv02', methods=['GET', 'POST'])
@login_required
def srv02():
    return render_template('servidores/srv02.html')

@servidor.route('/rd_server', methods=['GET', 'POST'])
@login_required
def rd_server():
    return render_template('servidores/rd_server.html')

@servidor.route('/entidades_local', methods=['GET', 'POST'])
@login_required
def local():
    return render_template('servidores/local.html')