# Car Rental System - Phase 2

This project is a Flask car rental system for INFO-I 211. For Phase 2, our team set up the app structure, connected the project to SQLite, and added a customer page that displays data from the database.

## Team Contributions

- Khoutoub worked on the customer domain.
- Arissa worked on the shared Flask setup and GitHub setup.
- Nathanial is helping with the other domain work and integration.

## Current Phase 2 Work

- Flask app structure with Blueprints
- SQLite database connection
- Customer model, manager, controller, template, and exceptions
- Customer list page at `/customers`

## Running the Project

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the app:

```bash
python3 main.py
```

If port 5000 is already in use, run:

```bash
python3 -c "from app import create_app; app = create_app(); app.run(debug=True, port=5001)"
```

Then open:

- `http://127.0.0.1:5000/customers`
- or `http://127.0.0.1:5001/customers`
