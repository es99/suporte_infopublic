from flask import Blueprint, render_template, redirect, request, url_for, flash
from infopublic_mail.blueprints.auth.forms import LoginForm, RegistrationForm
from infopublic_mail.extensions.db import User, db
from flask_login import login_user, logout_user, login_required
from datetime import datetime

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(cpf=form.cpf.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('blueprints.index')
            return redirect(next)
        flash('Email ou senha inválidos!')
    return render_template('auth/login.html', form=form)

@auth.route('/register', methods=['GET', 'POST'])   
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    cpf=form.cpf.data,
                    nome=form.nome.data,
                    sobrenome=form.sobrenome.data,
                    telefone=form.celular.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Registro feito com sucesso, você poderá realizar login agora')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Você foi deslogado do sistema!')
    return redirect(url_for('blueprints.index'))