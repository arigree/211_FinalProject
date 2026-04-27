# Author: Arissa Green
# Date: 4/27/2026
# File: user_manager.py
# Description:

from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from extensions import db
from .user import User

class UserManager:
    @staticmethod
    def get_user(user_id):
        try:
            stmt = select(User).filter_by(user_id=user_id)
            user = db.session.scalar(stmt)
            if user:
                return True, user
            else:
                return False, f"User with ID {user_id} was not found."
        except SQLAlchemyError as e:
            db.session.rollback()
            return False, f"An database error occurred: {str(e.__dict__['orig'])}."
        except Exception as e:
            db.session.rollback()
            return False, f"An unexpected error occurred: {str(e.__dict__['orig'])}"
