from app.extensions import db
from app.models.base import BaseModel


class Tour(BaseModel):
    __tablename__ = "tours"

    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String)
    duration = db.Column(db.String)
    price = db.Column(db.Integer)
    date = db.Column(db.String)
    available_places = db.Column(db.String)
    img =   db.Column(db.String)