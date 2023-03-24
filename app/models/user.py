from app.extensions import db, login_manager
from app.models.base import BaseModel
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user



class User(BaseModel, UserMixin):
    __tablename__ = "Users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    email = db.Column(db.String, unique = True, nullable = False)
    mobile_number = db.Column(db.String)
    role = db.Column(db.String, nullable = False)
    _password = db.Column("password", db.String)
    confirmed = db.Column(db.Boolean, default=False)
    reset_password = db.Column(db.Boolean, default=False)
    


    def _get_password(self):
        return self._password

    def _set_password(self, password):
        self._password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def has_role(self, role):
        return role in [current_user.role]
    
    password = db.synonym('_password', descriptor=property(_get_password, _set_password))


