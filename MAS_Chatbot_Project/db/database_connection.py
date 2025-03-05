import psycopg2
from .database_config import DB_CONFIG

def connect_to_db():
    connection = psycopg2.connect(**DB_CONFIG)
    return connection
