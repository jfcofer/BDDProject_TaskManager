from typing import Optional

from packages.authentication_api import AuthenticationApi
from packages.database_api import DatabaseApi
from packages.database_connection_manager.src.connection_manager import (
    ConnectionManager,
)
from packages.models import User


class DatabaseAuthenticationApi(AuthenticationApi, DatabaseApi):
    def __init__(self, *, connectionManager: ConnectionManager) -> None:
        super().__init__(connectionManager=connectionManager)

    def authenticateUser(self, *, email: str, password: str) -> Optional[User]:
        userData = self._executeStoredProcedure(
            procedureName="authenticate_user", params=(email, password)
        )
        if userData:
            return User(
                id=userData[0]["id"],
                email=userData[0]["email"],
                first_name=userData[0]["first_name"],
                last_name=userData[0]["last_name"],
            )
        return None

    def registerUser(
        self, *, email: str, password: str, first_name: str, last_name: str
    ) -> User:
        userData = self._executeStoredProcedure(
            procedureName="register_user",
            params=(email, password, first_name, last_name),
        )
        return User(
            id=userData[0]["id"],
            email=userData[0]["email"],
            first_name=userData[0]["first_name"],
            last_name=userData[0]["last_name"],
        )
