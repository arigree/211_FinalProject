# Author: Arissa Green
# Date: 4/27/2026
# File: auth_tools.py
# Description:

# Author: Arissa Green
# Date: 4/21/2026
# File: auth_tools.py
# Description:
from functools import wraps
from flask_login import current_user
from flask import redirect, url_for, request

from extensions import db, login_manager
from sqlalchemy import select
from app.user.user import User
@login_manager.user_loader
def load_user(user_id):
    return db.session.scalar(select(User).filter_by(user_id=user_id))

@login_manager.unauthorized_handler
def unauthorized_callback():
    message = 'You are not authorized to view this page. Please login first.'
    return redirect(url_for('auth.login', next=request.path, css_class='warning', message=message))

# define custom decorator for RBAC
def role_required(*roles):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not current_user.is_authenticated or current_user.role.lower() not in [role.lower() for role in roles]:
                message = "You don't have permission to access this page."
                css_class = "danger"
                return redirect(url_for("auth.login", css_class=css_class, message=message))
            return func(*args, **kwargs)
        return wrapper
    return decorator