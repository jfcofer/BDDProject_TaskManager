from os import getenv

from dotenv import load_dotenv

from packages.database_connection_manager import (
    ConnectionManager,
    DatabaseConfiguration,
)


def main():

    load_dotenv()

    databaseConfiguration = DatabaseConfiguration(
        dbname=getenv("DB_NAME"),
        user=getenv("DB_USER"),
        password=getenv("DB_PASSWORD"),
        host=getenv("DB_HOST"),
        port=getenv("DB_PORT"),
        minconn=int(getenv("DB_MINCONN", 1)),
        maxconn=int(getenv("DB_MAXCONN", 10)),
    )

    connectionManager = ConnectionManager()
    connectionManager.initialize(databaseConfiguration=databaseConfiguration)
