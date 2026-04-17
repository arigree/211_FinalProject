# Car Rental System — Phase 3

## Team Member Contributions
- Filtering, Sorting, and Limiting on Customer Domain - Khoutoub
- Searching Functionality - Arissa
- Querying Related Data (ORM Relationships) - Nathaniel

## Instructions for Installing Dependencies
- In the terminal, type: `pip install -r requirements.txt`

## Phase 3 Features Implemented and How to Test Them (Include URLs)
- Start the application with: `python3 main.py`
- Open the home page: `http://127.0.0.1:5000/`
_______________________
### Filtering, Sorting, and Limiting on Customer Domain
- Open the customer page: `http://127.0.0.1:5000/customers`
- Test filtering by city: `http://127.0.0.1:5000/customers?city=Indianapolis`
- Test sorting: `http://127.0.0.1:5000/customers?area_code=317&sort_by=last_name&order=desc`
- Test filtering, sorting, and limiting together: `http://127.0.0.1:5000/customers?city=Indianapolis&area_code=317&sort_by=first_name&order=asc&limit=2`
- Test invalid input handling: `http://127.0.0.1:5000/customers?limit=0`

### Searching Functionality
- Open the location page: `http://127.0.0.1:5000/locations`
- Enter a location name, or other detail, into the search bar
- Select 'Search' or hit enter
- To clear a search query, hit the clear button or backspace your text and hit enter

### Querying Related Data (ORM Relationships)
- Open the staff page: `http://127.0.0.1:5000/staff`
- Select any staff member to view their details
- Click "View Rentals" to access related rental data
- This page displays all rentals handled by the selected staff member
- Each rental also shows related customer information retrieved through ORM relationships


## Notes for Instructor and TA
- Styling across pages will be implemented in the final product