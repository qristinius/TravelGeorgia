from flask import Blueprint, render_template
from flask_login import current_user
from app.models.home import Card
main_blueprint = Blueprint("main", __name__, template_folder="templates")


@main_blueprint.route("/")
def home():
    cards = Card.query.all()
    return render_template("main/home.html", cards = cards)