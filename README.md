# Car Rental System - Phase 3

This project is a Flask car rental system for INFO-I 211.

### Team Member Contributions
- Filtering, Sorting, and Limiting on Customer Domain - Khoutoub

### Instructions for Installing Dependencies
- In the terminal, type: `pip install -r requirements.txt`

### Phase 3 Feature Completed So Far
- Member 1 feature completed on the Customer domain
- Filtering by city
- Filtering by phone area code
- Sorting by customer ID, first name, or last name
- Sorting in ascending or descending order
- Limiting the number of results returned
- User-friendly validation for invalid query input

### How to Test Khoutoub's Phase 3 Work
- Start the application with: `python3 main.py`
- Open the home page: `http://127.0.0.1:5000/`
- Open the customer page: `http://127.0.0.1:5000/customers`
- Test filtering by city: `http://127.0.0.1:5000/customers?city=Indianapolis`
- Test sorting: `http://127.0.0.1:5000/customers?area_code=317&sort_by=last_name&order=desc`
- Test filtering, sorting, and limiting together: `http://127.0.0.1:5000/customers?city=Indianapolis&area_code=317&sort_by=first_name&order=asc&limit=2`
- Test invalid input handling: `http://127.0.0.1:5000/customers?limit=0`

### Current Project Status
- Routing with Flask and Blueprints
- Pages to display data for the independent entities (Customer, location, and staff)
- Customer filtering, sorting, and limiting are implemented
- Other Phase 3 features will be added by the remaining team members

- [GitHub]('https://github.com/arigree/211_FinalProject')

### Notes for Instructor and TA
- This README currently documents only Khoutoub's completed Phase 3 contribution.
- The customer feature was implemented across routes, controller, manager, template, and exception handling layers.
