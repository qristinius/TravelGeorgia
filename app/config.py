from os import path, sep, pardir



class Config(object):
    SECRET_KEY = "Gradient"
    BASE_DIR = path.abspath(path.dirname(__file__) + sep + pardir)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + path.join(BASE_DIR, 'db.sqlite')

    MAIL_SERVER='sandbox.smtp.mailtrap.io'
    MAIL_PORT = 2525
    MAIL_USERNAME = '769b12411b12b0'
    MAIL_PASSWORD = '57cbda838b314c'
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    FLASK_ADMIN_SWATCH = "cyborg"


class Constant:
    SERIALIZER_SALT = "12345678"