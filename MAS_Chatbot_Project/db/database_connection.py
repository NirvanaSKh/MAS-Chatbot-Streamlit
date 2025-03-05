import psycopg2
from .database_config import DB_CONFIG

def connect_to_db():
    try:
        # Establish the connection using the database config
        connection = psycopg2.connect(**DB_CONFIG)
        return connection
    except Exception as e:
        print(f"Error: Unable to connect to the database: {e}")
        return None
