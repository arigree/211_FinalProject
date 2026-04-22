from extensions import db


class Customer(db.Model):
    __tablename__ = "Customer"

    customer_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    driver_license_number = db.Column(db.String(50), nullable=False, unique=True)
    address = db.Column(db.String(200), nullable=False)
    rentals = db.relationship("Rental", backref="customer", lazy=True)

    rentals = db.relationship("Rental", backref="customer", lazy=True)

    def __repr__(self):
        return f"<Customer {self.customer_id}: {self.first_name} {self.last_name}>"
