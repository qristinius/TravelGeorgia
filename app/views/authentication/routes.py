from flask import Blueprint, render_template, flash, request, redirect, url_for
from app.views.authentication.forms import RegisterForm, LoginForm, PasswordRecoveryForm, ResetPasswordForm
from app.models.user import User
from flask_login import login_user, logout_user
from app.email import send_email, confirm_key, create_key

authentication_Blueprint  = Blueprint("authentication", __name__, template_folder="templates")

@authentication_Blueprint.route("/registration", methods =["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user_username = form.username.data
        user_email = form.email.data
        user_number =form.mobile_number.data
        user_password = form.password.data
        user = User(username=user_username, email=user_email, mobile_number=user_number, password=user_password)
        user.create()
        user.save()
        flash("succesfully registered")
        key = create_key(form.email.data)
        html = render_template('authentication/_activation_message.html', key=key)
        send_email("Confirm your account", html, form.email.data)

        
    else:
        print(form.errors)
     
    return render_template("authentication/registration.html", register_form = form)

@authentication_Blueprint.route("/confirm_email/<string:key>")
def confirm_email(key):
    email = confirm_key(key)
    user = User.query.filter_by(email=email).first()
    if user and not user.confirmed:
        user.confirmed = True
        user.save()
        return redirect(url_for('main.home'))
    else:
        flash("Wrong secret key or expired, or already confirmed")
    


@authentication_Blueprint.route("/forgot_password", methods=['GET', 'POST'])
def forgot_password():
    form = PasswordRecoveryForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            user.reset_password = True
            reset_key = create_key(form.email.data)
            html = render_template('authentication/_reset_message.html', key=reset_key)
            send_email("Reset your password", html, form.email.data)
            user.save()
            flash("You have been emailed password reset link") 
    return render_template('authentication/forgot_password.html', form=form)


@authentication_Blueprint.route("/reset_password/<string:key>", methods=['GET', 'POST'])
def reset_password(key):
    form = ResetPasswordForm()
    email = confirm_key(key)
    user = User.query.filter_by(email=email).first()

    if not user: return "Wrong secret key or expired, or already confirmed"
    if not user.reset_password: flash("Password already reset")

    if form.validate_on_submit():
        user.password = form.password.data
        user.reset_password = False
        user.save()
        return redirect(url_for('authentication.login'))
    return render_template("authentication/reset_password.html", form=form)



@authentication_Blueprint.route("/authorisation", methods =["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        next = request.args.get("next")
        if user and user.check_password(form.password.data):
            login_user(user)
            if next:
                return redirect(url_for("profile.myaccount"))
            else:
                return redirect(url_for("main.home"))
        return redirect(url_for('main.home'))

           
    return render_template("authentication/login.html", login_form=form)




@authentication_Blueprint.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main.home"))
