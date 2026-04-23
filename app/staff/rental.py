# # Author: Nathaniel Adewara
# # Date: 4/15/2026
# # File: rental.py
# # Description: Define the rental model class
# from extensions import db
#
# # Rental model used to connect staff and customer data
# class Rental(db.Model):
#     __tablename__ = "Rental"
#
#     rental_id = db.Column(db.Integer, primary_key=True)
#     customer_id = db.Column(db.Integer, db.ForeignKey("Customer.customer_id"), nullable=False)
#     staff_id = db.Column(db.Integer, db.ForeignKey("Staff.staff_id"), nullable=False)
#     vehicle_id = db.Column(db.Integer, db.ForeignKey("Vehicle.vehicle_id"), nullable=False)
#     checkout_date = db.Column(db.String(50), nullable=False)
#     due_date = db.Column(db.String(50), nullable=False)
#     return_date = db.Column(db.String(50))
#     rental_status = db.Column(db.String(50), nullable=False)
#     total_cost = db.Column(db.Float, nullable=False)
#
#     def __repr__(self):
#         return f"<Rental {self.rental_id}>"
