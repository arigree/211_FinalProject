from extensions import db


class Vehicle(db.Model):
    __tablename__ = "Vehicle"

    vehicle_id = db.Column(db.Integer, primary_key=True)
    vin = db.Column(db.String(50), nullable=False, unique=True)
    make = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    color = db.Column(db.String(30), nullable=False)
    license_plate = db.Column(db.String(20), nullable=False, unique=True)
    mileage = db.Column(db.Integer, nullable=False)
    daily_rate = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(30), nullable=False)
    location_id = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Vehicle {self.vehicle_id}: {self.make} {self.model}>"
