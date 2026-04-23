# Author: Arissa Green
# Date: 4/23/2026
# File: rental.py
# Description:

# from extensions import db
#
#
# class Rental(db.Model):
#     __tablename__ = "rental"
#
#     rental_id = db.Column(db.Integer, primary_key=True)
#     checkout_date = db.Column(db.String(50), nullable=False)
#     due_date = db.Column(db.String(50), nullable=False)
#     return_date = db.Column(db.String(20), nullable=False)
#     checkout_mileage = db.Column(db.String(100), nullable=False)
#     return_mileage = db.Column(db.String(100), nullable=False)
#     rental_status = db.Column(db.String(20), nullable=False)
#     total_cost = db.Column(db.String(50), nullable=False)
#
#
#     def __repr__(self):
#         return f"<Rental {self.rental_id}: {self.rental_status}>"
