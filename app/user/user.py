# Author: Arissa Green
# Date: 4/27/2026
# File: user.py
# Description:

from datetime import datetime
from flask_login import UserMixin
from sqlalchemy.orm import Mapped
from extensions import db


# inherit from UserMixin to implement is_authenticated, is_active, is_anonymous, and get_id methods
class User(db.Model, UserMixin):
    __tablename__ = 'users'
    # __table_args__ = {'extend_existing': True}

    # Map attributes to table columns
    user_id: Mapped[int] = db.Column(db.Integer, primary_key=True)
    fullname: Mapped[str] = db.Column(db.String(100), nullable=False)
    username: Mapped[str] = db.Column(db.String(50), nullable=False, unique=True)
    password: Mapped[str] = db.Column(db.String(255), nullable=False)
    email: Mapped[str] = db.Column(db.String(100), nullable=False, unique=True)
    role: Mapped[str] = db.Column(db.String(50), nullable=False)

    date_created: Mapped[datetime] = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.now
    )

    def __init__(self, fullname, email, username, password, role):
        self.fullname = fullname
        self.email = email
        self.username = username
        self.password = password
        self.role = role

    def __repr__(self):
        return f'<User {self.fullname}, {self.email}>'

        # This method is required to use flask-login

    def get_id(self):
        return str(self.user_id)
