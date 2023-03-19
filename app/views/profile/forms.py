from wtforms.fields import StringField, PasswordField, EmailField,SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import length, equal_to, Email



class ProfileForm(FlaskForm):
    username = StringField()
    email = EmailField(Email())
    mobile = StringField()
    password = PasswordField(validators=[length(message="password length not satisfied", min=8, max=16)])
    confirm_password = PasswordField(validators=[equal_to("password", message="Password do not match")])
    submit = SubmitField()
