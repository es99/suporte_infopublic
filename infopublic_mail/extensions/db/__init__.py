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