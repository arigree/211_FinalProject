import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATABASE_NAME = "car_rental.db"
DATABASE_PATH = BASE_DIR / DATABASE_NAME


def get_connection():
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON;")
    return connection


SCHEMA_STATEMENTS = [
    """
    CREATE TABLE IF NOT EXISTS Customer (
        customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        phone TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        driver_license_number TEXT NOT NULL UNIQUE,
        address TEXT NOT NULL
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS Location (
        location_id INTEGER PRIMARY KEY AUTOINCREMENT,
        location_name TEXT NOT NULL,
        city TEXT NOT NULL,
        state TEXT NOT NULL,
        phone_number TEXT NOT NULL
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS Vehicle (
        vehicle_id INTEGER PRIMARY KEY AUTOINCREMENT,
        vin TEXT NOT NULL UNIQUE,
        make TEXT NOT NULL,
        model TEXT NOT NULL,
        year INTEGER NOT NULL,
        color TEXT NOT NULL,
        license_plate TEXT NOT NULL UNIQUE,
        mileage INTEGER NOT NULL,
        daily_rate REAL NOT NULL,
        status TEXT NOT NULL,
        location_id INTEGER NOT NULL,
        FOREIGN KEY (location_id) REFERENCES Location(location_id)
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS Rental (
        rental_id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id INTEGER NOT NULL,
        vehicle_id INTEGER NOT NULL,
        checkout_date TEXT NOT NULL,
        due_date TEXT NOT NULL,
        return_date TEXT,
        checkout_mileage INTEGER NOT NULL,
        return_mileage INTEGER,
        rental_status TEXT NOT NULL,
        total_cost REAL NOT NULL,
        FOREIGN KEY (customer_id) REFERENCES Customer(customer_id),
        FOREIGN KEY (vehicle_id) REFERENCES Vehicle(vehicle_id)
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS Payment (
        payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
        rental_id INTEGER NOT NULL,
        payment_date TEXT NOT NULL,
        amount REAL NOT NULL,
        payment_method TEXT NOT NULL,
        payment_status TEXT NOT NULL,
        FOREIGN KEY (rental_id) REFERENCES Rental(rental_id)
    );
    """,
]


def create_tables():
    connection = get_connection()

    try:
        cursor = connection.cursor()
        for statement in SCHEMA_STATEMENTS:
            cursor.execute(statement)
        connection.commit()
    finally:
        connection.close()
