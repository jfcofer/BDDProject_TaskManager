from os import getenv

from dotenv import load_dotenv

from packages.authentication_repository import AuthenticationRepository
from packages.database_authentication_api import DatabaseAuthenticationApi
from packages.database_connection_manager import (
    ConnectionManager,
    DatabaseConfiguration,
)
from packages.database_task_api import DatabaseTaskApi
from packages.database_user_api import DatabaseUserApi
from packages.task_repository import TaskRepository
from packages.user_repository import UserRepository


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

    userApi = DatabaseUserApi(connectionManager=connectionManager)
    taskApi = DatabaseTaskApi(connectionManager=connectionManager)
    authenticationApi = DatabaseAuthenticationApi(connectionManager=connectionManager)

    userRepository = UserRepository(userApi=userApi)
    taskReposiotry = TaskRepository(taskApi=taskApi)
    authenticationRepository = AuthenticationRepository(
        authenticationApi=authenticationApi
    )
