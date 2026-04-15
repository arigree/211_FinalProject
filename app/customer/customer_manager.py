from sqlalchemy import asc, desc
from sqlalchemy.exc import SQLAlchemyError

from .customer import Customer
from .customer_exceptions import CustomerDataError, CustomerQueryError


def get_all_customers():
    try:
        return Customer.query.all()
    except SQLAlchemyError as exc:
        raise CustomerDataError("Unable to load customer data right now.") from exc


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
