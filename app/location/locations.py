# Author: Arissa Green
# Date: 4/9/2026
# File: locations.py
# Description:

from extensions import db


class Location(db.Model):
    """
    Represents a physical rental branch location.

    Each location stores basic contact and geographic information.
    """
    __tablename__ = "location"
    # Primary key identifier for the location
    location_id = db.Column(db.Integer, primary_key=True)

    # Name of the branch (e.g., "Downtown Branch")
    location_name = db.Column(db.String(50), nullable=False)

    # City where the branch is based
    city = db.Column(db.String(50), nullable=False)

    # State
    state = db.Column(db.String(20), nullable=False)

    # Branch phone number
    phone_number = db.Column(db.String(100), nullable=False, unique=True)

    def __repr__(self):
        """Readable string representation for debugging/logging."""
        return f"<Location {self.location_id}: {self.location_name}>"
