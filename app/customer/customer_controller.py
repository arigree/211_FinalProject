from flask import Blueprint, render_template

from .customer_exceptions import CustomerDataError
from .customer_manager import get_all_customers

customer_bp = Blueprint(
    "customer",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/customer-static",
)


@customer_bp.route("/customers")
def show_customers():
    try:
        customers = get_all_customers()
        return render_template("customers.html", customers=customers, error_message=None)
    except CustomerDataError:
        return render_template(
            "customers.html",
            customers=[],
            error_message="Sorry, customer data could not be loaded right now.",
        )
    except Exception:
        return render_template(
            "customers.html",
            customers=[],
            error_message="Something went wrong while loading the page.",
        )
