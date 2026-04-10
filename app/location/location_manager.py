# Author: Arissa Green
# Date: 4/9/2026
# File: location_manager.py
# Description:

from sqlalchemy.exc import SQLAlchemyError

from .locations import Location
from .location_exceptions import LocationDataError


def get_all_locations():
    try:
        return Location.query.all()
    except SQLAlchemyError as exc:
        raise LocationDataError("Unable to load location data right now.") from exc