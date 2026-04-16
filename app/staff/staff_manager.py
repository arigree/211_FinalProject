# Author: Nathaniel Adewara
# Date: 4/9/2026
# File: staff_manager.py
# Description: Define the StaffManager class


from typing import Union
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select, or_
from extensions import db
from .staff import Staff
from .rental import Rental
from .staff_exceptions import *

# Staff Manager Class
class StaffManager:
    @staticmethod
    def get_staff_members() -> list | str:
        try:
            stmt = select(Staff)
            staff_members = db.session.scalars(stmt).all()
            if not staff_members:
                raise StaffNotFoundException("No staff members found")
            return staff_members
        except Exception as e:
            return StaffManager.handle_exceptions(e)

    # Get staff member by ID
    @staticmethod
    def get_staff_member(staff_id: int) -> Union[Staff, str]:
        try:
            stmt = select(Staff).filter_by(staff_id=staff_id)
            staff_member = db.session.scalar(stmt)
            if not staff_member:
                raise StaffNotFoundException(f"Staff member with ID {staff_id} not found")
            return staff_member
        except Exception as e:
            return StaffManager.handle_exceptions(e)

    # Search staff members
    @staticmethod
    def search_staff_members(search_text: str) -> list | str:
        try:
            search_text = (search_text or "").strip()
            if not search_text:
                return StaffManager.get_staff_members()

            terms = [term for term in search_text.split() if term]
            stmt = select(Staff)

            for term in terms:
                pattern = f"%{term}%"
                stmt = stmt.where(
                    or_(
                        Staff.first_name.ilike(pattern),
                        Staff.last_name.ilike(pattern),
                        Staff.username.ilike(pattern),
                        Staff.email.ilike(pattern),
                        Staff.role.ilike(pattern),
                        Staff.phone.ilike(pattern),
                        Staff.address.ilike(pattern),
                    )
                )

            stmt = stmt.order_by(Staff.last_name.asc(), Staff.first_name.asc()).limit(20)
            results = db.session.scalars(stmt).all()

            if not results:
                raise StaffNotFoundException("No staff members matched your search")

            return results

        except Exception as e:
            return StaffManager.handle_exceptions(e)

    # Get staff member rentals
    @staticmethod
    def get_staff_rentals(staff_id: int):
        try:
            staff_member = db.session.get(Staff, staff_id)
            if not staff_member:
                raise StaffNotFoundException(f"Staff member with ID {staff_id} not found")

            rentals = (
                db.session.query(Rental)
                .filter(Rental.staff_id == staff_id)
                .order_by(Rental.checkout_date.desc())
                .all()
            )

            return staff_member, rentals

        except Exception as e:
            return StaffManager.handle_exceptions(e)

    # Handle exceptions
    @staticmethod
    def handle_exceptions(exception):
        db.session.rollback()
        orig_error = getattr(exception, "orig", "")
        if isinstance(exception, StaffNotFoundException):
            return str(exception)
        elif isinstance(exception, SQLAlchemyError):
            return f"Database error: {str(orig_error)}"
        else:
            return f"An unexpected error has occurred: {str(exception)}"