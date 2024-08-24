import psycopg2
from config import DB_HOST, DB_PORT, DB_USER, DB_NAME, DB_PASSWORD

def get_db_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        dbname=DB_NAME
    )
    return conn
