from . import db

class Customer(db.Model):
    __tablename__ = 'Customer'
    username = db.Column(db.String(200), primary_key=True)
    email = db.Column(db.String(200), nullable=False,unique=True)
    phone_number = db.Column(db.String(200), nullable=False)
