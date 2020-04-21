import psycopg2

def get_postgres_connection():
    conn = psycopg2.connect("host=localhost dbname=snowpackDB user=postgres password=postgres")
    return conn;