from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATABASE_NAME = "car_rental.db"
DATABASE_PATH = BASE_DIR / DATABASE_NAME
DATABASE_URI = f"sqlite:///{DATABASE_PATH}"
