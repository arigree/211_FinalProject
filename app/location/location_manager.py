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

    @staticmethod
    def get_all_locations():
        try:
            return Location.query.all()
        except SQLAlchemyError as exc:
            raise LocationDataError("Unable to load location data right now.") from exc

    @staticmethod
    def search_locations(search_text: str):
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
    def handle_exceptions(exception):
        db.session.rollback()
        orig_error = exception.__dict__.get('orig', "")
        if isinstance(exception, (LocationDataError)):
            return exception.__str__()
        elif isinstance(exception, SQLAlchemyError):
            return f"An database error occurred: {str(orig_error)}."
        else:
            return f"An unexpected error occurred: {str(orig_error)}"