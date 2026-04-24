# Author: Arissa Green
# Date: 4/9/2026
# File: location_controller.py
# Description:

from flask import Blueprint, render_template, request

from .location_exceptions import LocationDataError
from .location_manager import LocationManager
from. locations import Location

# Blueprint groups all location-related routes together
location_bp = Blueprint(
    "location",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/location-static",
)

@location_bp.route("/locations")
def show_locations():
    """
       Displays all locations stored in the database.
       """
    locations = LocationManager.get_all_locations()
    return render_template("locations.html", locations=locations)

@location_bp.route("/locations/search")
def search():
    """
       Searches locations based on user query (name, city, state, phone).
       """
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
    """
      Handles creation of a new location.
      GET: display form
      POST: create location and redirect
      """
    from flask import redirect, url_for

    if request.method == "POST":

        name = request.form.get("location_name", "").strip()
        city = request.form.get("city", "").strip()
        state = request.form.get("state", "").strip()
        phone = request.form.get("phone_number", "").strip()

        # Required fields
        if not name:
            raise LocationDataError("Location name is required.")

        if not city:
            raise LocationDataError("City is required.")

        if not state:
            raise LocationDataError("State is required.")

        if not phone:
            raise LocationDataError("Phone number is required.")

        if not phone.isdigit():
            raise LocationDataError("Phone number must contain only digits.")


        data = {
            "location_name": name,
            "city": city,
            "state": state,
            "phone_number": phone,
        }

        LocationManager.create_location(data)
        return redirect(url_for("location.show_locations"))

    return render_template("location_form.html")

@location_bp.route("/locations/edit/<int:location_id>", methods=["GET", "POST"])
def edit_location(location_id):
    """
       Updates an existing location.
       GET: pre-fill form
       POST: save changes
       """
    from flask import redirect, url_for

    location = Location.query.get_or_404(location_id)

    if request.method == "POST":
        name = request.form.get("location_name", "").strip()
        city = request.form.get("city", "").strip()
        state = request.form.get("state", "").strip()
        phone = request.form.get("phone_number", "").strip()

        # Required fields
        if not name:
            raise LocationDataError("Location name is required.")

        if not city:
            raise LocationDataError("City is required.")

        if not state:
            raise LocationDataError("State is required.")

        if not phone:
            raise LocationDataError("Phone number is required.")

        if not phone.isdigit():
            raise LocationDataError("Phone number must contain only digits.")

        data = {
            "location_name": name,
            "city": city,
            "state": state,
            "phone_number": phone,
        }

        LocationManager.update_location(location_id, data)
        return redirect(url_for("location.show_locations"))

    return render_template("location_form.html", location=location)

@location_bp.route("/locations/delete/<int:location_id>", methods=["POST"])
def delete_location_route(location_id):
    """
    Deletes a location from the database.
    """
    from flask import redirect, url_for

    LocationManager.delete_location(location_id)
    return redirect(url_for("location.show_locations"))

