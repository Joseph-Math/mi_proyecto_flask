import mysql.connector

def get_db_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="abc123abc123",
        database="liceo_policial"
    )
    return conn
