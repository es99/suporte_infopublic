from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class BuscarForm(FlaskForm):
    cpf = StringField('CPF para busca: ', validators=[DataRequired()])
    submit = SubmitField('Buscar')