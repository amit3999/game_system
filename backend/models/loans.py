# create a __init__.py file in the models folder to make all the model act as a package if you dont have it already , also you can make one file with all the models just copy ythe all the code in the files into it
from . import db
from datetime import datetime 
from .customers import Customer
from .game import Game

class Loan(db.Model):
    __tablename__ = 'Loan'
    customer_username = db.Column(db.String(200), db.ForeignKey('Customer.username',ondelete='RESTRICT'),nullable=False)
    game_title = db.Column(db.String(200), db.ForeignKey('Game.title',ondelete='RESTRICT'),nullable=False)
    loan_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    return_date = db.Column(db.DateTime)
    __table_args__ = (
        db.PrimaryKeyConstraint('customer_username', 'game_title'),
    )

