# Author: Arissa Green
# Date: 4/27/2026
# File: auth_manager.py
# Description:

# Author: Arissa Green
# Date: 4/21/2026
# File: auth_manager.py
# Description:

from extensions import db, bcrypt, login_manager
from app.user.user import User
from sqlalchemy import select

class AuthManager:
    @staticmethod
    def register_user(fullname, email, username, password, role):
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        user= User(fullname=fullname, email=email, username=username, password=hashed_password, role=role)

        try:
            db.session.add(user)
            db.session.commit()

            return True, user
        except db.exc.IntegrityError as e:
            db.session.rollback()
            if "Duplicate entry" in str(e):
                return False, f"User {user.username, user.email} is already registered. Choose another username or email."
            else:
                return False, str(e)

    @staticmethod
    def authenticate_user(username, password):
        stmt = select(User).filter_by(username=username)
        user = db.session.scalar(stmt)
        if user and bcrypt.check_password_hash(user.password, password):
            return True, user
        else:
            return False, ""