from flask import render_template

from app import create_app
from app import create_app
from app.location.location_exceptions import LocationDataError
from app.rental.rental_exceptions import RentalDataError
from app.customer.customer_exceptions import CustomerDataError
from app.staff.staff_exceptions import StaffException



app = create_app()

@app.errorhandler(LocationDataError)
@app.errorhandler(RentalDataError)
@app.errorhandler(CustomerDataError)
@app.errorhandler(StaffException)
def handle_data_errors(error):
    """
    Centralized handler for all domain-specific data errors.
    Returns a user-friendly error page instead of crashing.
    """
    return render_template(
        "error.html",
        error_message=str(error)
    ), 500


if __name__ == "__main__":
    app.run(debug=True)
