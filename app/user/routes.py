# Author: Arissa Green
# Date: 4/27/2026
# File: routes.py
# Description:

from flask_login import login_required

from .user_controller import UserController
from . import bp

# user welcome page
@bp.route('/')
@bp.route('/index')
def index():
    return UserController.index()

# display user profile
@bp.route('/<int:user_id>')
@bp.route('/<int:user_id>/profile')
@login_required
def profile(user_id):
    return UserController.profile(user_id)
