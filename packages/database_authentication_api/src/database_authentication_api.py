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

    def authenticateUser(self, *, email: str, password: str) -> User | None:
        userData = self._executeStoredProcedureWithReturn(
            procedureName="authenticate_user", params=(email,)
        )

        if userData:
            print(userData)
            stored_hashed_password = userData[0][4]

            # Verify the password
            if bcrypt.checkpw(
                password.encode("utf-8"), stored_hashed_password.encode("utf-8")
            ):
                print(userData[0][0], userData[0][1], userData[0][2], userData[0][3])
                user = User(
                    int(userData[0][0]), userData[0][1], userData[0][2], userData[0][3]
                )
                print(user)
                return user
            return None

    def registerUser(
        self, *, email: str, password: str, firstName: str, lastName: str
    ) -> None:
        # Hash the password
        hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

        # Convert the hashed password to a string if necessary
        hashed_password = hashed_password.decode("utf-8")
        print(f"Registering user: {email}, {hashed_password}, {firstName}, {lastName}")
        self._executeStoredProcedure(
            procedureName="register_user",
            params=(email, hashed_password, firstName, lastName),
        )
