# Author: Nathaniel Adewara
# Date: 4/9/2026
# File: staff_manager.py
# Description: Define the StaffManager class
from typing import Union
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select
from extensions import db
from .staff import Staff
from .staff_exceptions import *


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

    @staticmethod
    def handle_exceptions(exception):
        db.session.rollback()
        orig_error = getattr(exception, 'orig', "")
        if isinstance(exception, StaffNotFoundException):
            return str(exception)
        elif isinstance(exception, SQLAlchemyError):
            return f"Database error: {str(orig_error)}"
        else:
            return f"An unexpected error has occurred: {str(exception)}"