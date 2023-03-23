from flask.cli import with_appcontext
from app.models.user import User
from app.models.tours import Tour
from app.models.home import Card
from app.extensions import db
import click

from data import Tours, Home_cards


@click.command("init_db")
@with_appcontext
def init_db():
    click.echo("Creating Database")
    db.drop_all()
    db.create_all()
    click.echo("Finished Creating Database")


@click.command("populate_db")
@with_appcontext
def populate_db():

    click.echo("Add Tours in Database")
    for tour in Tours:
        tour_item = Tour(location=tour["location"], duration=tour["duration"], price=tour["price"],
                        date=tour["date"], available_places=tour["available_places"],  img=tour["img"])
        db.session.add(tour_item)

    click.echo("Add Home_cards in Database")
    for home_card in Home_cards:
        card_item = Card(location=home_card["location"], information=home_card["information"], img = home_card["img"])

        db.session.add(card_item)


  
    click.echo("Done")

    db.session.commit()
