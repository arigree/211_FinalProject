from flask import Flask

from database import DATABASE_URI
from extensions import db
from app.vehicle import vehicle_bp


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    app.register_blueprint(vehicle_bp)

    @app.route("/")
    def home():
        return (
            "<h1>Car Rental System</h1>"
            '<p>Phase 2 Vehicle domain is ready.</p>'
            '<p><a href="/vehicles">View Vehicles</a></p>'
        )

    return app
