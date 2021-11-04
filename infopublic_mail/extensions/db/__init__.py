from flask_sqlalchemy import SQLAlchemy
from pytz import timezone
from datetime import datetime

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

class User(db.Model):
    __tablename__ = 'infopublic_acessos'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return f'User {self.username}, email: {self.email}'