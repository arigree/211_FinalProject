# Author: Nathaniel Adewara
# Date: 4/9/2026
# File: staff_exceptions.py
# Description: Define exceptions for the staff module
class StaffException(Exception):
    pass


class StaffNotFoundException(StaffException):
    pass


class InvalidStaffDataException(StaffException):
    pass