from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, URL

class SubmitForm(FlaskForm):
    longurl = StringField('Long URL', validators=[URL(message='Please enter a valid link to shorten. Make sure it includes http:// or https://'), DataRequired()])
    submit = SubmitField('Create Short URL')
