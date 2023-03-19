from wtforms.fields import StringField, PasswordField, EmailField,SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import length, equal_to, Email



class ProfileForm(FlaskForm):
    username = StringField()
    email = EmailField(Email())
    mobile = StringField()
    submit = SubmitField()
