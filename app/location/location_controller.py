# Author: Arissa Green
# Date: 4/9/2026
# File: location_controller.py
# Description:

from flask import Blueprint, render_template

from .location_exceptions import LocationDataError
from .location_manager import get_all_locations

# Blueprint setup
location_bp = Blueprint(
    "location",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/location-static",
)


@location_bp.route("/locations")
def show_locations():
    locations = get_all_locations()
    return render_template("locations.html", locations=locations)


@location_bp.errorhandler(LocationDataError)
def handle_location_data_error(error):
    return render_template(
        "locations.html",
        locations=[],
        error_message=str(error),
    ), 500