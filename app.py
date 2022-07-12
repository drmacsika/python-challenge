import os

from src import app
from src.database import connect_to_database
from src.routes import add_routes

connect_to_database(os.getenv("DB_URI"))

add_routes()
