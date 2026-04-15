from flask import Blueprint, render_template, request

from .customer_exceptions import CustomerDataError, CustomerQueryError
from .customer_manager import get_filtered_customers

customer_bp = Blueprint(
    "customer",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/customer-static",
)


def get_current_filters():
    return {
        "city": request.args.get("city", ""),
        "area_code": request.args.get("area_code", ""),
        "sort_by": request.args.get("sort_by", "customer_id"),
        "order": request.args.get("order", "asc"),
        "limit": request.args.get("limit", ""),
    }


@customer_bp.route("/customers")
def show_customers():
    customers = get_filtered_customers(**get_current_filters())
    return render_template(
        "customers.html",
        customers=customers,
        error_message=None,
        current_filters=get_current_filters(),
    )


@customer_bp.errorhandler(CustomerQueryError)
def handle_customer_query_error(error):
    return render_template(
        "customers.html",
        customers=[],
        error_message=str(error),
        current_filters=get_current_filters(),
    ), 400


@customer_bp.errorhandler(CustomerDataError)
def handle_customer_data_error(error):
    return render_template(
        "customers.html",
        customers=[],
        error_message=str(error),
        current_filters=get_current_filters(),
    ), 500


@customer_bp.errorhandler(Exception)
def handle_customer_unexpected_error(error):
    return render_template(
        "customers.html",
        customers=[],
        error_message="Something went wrong while loading the page.",
        current_filters=get_current_filters(),
    ), 500
