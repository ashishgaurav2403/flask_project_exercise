from . import db

class User(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    email=db.Column(db.String(100) , unique=True)
    name=db.Column(db.String(100))
    pasword=db.Column(db.String(100))