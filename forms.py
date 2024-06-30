from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class ConverterForm(FlaskForm):
    text = StringField('Text:', validators=[DataRequired()])
    convert = SubmitField('Convert')

class InverterForm(FlaskForm):
    morse = StringField('Morse Code:', validators=[DataRequired()])
    invert = SubmitField('Invert')