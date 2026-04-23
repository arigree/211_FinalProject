# Author: Arissa Green
# Date: 4/9/2026
# File: location_controller.py
# Description:

from flask import Blueprint, render_template, request

from .location_exceptions import LocationDataError
from .location_manager import LocationManager
from. locations import Location

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

@location_bp.route("/locations/add", methods=["GET", "POST"])
def add_location():
    from flask import redirect, url_for

    if request.method == "POST":
        data = {
            "location_name": request.form["location_name"],
            "city": request.form["city"],
            "state": request.form["state"],
            "phone_number": request.form["phone_number"],
        }

        LocationManager.create_location(data)
        return redirect(url_for("location.show_locations"))

    return render_template("location_form.html")

@location_bp.route("/locations/edit/<int:location_id>", methods=["GET", "POST"])
def edit_location(location_id):
    from flask import redirect, url_for

    location = Location.query.get_or_404(location_id)

    if request.method == "POST":
        data = {
            "location_name": request.form["location_name"],
            "city": request.form["city"],
            "state": request.form["state"],
            "phone_number": request.form["phone_number"],
        }

        LocationManager.update_location(location_id, data)
        return redirect(url_for("location.show_locations"))

    return render_template("location_form.html", location=location)

@location_bp.route("/locations/delete/<int:location_id>", methods=["POST"])
def delete_location_route(location_id):
    from flask import redirect, url_for

    LocationManager.delete_location(location_id)
    return redirect(url_for("location.show_locations"))

@location_bp.errorhandler(LocationDataError)
def handle_location_data_error(error):
    return render_template(
        "locations.html",
        locations=[],
        error_message=str(error),
    ), 500

