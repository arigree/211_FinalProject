# Author: Arissa Green
# Date: 4/27/2026
# File: __init__.py
# Description:

from flask import Blueprint
from . import auth_tools

bp = Blueprint("auth", __name__, url_prefix="/auth", static_folder="static", template_folder="templates")

from . import routes