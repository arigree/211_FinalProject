from sqlalchemy.exc import SQLAlchemyError

from .vehicle import Vehicle
from .vehicle_exceptions import VehicleDataError


def get_all_vehicles():
    try:
        return Vehicle.query.all()
    except SQLAlchemyError as exc:
        raise VehicleDataError("Unable to load vehicle data right now.") from exc
