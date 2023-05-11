from app import db

class Noodle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String)
    name = db.Column(db.String)
    description = db.Column(db.String)
    spice = db.Column(db.Integer)
    sodium = db.Column(db.Integer)
    price = db.Column(db.Integer)
