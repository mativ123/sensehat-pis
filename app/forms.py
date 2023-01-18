from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, SelectField, IntegerField
from wtforms.validators import DataRequired, ValidationError, EqualTo, NumberRange

class Specs(FlaskForm):
    kml = IntegerField("km/l", validators=[DataRequired()])
    tanktStrl = IntegerField("tank størrelse [l]")
    submit = SubmitField("send")
