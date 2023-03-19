from wtforms.fields import StringField, PasswordField, EmailField,SubmitField, IntegerField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, length, equal_to, Email



class RegisterForm(FlaskForm):
    username = StringField(validators=[DataRequired("username is required")])
    email = EmailField(validators=[DataRequired(), Email()])
    mobile_number = IntegerField(validators=[DataRequired("Mobile_number is required")])
    password = PasswordField(validators=[DataRequired("password is required"),
                                         length(message="password length not satisfied", min=8, max=16)])
    confirm_password = PasswordField(validators=[DataRequired("confirm password required"),
                                                 equal_to("password", message="Password do not match")])

    submit = SubmitField()


class LoginForm(FlaskForm):
    email = EmailField(validators=[DataRequired(), Email()])
    password = PasswordField(validators=[DataRequired("password is required")])
    submit = SubmitField()


class PasswordRecoveryForm(FlaskForm):
    email = EmailField('Email', [DataRequired(), Email()])
    submit = SubmitField('Reset')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password',[DataRequired()])
    confirm_password = PasswordField('Repeat password', [DataRequired(), equal_to('password')])
    submit = SubmitField('Reset')
    

