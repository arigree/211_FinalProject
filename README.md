# Car Rental System

This project is a Flask car rental system for INFO-I 211. The application uses Flask blueprints and Flask-SQLAlchemy models organized by domain.

## Team Member Contributions
- Khoutoub: Phase 3 customer filtering, sorting, and limiting; Phase 4 customer create, update, and delete
- Arissa: location and search features
- Nathaniel: staff and ORM relationship features

## Install and Run
- Install dependencies: `pip install -r requirements.txt`
- Start the app: `python3 main.py`
- Open the home page: `http://127.0.0.1:5000/`

## Phase 3 Note
- Customer filtering, sorting, and limiting are available at `http://127.0.0.1:5000/customers`
- The ORM relationships for the staff rentals feature are defined in `app/staff/staff.py` and `app/customer/customer.py`
- Related rental data are modeled in `app/staff/rental.py`
- The related data retrieved on the staff rentals page include the selected staff member's rentals plus each rental's related customer name

## Phase 4 Member 1 Work
- Domain 1 is the customer domain
- Create customer: `http://127.0.0.1:5000/customers/create`
- Update customer: open `http://127.0.0.1:5000/customers` and select `Edit`
- Delete customer: open `http://127.0.0.1:5000/customers` and select `Delete`

## Customer CRUD Features
- Create uses ORM `db.session.add()` and `db.session.commit()`
- Update loads a customer record, changes model attributes, and commits with ORM
- Delete loads a customer record, checks for related rentals, then uses ORM delete and commit
- Forms and templates are provided for create, update, and delete confirmation
- Validation handles empty fields, invalid email addresses, duplicate unique values, missing records, and blocked deletes

## GitHub
- Repository: https://github.com/arigree/211_FinalProject
