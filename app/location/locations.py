# Author: Arissa Green
# Date: 4/9/2026
# File: locations.py
# Description:

from extensions import db


class Location(db.Model):
    __tablename__ = "location"

    location_id = db.Column(db.Integer, primary_key=True)
    location_name = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    state = db.Column(db.String(20), nullable=False)
    phone_number = db.Column(db.String(100), nullable=False, unique=True)

    def __repr__(self):
        return f"<Location {self.location_id}: {self.location_name}>"
