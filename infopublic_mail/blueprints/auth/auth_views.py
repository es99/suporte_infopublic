from flask import Blueprint, render_template
from infopublic_mail.blueprints.auth.forms import LoginForm

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    form = LoginForm()
    return render_template('auth/login.html', form=form)