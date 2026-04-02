from flask import Flask

from models import DATABASE_NAME, get_connection

app = Flask(__name__)


@app.route("/")
def home():
    connection = get_connection()

    table_counts = {}
    tables = ["Customer", "Staff", "Location", "Vehicle", "Rental", "Payment"]

    try:
        for table_name in tables:
            result = connection.execute(
                f"SELECT COUNT(*) AS count FROM {table_name}"
            ).fetchone()
            table_counts[table_name] = result["count"]
    finally:
        connection.close()

    return (
        "<h1>Car Rental System Database Setup Complete</h1>"
        f"<p>Connected to <strong>{DATABASE_NAME}</strong>.</p>"
        "<ul>"
        f"<li>Customers: {table_counts['Customer']}</li>"
        f"<li>Staff: {table_counts['Staff']}</li>"
        f"<li>Locations: {table_counts['Location']}</li>"
        f"<li>Vehicles: {table_counts['Vehicle']}</li>"
        f"<li>Rentals: {table_counts['Rental']}</li>"
        f"<li>Payments: {table_counts['Payment']}</li>"
        "</ul>"
    )


if __name__ == "__main__":
    app.run(debug=True)
