# Author: Arissa Green
# Date: 4/27/2026
# File: user_controller.py
# Description:


from flask import render_template, request
from .user_manager import UserManager

class UserController:
    # Display the welcome page
    @staticmethod
    def index():
        css_class = request.args.get('css_class', None)
        message = request.args.get('message', None)
        return render_template('user/index.html', css_class=css_class, message=message)

    # display or edit user profile
    @staticmethod
    def profile(user_id):
        css_class = request.args.get('css_class', None)
        message = request.args.get('message', None)
        success, result = UserManager.get_user(user_id)

        if success:
            return render_template('user/profile.html', user=result, css_class=css_class, message=message)
        else:
            return render_template('errors/error.html', error=result)
