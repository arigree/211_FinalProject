# Author: Arissa Green
# Date: 4/23/2026
# File: rental.py
# Description:

from extensions import db
from .vehicle import Vehicle

class Rental(db.Model):
    """
    Represents a rental transaction.

    Links a customer, vehicle, and staff member together with
    rental timing, mileage, status, and cost.
    """
    __tablename__ = "Rental"

    # PK
    rental_id = db.Column(db.Integer, primary_key=True)

    # FKs
    customer_id = db.Column(db.Integer, db.ForeignKey("Customer.customer_id"), nullable=False)
    vehicle_id = db.Column(db.Integer, db.ForeignKey("Vehicle.vehicle_id"), nullable=False)
    staff_id = db.Column(db.Integer, db.ForeignKey("Staff.staff_id"), nullable=False)

    # Rental timeline
    checkout_date = db.Column(db.String(50), nullable=False)
    due_date = db.Column(db.String(50), nullable=False)
    return_date = db.Column(db.String(50))

    # Mileage tracking
    checkout_mileage = db.Column(db.String(50), nullable=False)
    return_mileage = db.Column(db.String(50))

    # Status
    rental_status = db.Column(db.String(50), nullable=False)

    # Total rental cost
    total_cost = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<Rental {self.rental_id}: {self.rental_status}>"
