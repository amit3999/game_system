# create a __init__.py file in the models folder to make all the model act as a package if you dont have it already , also you can make one file with all the models just copy ythe all the code in the files into it
from . import db


class Game(db.Model):
    __tablename__ = 'Game'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False , unique=True)
    price = db.Column(db.Integer, nullable=False)
    Genre = db.Column(db.Integer, nullable=False)
    Quantity = db.Column(db.Integer, nullable=False)
