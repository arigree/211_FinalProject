from flask import Blueprint, redirect, render_template, request, url_for

from .customer_exceptions import (
    CustomerDataError,
    CustomerNotFoundError,
    CustomerOperationError,
    CustomerQueryError,
)
from .customer_manager import CustomerManager

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


def get_customer_form_data():
    return {
        "first_name": request.form.get("first_name", ""),
        "last_name": request.form.get("last_name", ""),
        "phone": request.form.get("phone", ""),
        "email": request.form.get("email", ""),
        "driver_license_number": request.form.get("driver_license_number", ""),
        "address": request.form.get("address", ""),
    }


def render_customer_form(template_title, submit_label, form_action, customer_data, error_message=None):
    return render_template(
        "customer_form.html",
        page_title=template_title,
        submit_label=submit_label,
        form_action=form_action,
        customer_data=customer_data,
        error_message=error_message,
    )


@customer_bp.route("/customers")
def show_customers():
    customers = CustomerManager.get_filtered_customers(**get_current_filters())
    return render_template(
        "customers.html",
        customers=customers,
        error_message=None,
        status_message=request.args.get("message", ""),
        current_filters=get_current_filters(),
    )


@customer_bp.route("/customers/create", methods=["GET"])
def show_create_customer_form():
    return render_customer_form(
        template_title="Create Customer",
        submit_label="Create Customer",
        form_action=url_for("customer.create_customer_record"),
        customer_data={
            "first_name": "",
            "last_name": "",
            "phone": "",
            "email": "",
            "driver_license_number": "",
            "address": "",
        },
    )


@customer_bp.route("/customers/create", methods=["POST"])
def create_customer_record():
    customer_data = get_customer_form_data()

    try:
        CustomerManager.create_customer(customer_data)
    except CustomerDataError as error:
        return render_customer_form(
            template_title="Create Customer",
            submit_label="Create Customer",
            form_action=url_for("customer.create_customer_record"),
            customer_data=customer_data,
            error_message=str(error),
        ), 400

    return redirect(url_for("customer.show_customers", message="Customer created successfully."))


@customer_bp.route("/customers/<int:customer_id>/edit", methods=["GET"])
def show_edit_customer_form(customer_id):
    customer = CustomerManager.get_customer_by_id(customer_id)
    return render_customer_form(
        template_title="Edit Customer",
        submit_label="Save Changes",
        form_action=url_for("customer.update_customer_record", customer_id=customer_id),
        customer_data={
            "first_name": customer.first_name,
            "last_name": customer.last_name,
            "phone": customer.phone,
            "email": customer.email,
            "driver_license_number": customer.driver_license_number,
            "address": customer.address,
        },
    )


@customer_bp.route("/customers/<int:customer_id>/edit", methods=["POST"])
def update_customer_record(customer_id):
    customer_data = get_customer_form_data()

    try:
        CustomerManager.update_customer(customer_id, customer_data)
    except CustomerNotFoundError:
        raise
    except CustomerDataError as error:
        return render_customer_form(
            template_title="Edit Customer",
            submit_label="Save Changes",
            form_action=url_for("customer.update_customer_record", customer_id=customer_id),
            customer_data=customer_data,
            error_message=str(error),
        ), 400

    return redirect(url_for("customer.show_customers", message="Customer updated successfully."))


@customer_bp.route("/customers/<int:customer_id>/delete", methods=["GET"])
def show_delete_customer(customer_id):
    customer = CustomerManager.get_customer_by_id(customer_id)
    return render_template(
        "customer_delete.html",
        customer=customer,
        error_message=None,
    )


@customer_bp.route("/customers/<int:customer_id>/delete", methods=["POST"])
def delete_customer_record(customer_id):
    customer = CustomerManager.get_customer_by_id(customer_id)

    try:
        CustomerManager.delete_customer(customer_id)
    except CustomerOperationError as error:
        return render_template(
            "customer_delete.html",
            customer=customer,
            error_message=str(error),
        ), 400

    return redirect(url_for("customer.show_customers", message="Customer deleted successfully."))


@customer_bp.errorhandler(CustomerQueryError)
def handle_customer_query_error(error):
    return render_template(
        "customers.html",
        customers=[],
        error_message=str(error),
        status_message=None,
        current_filters=get_current_filters(),
    ), 400


@customer_bp.errorhandler(CustomerNotFoundError)
def handle_customer_not_found(error):
    return render_template(
        "customers.html",
        customers=[],
        error_message=str(error),
        status_message=None,
        current_filters=get_current_filters(),
    ), 404


@customer_bp.errorhandler(CustomerDataError)
def handle_customer_data_error(error):
    return render_template(
        "customers.html",
        customers=[],
        error_message=str(error),
        status_message=None,
        current_filters=get_current_filters(),
    ), 500


@customer_bp.errorhandler(Exception)
def handle_customer_unexpected_error(error):
    return render_template(
        "customers.html",
        customers=[],
        error_message="Something went wrong while loading the page.",
        status_message=None,
        current_filters=get_current_filters(),
    ), 500
