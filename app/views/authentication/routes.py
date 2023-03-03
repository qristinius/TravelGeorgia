from flask import Blueprint, render_template, flash
from app.views.authentication.forms import RegisterForm
from app.extensions import db
from app.models.user import User
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