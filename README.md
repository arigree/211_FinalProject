# Car Rental System - Phase 2

## Team Member Contributions

- Khoutoub: completed the vehicle domain for Phase 2, including the model, manager, controller, exceptions file, template, route, and testing.
- Arissa: completed shared setup work for the Flask project structure and GitHub repository setup.
- Nathanial: will complete another project domain and help with integration.

## Instructions for Installing Dependencies

1. Open the project folder in a terminal.
2. Install the required packages:

```bash
pip install -r requirements.txt
```

## Phase 2 Features Implemented and How to Test Them

- The project is connected to the SQLite database `car_rental.db`.
- The vehicle domain has been implemented using Flask Blueprints and Flask-SQLAlchemy.
- The application displays vehicle records from the database on a dynamic web page.

To test the current Phase 2 work:

1. Open the project folder in a terminal.
2. Run the app:

```bash
python3 main.py
```

3. If port 5000 is busy, run:

```bash
python3 -c "from app import create_app; app = create_app(); app.run(debug=True, port=5001)"
```

4. Open the browser and visit:

- `http://127.0.0.1:5000/vehicles`
- or `http://127.0.0.1:5001/vehicles` if using port 5001

The page should display a list of vehicles from the database.

## Notes for Instructor and TA

- This Phase 2 submission currently includes the vehicle domain.
- The project uses MVC structure, Flask Blueprints, Flask-SQLAlchemy, and exception handling for the vehicle page.
- The team is continuing to add the remaining domains required for the full Phase 2 project.
