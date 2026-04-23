# Author: Arissa Green
# Date: 4/9/2026
# File: location_controller.py
# Description:

from flask import Blueprint, render_template, request

from .location_exceptions import LocationDataError
from .location_manager import LocationManager

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
    locations = LocationManager.get_all_locations()
    return render_template("locations.html", locations=locations)

@location_bp.route("/locations/search")
def search():
    query_text = request.args.get("q", "")

    try:
        locations = LocationManager.search_locations(query_text)
        return render_template(
            "locations.html",
            locations=locations,
            query=query_text,
        )
    except LocationDataError as error:
        return render_template(
            "locations.html",
            locations=[],
            query=query_text,
            error_message=str(error),
        ), 500

@location_bp.errorhandler(LocationDataError)
def handle_location_data_error(error):
    return render_template(
        "locations.html",
        locations=[],
        error_message=str(error),
    ), 500

