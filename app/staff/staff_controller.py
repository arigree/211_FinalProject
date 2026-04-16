# Author: Nathaniel Adewara
# Date: 4/9/2026
# File: staff_controller.py
# Description: Define the staff controller class

from flask import render_template, request
from .staff_manager import StaffManager

class StaffController:
    @staticmethod
    def index():
        result = StaffManager.get_staff_members()
        if isinstance(result, str):
            return render_template("index.html", error=result, staff_members=[])
        return render_template("index.html", staff_members=result, error=None)

    # Display a staff member's details
    @staticmethod
    def detail(staff_id: int):
        result = StaffManager.get_staff_member(staff_id)
        if isinstance(result, str):
            return render_template("detail.html", error=result, staff=None)
        return render_template("detail.html", staff=result, error=None)

    # Display a staff member's rentals
    @staticmethod
    def rentals(staff_id):
        result = StaffManager.get_staff_rentals(staff_id)
        if isinstance(result, str):
            return render_template("staff_rentals.html", staff=None, error=result)
        staff_member, rentals = result
        return render_template("staff_rentals.html", staff=staff_member, rentals=rentals)

    # Search for staff members
    @staticmethod
    def search():
        q = request.args.get("q", "")
        result = StaffManager.search_staff_members(q)

        if isinstance(result, str):
            return render_template("index.html", error=result, staff_members=[], query=q)

        return render_template("index.html", staff_members=result, error=None, query=q)