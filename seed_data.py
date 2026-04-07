from models import create_tables, get_connection


LOCATIONS = [
    ("Downtown Branch", "Indianapolis", "IN", "317-555-1001"),
    ("Airport Branch", "Indianapolis", "IN", "317-555-1002"),
    ("North Side Branch", "Carmel", "IN", "317-555-1003"),
    ("West Side Branch", "Plainfield", "IN", "317-555-1004"),
    ("Bloomington Branch", "Bloomington", "IN", "812-555-1005"),
]

CUSTOMERS = [
    (
        "Maya",
        "Patel",
        "317-555-2101",
        "maya.patel@email.com",
        "INP1234567",
        "245 Maple St, Indianapolis, IN",
    ),
    (
        "Jordan",
        "Lee",
        "317-555-2102",
        "jordan.lee@email.com",
        "INL2345678",
        "18 Oak Ave, Carmel, IN",
    ),
    (
        "Avery",
        "Smith",
        "812-555-2103",
        "avery.smith@email.com",
        "INS3456789",
        "77 College Mall Rd, Bloomington, IN",
    ),
    (
        "Daniel",
        "Garcia",
        "463-555-2104",
        "daniel.garcia@email.com",
        "ING4567890",
        "902 River Rd, Plainfield, IN",
    ),
    (
        "Chloe",
        "Nguyen",
        "317-555-2105",
        "chloe.nguyen@email.com",
        "INN5678901",
        "601 Walnut St, Indianapolis, IN",
    ),
]

VEHICLES = [
    (
        "1HGBH41JXMN109186",
        "Toyota",
        "Camry",
        2022,
        "Silver",
        "IND-2451",
        28450,
        54.99,
        "Available",
        1,
    ),
    (
        "2FTRX18W1XCA34567",
        "Honda",
        "Civic",
        2021,
        "Black",
        "IND-3892",
        31220,
        49.99,
        "Available",
        2,
    ),
    (
        "3CZRE4H59BG701234",
        "Ford",
        "Escape",
        2023,
        "Blue",
        "CAR-1184",
        19870,
        64.99,
        "Rented",
        3,
    ),
    (
        "4T1BF1FK7GU567890",
        "Chevrolet",
        "Malibu",
        2020,
        "White",
        "PLN-5572",
        40510,
        47.50,
        "Maintenance",
        4,
    ),
    (
        "5NPE24AF4FH246810",
        "Nissan",
        "Altima",
        2022,
        "Red",
        "BLM-9033",
        25640,
        52.75,
        "Available",
        5,
    ),
]

STAFF_MEMBERS = [
    (
        "Emily",
        "Carter",
        "ecarter",
        "emily.carter@carrental.com",
        "Manager",
        "317-555-3101",
        "410 Meridian St, Indianapolis, IN",
    ),
    (
        "Marcus",
        "Reed",
        "mreed",
        "marcus.reed@carrental.com",
        "Rental Agent",
        "317-555-3102",
        "92 Pine St, Carmel, IN",
    ),
    (
        "Sofia",
        "Lopez",
        "slopez",
        "sofia.lopez@carrental.com",
        "Rental Agent",
        "812-555-3103",
        "55 Grant St, Bloomington, IN",
    ),
    (
        "Tyler",
        "Brooks",
        "tbrooks",
        "tyler.brooks@carrental.com",
        "Customer Support",
        "463-555-3104",
        "711 Center St, Plainfield, IN",
    ),
    (
        "Hannah",
        "Kim",
        "hkim",
        "hannah.kim@carrental.com",
        "Supervisor",
        "317-555-3105",
        "28 Cedar Dr, Indianapolis, IN",
    ),
]

RESERVATIONS = [
    (1, 2, "2026-03-18", "2026-03-20", "2026-03-23", "Confirmed", 149.97),
    (2, 4, "2026-03-19", "2026-03-22", "2026-03-24", "Pending", 95.00),
    (3, 5, "2026-03-20", "2026-03-25", "2026-03-28", "Confirmed", 158.25),
    (4, 1, "2026-03-21", "2026-03-26", "2026-03-27", "Completed", 109.98),
    (5, 3, "2026-03-22", "2026-03-29", "2026-03-31", "Confirmed", 129.98),
]

RENTALS = [
    (1, 1, 1, "2026-03-01", "2026-03-04", "2026-03-04", 28450, 28710, "Completed", 164.97),
    (2, 2, 2, "2026-03-05", "2026-03-08", "2026-03-08", 31220, 31405, "Completed", 149.97),
    (3, 3, 3, "2026-03-10", "2026-03-13", None, 19870, None, "Active", 194.97),
    (4, 5, 4, "2026-03-12", "2026-03-14", "2026-03-14", 25640, 25900, "Completed", 105.50),
    (5, 1, 5, "2026-03-15", "2026-03-17", "2026-03-17", 28710, 28860, "Completed", 109.98),
]

PAYMENTS = [
    (1, "2026-03-01", 164.97, "Credit Card", "Paid"),
    (2, "2026-03-05", 149.97, "Debit Card", "Paid"),
    (3, "2026-03-10", 100.00, "Credit Card", "Partial"),
    (4, "2026-03-12", 105.50, "Cash", "Paid"),
    (5, "2026-03-15", 109.98, "Credit Card", "Paid"),
]


def seed_database():
    create_tables()
    connection = get_connection()

    try:
        cursor = connection.cursor()

        table_order = [
            "Payment",
            "Rental",
            "Reservation",
            "Staff",
            "Vehicle",
            "Customer",
            "Location",
        ]
        for table_name in table_order:
            cursor.execute(f"DELETE FROM {table_name}")

        cursor.executemany(
            """
            INSERT INTO Location (location_name, city, state, phone_number)
            VALUES (?, ?, ?, ?)
            """,
            LOCATIONS,
        )

        cursor.executemany(
            """
            INSERT INTO Customer (
                first_name, last_name, phone, email, driver_license_number, address
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            CUSTOMERS,
        )

        cursor.executemany(
            """
            INSERT INTO Vehicle (
                vin, make, model, year, color, license_plate, mileage,
                daily_rate, status, location_id
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            VEHICLES,
        )

        cursor.executemany(
            """
            INSERT INTO Staff (
                first_name, last_name, username, email, role, phone, address
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            STAFF_MEMBERS,
        )

        cursor.executemany(
            """
            INSERT INTO Reservation (
                customer_id, vehicle_id, reservation_date, pickup_date, return_date,
                reservation_status, estimated_total
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            RESERVATIONS,
        )

        cursor.executemany(
            """
            INSERT INTO Rental (
                customer_id, vehicle_id, staff_id, checkout_date, due_date, return_date,
                checkout_mileage, return_mileage, rental_status, total_cost
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            RENTALS,
        )

        cursor.executemany(
            """
            INSERT INTO Payment (
                rental_id, payment_date, amount, payment_method, payment_status
            )
            VALUES (?, ?, ?, ?, ?)
            """,
            PAYMENTS,
        )

        connection.commit()
    finally:
        connection.close()


if __name__ == "__main__":
    seed_database()
    print("Car rental database seeded successfully.")
