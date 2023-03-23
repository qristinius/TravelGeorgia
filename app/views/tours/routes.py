from flask import Blueprint, render_template
from app.models.tours import Tour
tour_blueprint = Blueprint("tours", __name__, template_folder="templates")


@tour_blueprint.route("/tours")
def choose_tour():
    tours = Tour.query.all()
    return render_template("tours/tours.html", tours=tours)
