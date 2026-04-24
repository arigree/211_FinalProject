# Author: Arissa Green
# Date: 4/9/2026
# File: location_manager.py
# Description:

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import or_

from extensions import db
from .locations import Location
from .location_exceptions import LocationDataError

class LocationManager:
    """
    Handles all database operations related to Location.
    Separates business logic from route/controller logic.
    """
    @staticmethod
    def get_all_locations():
        """Returns all locations."""

        try:
            return Location.query.all()
        except SQLAlchemyError as exc:
            raise LocationDataError("Unable to load location data right now.") from exc

    @staticmethod
    def search_locations(search_text: str):
        """
        Searches locations based on partial matches across multiple fields.
        """
        try:
            search_text = (search_text or "").strip()

            if not search_text:
                return Location.query.all()
            terms = [term for term in search_text.split() if term]
            query = Location.query

            for term in terms:
                pattern = f"%{term}%"
                query = query.filter(
                    or_(
                        Location.location_name.ilike(pattern),
                        Location.city.ilike(pattern),
                        Location.state.ilike(pattern),
                        Location.phone_number.ilike(pattern),
                    )
                )

            results = query.order_by(Location.location_name.asc()).limit(20).all()

            if not results:
                raise LocationDataError("No locations matched your search.")
            return results

        except SQLAlchemyError as exc:
            raise LocationDataError("Unable to load location data right now.") from exc

    @staticmethod
    def create_location(data):
        """Creates and saves a new location."""
        try:
            location = Location(**data)
            db.session.add(location)
            db.session.commit()
            return location
        except SQLAlchemyError as exc:
            db.session.rollback()
            raise LocationDataError("Unable to create location.") from exc

    @staticmethod
    def update_location(location_id, data):
        """Updates an existing location."""
        try:
            location = Location.query.get(location_id)

            if not location:
                raise LocationDataError("Location not found.")

            for key, value in data.items():
                setattr(location, key, value)

            db.session.commit()
            return location

        except SQLAlchemyError as exc:
            db.session.rollback()
            raise LocationDataError("Unable to update location.") from exc

    @staticmethod
    def delete_location(location_id):
        """Deletes a location."""
        try:
            location = Location.query.get(location_id)

            if not location:
                raise LocationDataError("Location not found.")

            db.session.delete(location)
            db.session.commit()

        except SQLAlchemyError as exc:
            db.session.rollback()
            raise LocationDataError("Unable to delete location.") from exc


    @staticmethod
    def handle_exceptions(exception):
        db.session.rollback()
        orig_error = exception.__dict__.get('orig', "")
        if isinstance(exception, (LocationDataError)):
            return exception.__str__()
        elif isinstance(exception, SQLAlchemyError):
            return f"An database error occurred: {str(orig_error)}."
        else:
            return f"An unexpected error occurred: {str(orig_error)}"