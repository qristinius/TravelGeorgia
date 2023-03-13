from flask import Flask
from app.config import Config
from app.views.main.routes import main_blueprint
from app.views.authentication.routes import authentication_Blueprint
from app.extensions import db, migrate,login_manager, mail
from app.commands import init_db
from app.models.user import User


BLUEPRINTS = [main_blueprint, authentication_Blueprint]
COMMANDS = [init_db]


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    register_blueprints(app)
    register_extensions(app)
    register_commands(app)

    return app

def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    
    @login_manager.user_loader
    def load_user(_id):
        return User.query.get(_id)


def register_commands(app):
    for command in COMMANDS:
        app.cli.add_command(command)


def register_blueprints(app):
    for blueprint in BLUEPRINTS:
        app.register_blueprint(blueprint)