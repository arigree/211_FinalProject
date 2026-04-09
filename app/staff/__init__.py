# Author: Nathaniel Adewara
# Date: 4/8/2026
# File: __init__.py
# Description:
from flask import Blueprint

bp = Blueprint('staff', __name__, url_prefix='/staff',
               static_folder='static', template_folder='templates')
