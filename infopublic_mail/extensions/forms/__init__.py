from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, DateField
from wtforms.validators import DataRequired, Email, Optional, InputRequired, EqualTo

class BuscarForm(FlaskForm):
    cpf = StringField('CPF para busca: ', validators=[DataRequired()])
    submit = SubmitField('Buscar')

class EnviaButton(FlaskForm):
    submit = SubmitField('Enviar')

class Cadastro(FlaskForm):
    cpf = StringField('CPF:', validators=[DataRequired()])
    nome = StringField('Nome:', validators=[DataRequired()])
    telefone = StringField('Telefone:', validators=[Optional()])
    rg = StringField('Rg:', validators=[Optional()])
    email = StringField('Email:', validators=[Email(), Optional()])
    senha = StringField('Senha:', validators=[InputRequired(), EqualTo('confirme', message='Senhas devem ser iguais')])
    confirme = StringField('Repetir Senha:')
    ativo = BooleanField('Usuário ativo no sistema?', validators=[Optional()])
    adm = BooleanField('Administrador?', validators=[Optional()])
    submit = SubmitField('Cadastrar')