from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from infopublic_mail.extensions.db import User

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField('Senha', validators=[DataRequired()])
    remember_me = BooleanField('Mantenha-me logado')
    submit = SubmitField('Log In')

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
    username = StringField('Nome de usuário', validators=[DataRequired(), Length(1, 64),
                            Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                            'Nomes de usuários só podem conter letras, numeros, pontos e '
                            'underscores')])
    password = PasswordField('Senha', validators=[DataRequired(), EqualTo('password2', 
                            message='As senhas devem ser iguais!')])
    password2 = PasswordField('Confirme a senha', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('O email já encontra-se registrado!')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Nome de usuário já em uso!')