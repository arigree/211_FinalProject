# Author: Arissa Green
# Date: 4/23/2026
# File: vehicle.py
# Description:

from extensions import db

class Vehicle(db.Model):
    __tablename__ = "Vehicle"

    vehicle_id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String)
    model = db.Column(db.String)
    year = db.Column(db.Integer)
    color = db.Column(db.String)