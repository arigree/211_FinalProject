# Author: Arissa Green
# Date: 4/27/2026
# File: __init__.py
# Description:

from flask import Blueprint

bp = Blueprint('user', __name__, url_prefix="/users", static_folder="static", template_folder='templates')

from . import routes