from flask_sqlalchemy import SQLAlchemy
from pytz import timezone
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from infopublic_mail.extensions.login import login_manager

db = SQLAlchemy()
fuso = timezone('America/Recife')

class Enviados(db.Model):
    __tablename__ = 'emails_enviados'
    id = db.Column(db.Integer, primary_key=True)
    data_envio = db.Column(db.DateTime, default=datetime.now().astimezone(fuso))
    cpf = db.Column(db.String(64), index=True, nullable=False)
    email = db.Column(db.String(120), index=True, nullable=False)

def init_app(app):
    db.init_app(app)

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role')

    def __repr__(self):
        return f'Role {self.name}'

class User(db.Model, UserMixin):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    cpf = db.Column(db.String(64), unique=True, index=True)
    nome = db.Column(db.String(64), unique=False, index=True)
    sobrenome = db.Column(db.String(64), unique=False, index=True)
    email = db.Column(db.String(64), unique=True, index=True)
    telefone = db.Column(db.String(64), unique=False, index=True)
    password_hash = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    tickets = db.relationship('Ticket', backref='user', lazy='dynamic')

    def __repr__(self):
        return f'User {self.username}, email: {self.email}'

    @property
    def password(self):
        raise AttributeError('a senha não é um atributo a ser lido')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Ticket(db.Model):
    __tablename__ = "tickets"
    id = db.Column(db.Integer, primary_key=True)
    fechado = db.Column(db.Boolean, default=False)
    andamento = db.Column(db.Boolean, default=False)
    date = db.Column(db.Date, index=True)
    hora = db.Column(db.String(20), nullable=True)
    intervalo = db.Column(db.Interval)
    cpf = db.Column(db.String(64), index=True, nullable=False)
    nome = db.Column(db.String(64), unique=False, index=True, nullable=False)
    sistema = db.Column(db.String(64), unique=False, index=True)
    entidade = db.Column(db.String(120))
    assunto = db.Column(db.String(120), unique=False, index=True)
    descricao = db.Column(db.Text, unique=False)
    solucao = db.Column(db.Text, unique=False, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))

    def __repr__(self):
        return f'Ticket id: {self.id}'

    def valida_fechamento(self):
        if self.fechado:
            self.andamento = False
            return True
        
