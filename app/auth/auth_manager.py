# Author: Arissa Green
# Date: 4/27/2026
# File: auth_manager.py
# Description:

# Author: Arissa Green
# Date: 4/21/2026
# File: auth_manager.py
# Description:

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from app.user.user import User
from extensions import bcrypt, db

class AuthManager:
    @staticmethod
    def register_user(fullname, email, username, password, role):
        hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")

        user = User(
            fullname=fullname,
            email=email,
            username=username,
            password=hashed_password,
            role=role,
        )

        try:
            db.session.add(user)
            db.session.commit()

            return True, user
        except IntegrityError as e:
            db.session.rollback()

            if "users.username" in str(e.orig):
                return False, "That username is already in use. Choose another username."

            if "users.email" in str(e.orig):
                return False, "That email is already in use. Choose another email."

            return False, "We could not create your account right now."

    @staticmethod
    def authenticate_user(username, password):
        stmt = select(User).filter_by(username=username)
        user = db.session.scalar(stmt)

        if user and bcrypt.check_password_hash(user.password, password):
            return True, user

        return False, ""
