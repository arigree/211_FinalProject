# Author: Nathaniel Adewara
# Date: 4/9/2026
# File: staff_controller.py
# Description: Define the staff controller class
from flask import render_template
from .staff_manager import StaffManager


class StaffController:
    # list all the staff members
    @staticmethod
    def index():
        result = StaffManager.get_staff_members()
        if isinstance(result, str):
            return render_template('index.html', error=result, staff_members=[])
        return render_template('index.html', staff_members=result, error = None)

    @staticmethod
    def detail(staff_id: int):
        result = StaffManager.get_staff_member(staff_id)
        if isinstance(result, str):
            return render_template('detail.html', error=result, staff=None)
        return render_template('detail.html', staff=result, error=None)
