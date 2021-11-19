from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField, FileField
from wtforms.validators import DataRequired, Optional

class TicketForm(FlaskForm):
    sistema = SelectField('Sistema:', choices=[
        ('PJPCTB', 'CONTABILIDADE'), 
        ('PJFOLHA', 'FOLHA'),
        ('PJTRIBUTOS', 'TRIBUTOS'),
        ('PJFROTA', 'FROTA'),
        ('PJCHEQUE', 'CHEQUE'),
        ('PJDOACAO', 'DOAÇÃO'),
        ('PJTOMB', 'TOMBAMENTO'),
        ('NOTA', 'NOTA FISCAL')
    ])
    entidade = StringField('Entidade', validators=[DataRequired()],
                            description='exemplo: Cras Picui, Camara Umbuzeiro, PM Mari')
    assunto = StringField('Assunto:', validators=[DataRequired()])
    descricao = TextAreaField('Descrição detalhada do problema', validators=[DataRequired()])
    submit = SubmitField('Abrir ticket')