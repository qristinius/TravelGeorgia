from flask.cli import with_appcontext
from app.models.user import User
from app.extensions import db
import click



@click.command("init_db")
@with_appcontext
def init_db():
    click.echo("Creating Database")
    db.drop_all()
    db.create_all()
    click.echo("Finished Creating Database")


