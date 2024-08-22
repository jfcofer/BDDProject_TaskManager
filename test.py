import psycopg2
from os import getenv
from packages.database_connection_manager import (
    ConnectionManager,
    DatabaseConfiguration,
)
from dotenv import load_dotenv

load_dotenv()


databaseConfiguration = DatabaseConfiguration(
    dbname=getenv("DB_NAME"),
    user=getenv("DB_USER"),
    password=getenv("DB_PASSWORD"),
    host=getenv("DB_HOST"),
    port=getenv("DB_PORT", 5432),
    minconn=int(getenv("DB_MINCONN", 1)),
    maxconn=int(getenv("DB_MAXCONN", 10)),
)


def test_register_user():
    try:
        conn = psycopg2.connect(
            dbname=databaseConfiguration.dbname,
            user=databaseConfiguration.user,
            password=databaseConfiguration.password,
            host=databaseConfiguration.host,
        )
        with conn.cursor() as cursor:
            hashed_password = "known_good_hashed_password"
            cursor.callproc(
                "register_user", ("hola@mail.com", hashed_password, "Juan", "Doe")
            )
            conn.commit()
            print("User registered successfully")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()


test_register_user()
