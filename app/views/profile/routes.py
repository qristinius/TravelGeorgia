from flask import Blueprint, render_template
from flask_login import current_user, login_required
from app.views.profile.forms import ProfileForm

profile_blueprint = Blueprint("profile", __name__, template_folder="templates")


@profile_blueprint.route("/profile")
@login_required
def myaccount():
    form = ProfileForm()
    return render_template("profile/profile.html", profile_form = form)