from typing import Optional

import bcrypt

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
            procedureName="authenticate_user", params=(email,)
        )

        if userData:
            stored_hashed_password = userData[0]["password"]

            # Verify the password
            if bcrypt.checkpw(
                password.encode("utf-8"), stored_hashed_password.encode("utf-8")
            ):

                return User(
                    id=userData[0]["id"],
                    email=userData[0]["email"],
                    firstName=userData[0]["first_name"],
                    lastName=userData[0]["last_name"],
                )
        return None

    def registerUser(
        self, *, email: str, password: str, firstName: str, lastName: str
    ) -> None:
        # Hash the password
        hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

        # Convert the hashed password to a string if necessary
        hashed_password = hashed_password.decode("utf-8")

        self._executeStoredProcedure(
            procedureName="register_user",
            params=(email, hashed_password, firstName, lastName),
        )
