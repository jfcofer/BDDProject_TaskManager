from psycopg2.pool import SimpleConnectionPool

from .database_configuration import DatabaseConfiguration


class ConnectionManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(ConnectionManager, cls).__new__(cls)
            cls._instance._connection_pool = None
        return cls._instance

    def initialize(self, *, databaseConfiguration: DatabaseConfiguration):
        if self._connection_pool is None:
            self._connection_pool = SimpleConnectionPool(
                minconn=databaseConfiguration.minconn,
                maxconn=databaseConfiguration.maxconn,
                dbname=databaseConfiguration.dbname,
                user=databaseConfiguration.user,
                password=databaseConfiguration.password,
                host=databaseConfiguration.host,
                port=databaseConfiguration.port,
            )

    def get_connection(self):
        if self._connection_pool is None:
            raise Exception("Connection pool is not initialized.")
        return self._connection_pool.getconn()

    def release_connection(self, *, conn):
        if self._connection_pool is not None:
            self._connection_pool.putconn(conn)

    def close_all_connections(self):
        if self._connection_pool is not None:
            self._connection_pool.closeall()
