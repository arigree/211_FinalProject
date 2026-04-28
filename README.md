# Phase 5
___________________
## Team Member Contributions
- Khoutoub: Added Phase 5 session management and route protection across the customer, location, rental, and staff CRUD flows. Updated the app so protected routes redirect unauthenticated users to login with a clear message, and refreshed the home page to reflect login state.
- Arissa: Added the initial authentication foundation with user registration, login, logout, the auth blueprint, the user model, and the related auth/user templates.
- Nathaniel:

## Instructions for Installing Dependencies
- Install dependencies: `pip install -r requirements.txt`
- Start the app: `python3 main.py`
- Open the home page: `http://127.0.0.1:5000/`

## Phase Features Implemented and How to Test Them
- Register a new user at `http://127.0.0.1:5000/auth/register`
- Log in at `http://127.0.0.1:5000/auth/login`
- Visit any protected CRUD route while logged out, such as:
  - `http://127.0.0.1:5000/customers/create`
  - `http://127.0.0.1:5000/locations/add`
  - `http://127.0.0.1:5000/rental/add`
  - `http://127.0.0.1:5000/staff/create`
- Confirm that protected routes redirect to login and show a message for unauthorized access.
- After logging in, revisit those routes and confirm that create, edit, and delete pages load normally.
- Open `http://127.0.0.1:5000/` to confirm the home page changes based on whether a user is logged in or logged out.


## Notes for Instructor and TA
- Phase 5 Member 2 work focuses on session management and route protection. The app uses Flask-Login to preserve logged-in state and applies `@login_required` to create, update, and delete routes across the main domains.

## GitHub
- Repository: https://github.com/arigree/211_FinalProject
