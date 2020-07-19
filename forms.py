from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, StringField


class AuswalFormular(FlaskForm): # Erstelle ein  Formular
    aktion = SelectField(u'Was soll der Arduino tun?', choices=[('verbinden', 'verbinden'), ("dreh", "Schlüssel drehen")]) # Selektor
    serialDevice = StringField(u'Serielles Gerät')
    submit = SubmitField('Signal schicken') # Submit Button
