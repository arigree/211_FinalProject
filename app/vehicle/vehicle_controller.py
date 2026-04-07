from flask import Blueprint, render_template

from .vehicle_exceptions import VehicleDataError
from .vehicle_manager import get_all_vehicles

vehicle_bp = Blueprint("vehicle", __name__, template_folder="templates")


@vehicle_bp.route("/vehicles")
def show_vehicles():
    try:
        vehicles = get_all_vehicles()
        return render_template("vehicles.html", vehicles=vehicles, error_message=None)
    except VehicleDataError:
        return render_template(
            "vehicles.html",
            vehicles=[],
            error_message="Sorry, vehicle data could not be loaded right now.",
        )
