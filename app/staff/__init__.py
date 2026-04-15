# Author: Nathaniel Adewara
# Date: 4/8/2026
# File: __init__.py
# Description:
from flask import Blueprint
from .staff_controller import StaffController

bp = Blueprint('staff', __name__, url_prefix='/staff',
               static_folder='static', template_folder='templates')

@bp.route("/")
def index():
    return StaffController.index()

@bp.route("/<int:staff_id>")
def detail(staff_id):
    return StaffController.detail(staff_id)

@bp.route("/search")
def search():
    return StaffController.search()