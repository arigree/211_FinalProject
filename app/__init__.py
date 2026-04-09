from flask import Flask

from database import DATABASE_URI
from extensions import db
from app.customer import customer_bp
from app.staff import bp as staff_bp

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    app.register_blueprint(customer_bp)
    app.register_blueprint(staff_bp)

    @app.route("/")
    def home():
        return (
            "<h1>Car Rental System</h1>"
            '<p>This page links to the customer list for Phase 2.</p>'
            '<p><a href="/customers">Go to Customers</a></p>'
        )

    return app
