# Author: Nathaniel Adewara
# Date: 4/9/2026
# File: staff_exceptions.py
# Description: Define exceptions for the staff module

class StaffException(Exception):
    """Base exception class for staff-specific exceptions."""
    pass


class StaffNotFoundException(StaffException):
    """Exception raised when a staff member is not found in the database."""
    pass


class InvalidStaffDataException(StaffException):
    """Exception raised when staff data is not valid."""
    pass