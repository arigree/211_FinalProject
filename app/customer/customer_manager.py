import re

from sqlalchemy import asc, desc
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from extensions import db

from .customer import Customer
from .customer_exceptions import (
    CustomerDataError,
    CustomerNotFoundError,
    CustomerOperationError,
    CustomerQueryError,
    CustomerValidationError,
)


EMAIL_PATTERN = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

class CustomerManager:

    @staticmethod
    def _normalize_customer_data(form_data):
        normalized_data = {
            "first_name": form_data.get("first_name", "").strip(),
            "last_name": form_data.get("last_name", "").strip(),
            "phone": form_data.get("phone", "").strip(),
            "email": form_data.get("email", "").strip(),
            "driver_license_number": form_data.get("driver_license_number", "").strip(),
            "address": form_data.get("address", "").strip(),
        }

        missing_fields = [
            label
            for key, label in (
                ("first_name", "First name"),
                ("last_name", "Last name"),
                ("phone", "Phone"),
                ("email", "Email"),
                ("driver_license_number", "Driver license number"),
                ("address", "Address"),
            )
            if not normalized_data[key]
        ]

        if missing_fields:
            raise CustomerValidationError(f"{', '.join(missing_fields)} must not be empty.")

        if not EMAIL_PATTERN.match(normalized_data["email"]):
            raise CustomerValidationError("Enter a valid email address.")

        return normalized_data

    @staticmethod
    def get_all_customers():
        try:
            return Customer.query.all()
        except SQLAlchemyError as exc:
            raise CustomerDataError("Unable to load customer data right now.") from exc

    @staticmethod
    def get_filtered_customers(city="", area_code="", sort_by="customer_id", order="asc", limit=""):
        sort_options = {
            "customer_id": Customer.customer_id,
            "first_name": Customer.first_name,
            "last_name": Customer.last_name,
        }
        allowed_orders = {"asc", "desc"}

        normalized_city = city.strip()
        normalized_area_code = area_code.strip()
        normalized_sort = sort_by.strip() or "customer_id"
        normalized_order = order.strip().lower() or "asc"
        normalized_limit = limit.strip()

        if normalized_sort not in sort_options:
            raise CustomerQueryError("Choose a valid field to sort customers by.")

        if normalized_order not in allowed_orders:
            raise CustomerQueryError("Choose a valid sort order.")

        limit_value = None
        if normalized_limit:
            try:
                limit_value = int(normalized_limit)
            except ValueError as exc:
                raise CustomerQueryError("Limit must be a whole number.") from exc

            if limit_value <= 0:
                raise CustomerQueryError("Limit must be greater than zero.")

        try:
            query = Customer.query

            if normalized_city:
                query = query.filter(Customer.address.ilike(f"%{normalized_city}%"))

            if normalized_area_code:
                query = query.filter(Customer.phone.like(f"{normalized_area_code}%"))

            sort_column = sort_options[normalized_sort]
            query = query.order_by(desc(sort_column) if normalized_order == "desc" else asc(sort_column))

            if limit_value is not None:
                query = query.limit(limit_value)

            return query.all()
        except SQLAlchemyError as exc:
            raise CustomerDataError("Unable to load customer data right now.") from exc

    @staticmethod
    def get_customer_by_id(customer_id):
        try:
            customer = db.session.get(Customer, customer_id)
        except SQLAlchemyError as exc:
            raise CustomerDataError("Unable to load customer data right now.") from exc

        if customer is None:
            raise CustomerNotFoundError(f"Customer with ID {customer_id} was not found.")

        return customer

    @staticmethod
    def create_customer(form_data):
        normalized_data = CustomerManager._normalize_customer_data(form_data)

        try:
            customer = Customer(**normalized_data)
            db.session.add(customer)
            db.session.commit()
            return customer
        except IntegrityError as exc:
            db.session.rollback()
            raise CustomerValidationError(
                "Email and driver license number must both be unique."
            ) from exc
        except SQLAlchemyError as exc:
            db.session.rollback()
            raise CustomerOperationError("Unable to create the customer right now.") from exc

    @staticmethod
    def update_customer(customer_id, form_data):
        normalized_data = CustomerManager._normalize_customer_data(form_data)
        customer = CustomerManager.get_customer_by_id(customer_id)

        try:
            for field_name, value in normalized_data.items():
                setattr(customer, field_name, value)

            db.session.commit()
            return customer
        except IntegrityError as exc:
            db.session.rollback()
            raise CustomerValidationError(
                "Email and driver license number must both be unique."
            ) from exc
        except SQLAlchemyError as exc:
            db.session.rollback()
            raise CustomerOperationError("Unable to update the customer right now.") from exc

    @staticmethod
    def delete_customer(customer_id):
        customer = CustomerManager.get_customer_by_id(customer_id)

        if customer.rentals:
            raise CustomerOperationError(
                "This customer cannot be deleted because related rental records still exist."
            )

        try:
            db.session.delete(customer)
            db.session.commit()
        except SQLAlchemyError as exc:
            db.session.rollback()
            raise CustomerOperationError("Unable to delete the customer right now.") from exc

    @staticmethod
    def handle_exceptions(exception):
        db.session.rollback()
        orig_error = exception.__dict__.get('orig', "")
        if isinstance(exception, (CustomerDataError)):
            return exception.__str__()
        elif isinstance(exception, SQLAlchemyError):
            return f"An database error occurred: {str(orig_error)}."
        else:
            return f"An unexpected error occurred: {str(orig_error)}"