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
    """
    Handles creation of a rental.

    GET: display form
    POST: validate input and create rental
    """
    from flask import redirect, url_for

    if request.method == "POST":

        try:
            customer_id = int(request.form.get("customer_id", ""))
            vehicle_id = int(request.form.get("vehicle_id", ""))
            staff_id = int(request.form.get("staff_id", ""))
        except ValueError:
            raise RentalDataError("Customer, Vehicle, and Staff must be valid IDs.")

        checkout_date = request.form.get("checkout_date", "").strip()
        due_date = request.form.get("due_date", "").strip()
        status = request.form.get("rental_status", "").strip()

        if not checkout_date:
            raise RentalDataError("Checkout date is required.")

        if not due_date:
            raise RentalDataError("Due date is required.")

        if not status:
            raise RentalDataError("Rental status is required.")

        checkout_mileage = request.form.get("checkout_mileage", "").strip()
        return_mileage = request.form.get("return_mileage", "").strip()

        if not checkout_mileage:
            raise RentalDataError("Checkout mileage is required.")

        try:
            total_cost = float(request.form.get("total_cost", ""))
        except ValueError:
            raise RentalDataError("Total cost must be a valid number.")

        if not Customer.query.get(customer_id):
            raise RentalDataError("Selected customer does not exist.")

        if not Staff.query.get(staff_id):
            raise RentalDataError("Selected staff member does not exist.")

        if not Vehicle.query.get(vehicle_id):
            raise RentalDataError("Selected vehicle does not exist.")

        data = {
            "customer_id": customer_id,
            "vehicle_id": vehicle_id,
            "staff_id": staff_id,
            "checkout_date": checkout_date,
            "due_date": due_date,
            "return_date": request.form.get("return_date"),
            "checkout_mileage": checkout_mileage,
            "return_mileage": return_mileage,
            "rental_status": status,
            "total_cost": total_cost,
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

        try:
            customer_id = int(request.form.get("customer_id", ""))
            vehicle_id = int(request.form.get("vehicle_id", ""))
            staff_id = int(request.form.get("staff_id", ""))
        except ValueError:
            raise RentalDataError("Customer, Vehicle, and Staff must be valid IDs.")

        checkout_date = request.form.get("checkout_date", "").strip()
        due_date = request.form.get("due_date", "").strip()
        status = request.form.get("rental_status", "").strip()

        if not checkout_date:
            raise RentalDataError("Checkout date is required.")

        if not due_date:
            raise RentalDataError("Due date is required.")

        if not status:
            raise RentalDataError("Rental status is required.")

        checkout_mileage = request.form.get("checkout_mileage", "").strip()
        return_mileage = request.form.get("return_mileage", "").strip()

        if not checkout_mileage:
            raise RentalDataError("Checkout mileage is required.")

        try:
            total_cost = float(request.form.get("total_cost", ""))
        except ValueError:
            raise RentalDataError("Total cost must be a valid number.")

        if not Customer.query.get(customer_id):
            raise RentalDataError("Selected customer does not exist.")

        if not Staff.query.get(staff_id):
            raise RentalDataError("Selected staff member does not exist.")

        if not Vehicle.query.get(vehicle_id):
            raise RentalDataError("Selected vehicle does not exist.")

        data = {
            "customer_id": customer_id,
            "vehicle_id": vehicle_id,
            "staff_id": staff_id,
            "checkout_date": checkout_date,
            "due_date": due_date,
            "return_date": request.form.get("return_date"),
            "checkout_mileage": checkout_mileage,
            "return_mileage": return_mileage,
            "rental_status": status,
            "total_cost": total_cost,
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

