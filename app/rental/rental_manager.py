# Author: Arissa Green
# Date: 4/23/2026
# File: rental_manager.py
# Description:

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import or_

from extensions import db
from .rental import Rental
from .rental_exceptions import RentalDataError

class RentalManager:

    @staticmethod
    def get_all_rentals():
        try:
            return Rental.query.all()
        except SQLAlchemyError as exc:
            raise RentalDataError("Unable to load rental data right now.") from exc

    @staticmethod
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

    @staticmethod
    def create_rental(data):
        try:
            rental = Rental(**data)
            db.session.add(rental)
            db.session.commit()
            return rental
        except SQLAlchemyError as exc:
            db.session.rollback()
            print(exc)
            raise RentalDataError("Unable to create rental.") from exc

    @staticmethod
    def update_rental(rental_id, data):
        try:
            rental = Rental.query.get(rental_id)

            if not rental:
                raise RentalDataError("Rental not found.")

            for key, value in data.items():
                setattr(rental, key, value)

            db.session.commit()
            return rental

        except SQLAlchemyError as exc:
            db.session.rollback()
            print(exc)
            raise RentalDataError("Unable to update rental.") from exc

    @staticmethod
    def delete_rental(rental_id):
        try:
            rental = Rental.query.get(rental_id)

            if not rental:
                raise RentalDataError("Rental not found.")

            db.session.delete(rental)
            db.session.commit()

        except SQLAlchemyError as exc:
            db.session.rollback()
            print(exc)
            raise RentalDataError("Unable to delete rental.") from exc
