# Author: Nathaniel Adewara
# Date: 4/9/2026
# File: staff_manager.py
# Description: Define the StaffManager class

from typing import Union

from sqlalchemy import or_, select
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from extensions import db

from .rental import Rental
from .staff import Staff
from .staff_exceptions import *


class StaffManager:
    # Get all staff members
    @staticmethod
    def get_staff() -> list | str:
        try:
            stmt = select(Staff)
            staff_members = db.session.scalars(stmt).all()
            if not staff_members:
                raise StaffNotFoundException("No staff members found")
            return staff_members
        except Exception as e:
            return StaffManager.handle_exceptions(e)

    # Get a staff member by ID
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

    # Search for staff members
    @staticmethod
    def search_staff(search_text: str) -> list | str:
        try:
            search_text = (search_text or "").strip()
            if not search_text:
                return StaffManager.get_staff()

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

    # Create a new staff member
    @staticmethod
    def create_staff(staff_data) -> int | str:
        try:
            required_fields = [
                'first_name',
                'last_name',
                'username',
                'email',
                'role',
                'phone',
                'address'
            ]

            for field in required_fields:
                if not staff_data.get(field):
                    raise InvalidStaffDataException(f"'{field}' is required.")

            new_staff = Staff(
                first_name=staff_data.get('first_name'),
                last_name=staff_data.get('last_name'),
                username=staff_data.get('username'),
                email=staff_data.get('email'),
                role=staff_data.get('role'),
                phone=staff_data.get('phone'),
                address=staff_data.get('address')
            )

            db.session.add(new_staff)
            db.session.commit()

            return new_staff.staff_id

        except IntegrityError:
            db.session.rollback()
            return "Username or email already exists."
        except Exception as e:
            db.session.rollback()
            return StaffManager.handle_exceptions(e)

    # Update staff member details
    @staticmethod
    def update_staff(staff_id, form_data) -> bool | str:
        try:
            stmt = select(Staff).filter_by(staff_id=staff_id)
            staff_member = db.session.scalar(stmt)

            if not staff_member:
                raise StaffNotFoundException(f"The staff id '{staff_id}' could not be found in the database.")

            staff_member.first_name = form_data.get('first_name')
            staff_member.last_name = form_data.get('last_name')
            staff_member.username = form_data.get('username')
            staff_member.email = form_data.get('email')
            staff_member.role = form_data.get('role')
            staff_member.phone = form_data.get('phone')
            staff_member.address = form_data.get('address')

            db.session.commit()
            return True

        except IntegrityError:
            db.session.rollback()
            return "Username or email already exists."
        except Exception as e:
            db.session.rollback()
            return StaffManager.handle_exceptions(e)

    # Delete a staff member
    @staticmethod
    def delete_staff(staff_id) -> bool | str:
        try:
            stmt = select(Staff).filter_by(staff_id=staff_id)
            staff_member = db.session.scalar(stmt)

            if not staff_member:
                raise StaffNotFoundException(f"The staff id '{staff_id}' could not be found in the database.")

            related_rentals = select(Rental).filter_by(staff_id=staff_id)
            rentals = db.session.scalars(related_rentals).all()

            if rentals:
                return "This staff member cannot be deleted because there are rental records connected to them."

            db.session.delete(staff_member)
            db.session.commit()
            return True

        except Exception as e:
            db.session.rollback()
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