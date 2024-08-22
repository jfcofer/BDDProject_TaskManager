import psycopg2
from psycopg2.extensions import connection
from psycopg2.extras import DictCursor

from packages.database_connection_manager import ConnectionManager


class DatabaseApi:
    def __init__(self, *, connectionManager: ConnectionManager) -> None:
        self.connectionManager = connectionManager

    def _getConnection(self):
        return self.connectionManager.getConnection()

    def _releaseConnection(self, *, conn: connection):
        self.connectionManager.releaseConnection(conn=conn)

    def _executeStoredProcedure(self, *, procedureName: str, params: tuple):
        conn = self._getConnection()
        try:
            with conn.cursor(cursor_factory=DictCursor) as cursor:
                cursor.callproc(procedureName, params)
                if cursor.description:  # If the stored procedure returns data
                    return cursor.fetchall()
                conn.commit()
        except psycopg2.Error as e:
            print(f"Database error: {e}")
            conn.rollback()
            raise e  # Re-raise or handle it according to your needs
        finally:
            self._releaseConnection(conn=conn)
