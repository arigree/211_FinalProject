from flask import Flask

from database import DATABASE_URI
from extensions import bcrypt, db, login_manager

from app.auth import bp as auth_bp
from app.customer import customer_bp
from app.location import location_bp
from app.rental import rental_bp
from app.staff import bp as staff_bp
from app.user import bp as user_bp

def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = "i211 rental final"
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SESSION_COOKIE_HTTPONLY"] = True
    app.config["SESSION_COOKIE_SAMESITE"] = "Lax"
    app.config["REMEMBER_COOKIE_HTTPONLY"] = True
    app.config["REMEMBER_COOKIE_SAMESITE"] = "Lax"

    db.init_app(app)
    bcrypt.init_app(app)

    login_manager.init_app(app)
    login_manager.login_view = "auth.login"
    login_manager.login_message = None

    app.register_blueprint(location_bp)
    app.register_blueprint(customer_bp)
    app.register_blueprint(staff_bp)
    app.register_blueprint(rental_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(auth_bp)

    @app.route("/")
    def home():
        from flask import render_template

        return render_template("home.html")

    return app
