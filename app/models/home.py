from app.extensions import db
from app.models.base import BaseModel


class Card(BaseModel):
    __tablename__ = "Home Cards"

    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String)
    information = db.Column(db.String)
    img =   db.Column(db.String)