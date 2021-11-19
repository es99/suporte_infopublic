from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from infopublic_mail.extensions.db import User

class LoginForm(FlaskForm):
    cpf = StringField('CPF', validators=[DataRequired(),
                                        Regexp('[0-9]{3}[\.][0-9]{3}[\.][0-9]{3}[-][0-9]{2}', 0,
                            'Digite o cpf separados por pontos e traço, ex: 000.000.000-00')])
    password = PasswordField('Senha', validators=[DataRequired()])
    remember_me = BooleanField('Mantenha-me logado')
    submit = SubmitField('Log In')

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
    cpf = StringField('CPF', validators=[DataRequired(),
                            Regexp('[0-9]{3}[\.][0-9]{3}[\.][0-9]{3}[-][0-9]{2}', 0,
                            'Digite o cpf separados por pontos e traço, ex: 000.000.000-00')],
                            description='Ex: 000.000.000-00')
    nome = StringField('Nome', validators=[DataRequired(),
                                Regexp('[A-Z][a-z]{2,10}', 0,
                                '2 a 10 caracteres, apenas letras, iniciando com maiúscula')])
    sobrenome = StringField('Sobrenome', validators=[DataRequired(),
                                Regexp('[A-Z][a-z]{2,10}', 0,
                                '2 a 10 caracteres, apenas letras, iniciando com maiúscula')])
    celular = StringField('Celular', validators=[DataRequired(),
                            Regexp('[(][0-9]{2}[)] [9][\.][0-9]{4}[-][0-9]{4}', 0,
                            'Digite o número do telefone neste formato (xx) 9.xxxx-xxxx')], 
                            description='Ex (00) 9.0000-0000')
    password = PasswordField('Senha', validators=[DataRequired(), EqualTo('password2', 
                            message='As senhas devem ser iguais!')])
    password2 = PasswordField('Confirme a senha', validators=[DataRequired()])
    submit = SubmitField('Registrar')

    def validate_cpf(self, field):
        if User.query.filter_by(cpf=field.data).first():
            raise ValidationError('O CPF já encontra-se registrado!')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('O Email já encontra-se registrado!')