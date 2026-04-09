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
            return render_template('errors/404.html', error=result)
        else:
            return render_template('staff/index.html', staff_members=result)

    @staticmethod
    def detail(staff_id: int):
        result = StaffManager.get_staff_member(staff_id)
        if isinstance(result, str):
            return render_template('errors/404.html', error=result)
        else:
            return render_template('staff/detail.html', staff=result)