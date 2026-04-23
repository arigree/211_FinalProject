# # Author: Arissa Green
# # Date: 4/23/2026
# # File: rental_controller.py
# # Description:

from flask import Blueprint, render_template, request

from .rental_exceptions import RentalDataError
from .rental_manager import get_all_rentals, search_rentals

# Blueprint setup
rental_bp = Blueprint(
    "rental",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/rental-static",
)


@rental_bp.route("/rental")
def show_rentals():
    rentals = get_all_rentals()
    print(get_all_rentals())
    return render_template("rental.html", rentals=rentals)


@rental_bp.route("/rental/search")
def search():
    query_text = request.args.get("q", "")

    try:
        rental = search_rentals(query_text)
        return render_template(
            "rental.html",
            rental=rental,
            query=query_text,
        )
    except RentalDataError as error:
        return render_template(
            "rental.html",
            rental=[],
            query=query_text,
            error_message=str(error),
        ), 500

@rental_bp.errorhandler(RentalDataError)
def handle_rental_data_error(error):
    return render_template(
        "rental.html",
        rental=[],
        error_message=str(error),
    ), 500
