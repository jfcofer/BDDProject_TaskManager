import psycopg2
from psycopg2.extensions import connection

from packages.database_connection_manager import ConnectionManager


class DatabaseApi:
    def __init__(self, *, connectionManager: ConnectionManager) -> None:
        self.connectionManager = connectionManager

    def _getConnection(self):
        return self.connectionManager.get_connection()

    def _releaseConnection(self, *, conn: connection):
        self.connectionManager.release_connection(conn=conn)

    def _executeStoredProcedure(self, *, procedure_name, params):
        conn = self._get_connection()
        try:
            with conn.cursor() as cursor:
                cursor.execute(f"CALL {procedure_name}(%s)", params)
                if cursor.description:  # If the stored procedure returns data
                    return cursor.fetchall()
        except psycopg2.Error as e:
            print(f"Database error: {e}")
            raise  # Re-raise or handle it according to your needs
        finally:
            self._releaseConnection(conn=conn)
