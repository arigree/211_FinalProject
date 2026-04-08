from sqlalchemy.exc import SQLAlchemyError

from .customer import Customer
from .customer_exceptions import CustomerDataError


def get_all_customers():
    try:
        return Customer.query.all()
    except SQLAlchemyError as exc:
        raise CustomerDataError("Unable to load customer data right now.") from exc
