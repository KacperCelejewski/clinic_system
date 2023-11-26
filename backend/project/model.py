from . import db


class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    surrname = db.Column(db.String(40))
    pesel = db.Column(db.Integer)
