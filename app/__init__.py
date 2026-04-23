from flask import Flask

from app.rental import rental
from database import DATABASE_URI
from extensions import db

from app.customer import customer_bp
from app.location import location_bp
from app.staff import bp as staff_bp
from app.rental import rental_bp


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    app.register_blueprint(location_bp)
    app.register_blueprint(customer_bp)
    app.register_blueprint(staff_bp)
    app.register_blueprint(rental_bp)

    @app.route("/")
    def home():
        from flask import render_template

        return render_template("home.html")

    return app
