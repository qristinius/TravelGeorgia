from flask import Blueprint, render_template, flash, request, redirect, url_for
from app.views.authentication.forms import RegisterForm, LoginForm
from app.extensions import db
from app.models.user import User
from flask_login import login_user, logout_user
authentication_Blueprint  = Blueprint("authentication", __name__, template_folder="templates")

@authentication_Blueprint.route("/registration", methods =["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user_username = form.username.data
        user_email = form.email.data
        user_password = form.password.data
        user = User(username=user_username, email=user_email, password=user_password)
        user.create()
        user.save()
        flash("succesfully registered")
    else:
        print(form.errors)

       
    return render_template("authentication/registration.html", register_form = form)



@authentication_Blueprint.route("/authorisation", methods =["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
        return redirect(url_for('main.home'))

           
    return render_template("authentication/login.html", login_form=form)


@authentication_Blueprint.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main.home"))
