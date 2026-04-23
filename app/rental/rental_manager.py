# Author: Arissa Green
# Date: 4/23/2026
# File: rental_manager.py
# Description:

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import or_

from .rental import Rental
from .rental_exceptions import RentalDataError


def get_all_rentals():
    try:
        return Rental.query.all()
    except SQLAlchemyError as exc:
        raise RentalDataError("Unable to load rental data right now.") from exc

def search_rentals(search_text: str):
    try:
        search_text = (search_text or "").strip()

        if not search_text:
            return Rental.query.all()
        terms = [term for term in search_text.split() if term]
        query = Rental.query

        for term in terms:
            pattern = f"%{term}%"
            query = query.filter(
                or_(
                    Rental.rental_status.ilike(pattern),
                    Rental.checkout_date.ilike(pattern),
                    Rental.return_date.ilike(pattern),
                    Rental.checkout_mileage.ilike(pattern),
                    Rental.return_mileage.ilike(pattern)
                )
            )

        results = query.order_by(Rental.rental_status.asc()).limit(20).all()

        if not results:
            raise RentalDataError("No rentals matched your search.")
        return results

    except SQLAlchemyError as exc:
        raise RentalDataError("Unable to load rental data right now.") from exc
