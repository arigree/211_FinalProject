# Author: Arissa Green
# Date: 4/27/2026
# File: routes.py
# Description:

# Author: Arissa Green
# Date: 4/21/2026
# File: routes.py
# Description:

from flask_login import login_required

from . import bp
from .auth_controller import AuthController

@bp.route('/register', methods=['GET', 'POST'])
def register():
    return AuthController().register()

@bp.route('/login', methods=['GET', 'POST'])
def login():
    return AuthController.login()

@bp.route('/logout', methods=['POST'])
@login_required
def logout():
    return AuthController.logout()