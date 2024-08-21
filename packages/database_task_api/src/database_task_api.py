from packages.database_connection_manager.src.connection_manager import ConnectionManager
from packages.task_api import TaskApi
from packages.database_api import DatabaseApi

class DatabaseTaskApi(TaskApi, DatabaseApi):
    def __init__(self, *, connectionManager: ConnectionManager) -> None:
        super().__init__(connectionManager=connectionManager)

    