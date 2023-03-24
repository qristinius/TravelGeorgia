from flask import Flask
from app.config import Config
from app.views.main.routes import main_blueprint
from app.views.authentication.routes import authentication_Blueprint
from app.views.tours.routes import tour_blueprint
from app.views.profile.routes import profile_blueprint
from app.extensions import db, migrate,login_manager, mail, admin
from app.commands import init_db, populate_db
from app.models.user import User
from app.models.tours import Tour
from app.admin_modules import SecuredModelView, UserModelView
from flask_admin.base import MenuLink


BLUEPRINTS = [main_blueprint, authentication_Blueprint, profile_blueprint, tour_blueprint]
COMMANDS = [init_db, populate_db]


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
    login_manager.login_view = "authentication.login"
    mail.init_app(app)

    
    @login_manager.user_loader
    def load_user(_id):
        return User.query.get(_id)

    admin.init_app(app)
    admin.add_view(SecuredModelView(Tour, db.session, endpoint="tour" ))
    admin.add_view(UserModelView(User, db.session))
    admin.add_link(MenuLink("Return", url="/", icon_type="fa", icon_value="fa-sign-out"))


def register_commands(app):
    for command in COMMANDS:
        app.cli.add_command(command)


def register_blueprints(app):
    for blueprint in BLUEPRINTS:
        app.register_blueprint(blueprint)