from datetime import datetime
from app import db

class Pickle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    kmkort = db.Column(db.Float)
    tankstrl = db.Column(db.Integer)
    kml = db.Column(db.Integer)
