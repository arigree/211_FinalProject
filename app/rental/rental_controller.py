# # Author: Arissa Green
# # Date: 4/23/2026
# # File: rental_controller.py
# # Description:

from flask import Blueprint, render_template, request

from .rental_exceptions import RentalDataError
from .rental_manager import RentalManager
from .rental import Rental
from app.customer.customer import Customer
from app.staff.staff import Staff
from .vehicle import Vehicle

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
    rentals = RentalManager.get_all_rentals()
    print(RentalManager.get_all_rentals())
    return render_template("rental.html", rentals=rentals)


@rental_bp.route("/rental/search")
def search():
    query_text = request.args.get("q", "")

    try:
        rental = RentalManager.search_rentals(query_text)
        return render_template(
            "rental.html",
            rentals=rental,
            query=query_text,
        )
    except RentalDataError as error:
        return render_template(
            "rental.html",
            rental=[],
            query=query_text,
            error_message=str(error),
        ), 500

@rental_bp.route("/rental/add", methods=["GET", "POST"])
def add_rental():
    from flask import redirect, url_for

    if request.method == "POST":
        data = {
            "customer_id": int(request.form["customer_id"]),
            "vehicle_id": int(request.form["vehicle_id"]),
            "staff_id": int(request.form["staff_id"]),
            "checkout_date": request.form["checkout_date"],
            "due_date": request.form["due_date"],
            "return_date": request.form.get("return_date"),
            "checkout_mileage": request.form["checkout_mileage"],
            "return_mileage": request.form["return_mileage"],
            "rental_status": request.form["rental_status"],
            "total_cost": float(request.form["total_cost"]),
        }

        RentalManager.create_rental(data)
        return redirect(url_for("rental.show_rentals"))

    customers = Customer.query.all()
    staff_members = Staff.query.all()
    vehicles = Vehicle.query.all()

    return render_template("rental_form.html", customers=customers, staff_members=staff_members, vehicles=vehicles)

@rental_bp.route("/rental/edit/<int:rental_id>", methods=["GET", "POST"])
def edit_rental(rental_id):
    from flask import redirect, url_for

    rental = Rental.query.get_or_404(rental_id)

    if request.method == "POST":
        data = {
            "customer_id": int(request.form["customer_id"]),
            "vehicle_id": int(request.form["vehicle_id"]),
            "staff_id": int(request.form["staff_id"]),
            "checkout_date": request.form["checkout_date"],
            "due_date": request.form["due_date"],
            "return_date": request.form.get("return_date"),
            "checkout_mileage": request.form["checkout_mileage"],
            "return_mileage": request.form["return_mileage"],
            "rental_status": request.form["rental_status"],
            "total_cost": float(request.form["total_cost"]),
        }

        RentalManager.update_rental(rental_id, data)
        return redirect(url_for("rental.show_rentals"))

    customers = Customer.query.all()
    staff_members = Staff.query.all()
    vehicles = Vehicle.query.all()

    return render_template("rental_form.html", rental=rental, customers=customers, staff_members=staff_members, vehicles=vehicles)

@rental_bp.route("/rental/delete/<int:rental_id>", methods=["POST"])
def delete_rental_route(rental_id):
    from flask import redirect, url_for

    RentalManager.delete_rental(rental_id)
    return redirect(url_for("rental.show_rentals"))

@rental_bp.errorhandler(RentalDataError)
def handle_rental_data_error(error):
    return render_template(
        "rental.html",
        rental=[],
        error_message=str(error),
    ), 500

