# Author: Nathaniel Adewara
# Date: 4/9/2026
# File: staff.py
# Description: Define the staff model class
from extensions import db


class Staff(db.Model):
    __tablename__ = 'Staff'

    staff_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    role = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(20))
    address = db.Column(db.String(200))
    rentals = db.relationship("Rental", backref="staff", lazy=True)

    rentals = db.relationship("Rental", backref="staff", lazy=True)

    def __init__(self, first_name, last_name, username, email, role, phone, address):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.role = role
        self.phone = phone
        self.address = address

    def __repr__(self):
        return f"<Staff {self.first_name} {self.last_name}>"
