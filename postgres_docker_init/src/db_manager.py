import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()


def get_pg_creds():
    return {
        "user": os.environ.get("POSTGRES_USER"),
        "password": os.environ.get("POSTGRES_PASSWORD"),
        "port": os.environ.get("POSTGRES_PORT", 5434),
        "host": os.environ.get("POSTGRES_HOST", "localhost"),
        "db_name": os.environ.get("POSTGRES_DB"),
    }


def start_postgres_connection():
    creds = get_pg_creds()
    connection = psycopg2.connect(
        dbname=creds["db_name"],
        user=creds["user"],
        password=creds["password"],
        host=creds["host"],
        port=creds["port"],
    )

    return connection


def query_database(connection, query_str):
    conn = connection
    cursor = conn.cursor()
    cursor.execute(query_str)
    rows = cursor.fetchall()

    cursor.close
    conn.close

    return rows
