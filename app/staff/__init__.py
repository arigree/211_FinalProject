# Author: Nathaniel Adewara
# Date: 4/8/2026
# File: __init__.py
# Description: Define the staff blueprint
from flask import Blueprint
from .staff_controller import StaffController

bp = Blueprint('staff', __name__, url_prefix='/staff',
               static_folder='static', template_folder='templates')

# Define the routes for the staff blueprint
@bp.route("/")
def index():
    return StaffController.index()

# Define the route for the staff detail page
@bp.route("/<int:staff_id>")
def detail(staff_id):
    return StaffController.detail(staff_id)

# Define the route for the staff rentals page
@bp.route("/<int:staff_id>/rentals")
def rentals(staff_id):
    return StaffController.rentals(staff_id)

# Define the route for the staff search page
@bp.route("/search")
def search():
    return StaffController.search()

# Define the route for the staff create page
@bp.route("/create", methods=["GET", "POST"])
def create():
    return StaffController.create()

# Define the route for the staff edit page
@bp.route("/<int:staff_id>/edit", methods=["GET", "POST"])
def edit(staff_id):
    return StaffController.edit(staff_id)

# Define the route for the staff delete page
@bp.route("/<int:staff_id>/delete", methods=["GET", "POST"])
def delete(staff_id):
    return StaffController.delete(staff_id)
