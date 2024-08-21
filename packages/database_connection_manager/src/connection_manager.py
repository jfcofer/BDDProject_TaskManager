from typing import Any, Optional

from psycopg2.extensions import connection
from psycopg2.pool import SimpleConnectionPool

from .database_configuration import DatabaseConfiguration


class ConnectionManager:
    _instance: Optional["ConnectionManager"] = None
    _connectionPool: Optional[SimpleConnectionPool] = None

    def __new__(cls, *args: Any, **kwargs: Any) -> "ConnectionManager":
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def initialize(self, *, databaseConfiguration: DatabaseConfiguration) -> None:
        if self._connectionPool is None:
            self._connectionPool = SimpleConnectionPool(
                minconn=databaseConfiguration.minconn,
                maxconn=databaseConfiguration.maxconn,
                dbname=databaseConfiguration.dbname,
                user=databaseConfiguration.user,
                password=databaseConfiguration.password,
                host=databaseConfiguration.host,
                port=databaseConfiguration.port,
            )

    def get_connection(self) -> connection:
        if self._connectionPool is None:
            raise Exception("Connection pool is not initialized.")
        return self._connectionPool.getconn()

    def release_connection(self, *, conn: connection) -> None:
        if self._connectionPool is not None:
            self._connectionPool.putconn(conn)

    def close_all_connections(self) -> None:
        if self._connectionPool is not None:
            self._connectionPool.closeall()
