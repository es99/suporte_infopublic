from flask import Blueprint, render_template, redirect, request, url_for, flash
from infopublic_mail.blueprints.auth.forms import LoginForm
from infopublic_mail.extensions.db import User
from flask_login import login_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('blueprints.index')
            return redirect(next)
        flash('Email ou senha inválidos!')
    return render_template('auth/login.html', form=form)