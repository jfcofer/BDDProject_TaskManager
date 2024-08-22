from os import getenv

import psycopg2
from dotenv import load_dotenv
from psycopg2.extensions import connection

from packages.database_connection_manager import (
    ConnectionManager,
    DatabaseConfiguration,
)


class DatabaseApi:
    def __init__(self, *, connectionManager: ConnectionManager) -> None:
        self.connectionManager = connectionManager
        load_dotenv()

        self.databaseConfiguration = DatabaseConfiguration(
            dbname=getenv("DB_NAME"),
            user=getenv("DB_USER"),
            password=getenv("DB_PASSWORD"),
            host=getenv("DB_HOST"),
            port=getenv("DB_PORT", 5432),
            minconn=int(getenv("DB_MINCONN", 1)),
            maxconn=int(getenv("DB_MAXCONN", 10)),
        )

    def _getConnection(self):
        return self.connectionManager.getConnection()

    def _releaseConnection(self, *, conn: connection):
        self.connectionManager.releaseConnection(conn=conn)

    def _executeStoredProcedure(self, *, procedureName: str, params: tuple):
        conn = self._getConnection()
        try:
            with conn.cursor() as cursor:
                cursor.callproc(procedureName, params)
                conn.commit()
        except psycopg2.Error as e:
            print(f"Database error: {e}")
            conn.rollback()
            raise e  # Re-raise or handle it according to your needs
        finally:
            self._releaseConnection(conn=conn)

    def _executeStoredProcedureWithReturn(self, *, procedureName: str, params: tuple):
        conn = self._getConnection()
        try:
            with conn.cursor() as cursor:
                cursor.callproc(procedureName, params)
                if cursor.description:
                    return cursor.fetchall()
                conn.commit()
        except psycopg2.Error as e:
            print(f"Database error: {e}")
            conn.rollback()
            raise e  # Re-raise or handle it according to your needs
        finally:
            self._releaseConnection(conn=conn)
