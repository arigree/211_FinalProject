# Author: Arissa Green
# Date: 4/27/2026
# File: auth_controller.py
# Description:

from flask import redirect, render_template, request, url_for
from flask_login import login_user, logout_user

from .auth_manager import AuthManager


class AuthController:
    @staticmethod
    def register():
        if request.method == "GET":
            return render_template("auth/register.html")

        if request.method == "POST":
            fullname = request.form["fullname"].strip()
            email = request.form["email"].strip()
            username = request.form["username"].strip()
            password = request.form["password"]
            role = "User"

            success, result = AuthManager.register_user(fullname, email, username, password, role)
            if success:
                login_user(result)

                message = "You are now registered!"
                return redirect(
                    url_for(
                        "user.profile",
                        user_id=result.user_id,
                        css_class="success",
                        message=message,
                    )
                )

            return render_template(
                "auth/register.html",
                user=request.form,
                css_class="error",
                message=result,
            )


    @staticmethod
    def login():
        if request.method == "POST":
            username = request.form["username"].strip()
            password = request.form["password"]
            success, user = AuthManager.authenticate_user(username, password)
            if success:
                login_user(user)
                next_page = request.args.get("next")
                message = "You are now logged in!"
                return redirect(
                    next_page
                    or url_for(
                        "home",
                        user_id=user.user_id,
                        css_class="success",
                        message=message,
                    )
                )

            message = "Invalid username or password."
            return render_template(
                "auth/login.html",
                css_class="error",
                message=message,
            ), 401

        css_class = request.args.get("css_class")
        message = request.args.get("message")
        return render_template("auth/login.html", css_class=css_class, message=message)

    @staticmethod
    def logout():
        if request.method == "POST":
            logout_user()
            message = "Thank you for your visit, you are now logged out!"
            return redirect(url_for("home", css_class="success", message=message))

        return render_template("auth/logout.html")
