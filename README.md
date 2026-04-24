# Phase 4
___________________
## Team Member Contributions
- Khoutoub: Phase 3 customer filtering, sorting, and limiting; Phase 4 customer create, update, and delete
- Arissa: Location and rental CRUD applications. Rental MVC domain creation, search functionality creation. Exception handling adjustments
- Nathaniel: Staff CRUD applications, rental testing

## Instructions for Installing Dependencies
- Install dependencies: `pip install -r requirements.txt`
- Start the app: `python3 main.py`
- Open the home page: `http://127.0.0.1:5000/`

## Phase Features Implemented and How to Test Them
- Customer domain
  - Create customer: `http://127.0.0.1:5000/customers/create`
  - Update customer: open `http://127.0.0.1:5000/customers` and select `Edit`
  - Delete customer: open `http://127.0.0.1:5000/customers` and select `Delete`
- Staff domain
  - Create staff: `http://127.0.0.1:5000/staff/create`
  - Update staff: `http://127.0.0.1:5000/staff` and select `Edit`
  - Delete staff: `http://127.0.0.1:5000/staff` and select `Delete`
- Location domain
  - Create location: `http://127.0.0.1:5000/locations/create`
  - Update location: `http://127.0.0.1:5000/locations` and select `Edit`
  - Delete location: `http://127.0.0.1:5000/locations` and select `Delete`
- Rental Domain
  - Create rental: `http://127.0.0.1:5000/rental/create`
  - Update Rental:`http://127.0.0.1:5000/rental` and select `Edit`
  - Delete rental: `http://127.0.0.1:5000/rental` and select `Delete`

## Notes for Instructor and TA
- The exception handling and MVC for rentals is now added, please let us know if it does not meet requirements.

## GitHub
- Repository: https://github.com/arigree/211_FinalProject
