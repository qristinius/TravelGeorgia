from app.extensions import db, login_manager
from app.models.base import BaseModel
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash




class User(BaseModel, UserMixin):
    __tablename__ = "Users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    email = db.Column(db.String)
    mobile_number = db.Column(db.String)
    _password = db.Column("password", db.String)
    confirmed = db.Column(db.Boolean, default=False)
    reset_password = db.Column(db.Boolean, default=False)
    


    def _get_password(self):
        return self._password

    def _set_password(self, password):
        self._password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    password = db.synonym('_password', descriptor=property(_get_password, _set_password))
