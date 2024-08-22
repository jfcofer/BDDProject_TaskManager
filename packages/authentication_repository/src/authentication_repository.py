from typing import Optional

from packages.authentication_api import AuthenticationApi
from packages.models import User


class AuthenticationRepository:
    def __init__(self, *, authenticationApi: AuthenticationApi) -> None:
        self.authenticationApi = authenticationApi

    def registerUser(
        self, *, email: str, password: str, firstName: str, lastName: str
    ) -> None:
        self.authenticationApi.registerUser(
            email=email, password=password, firstName=firstName, lastName=lastName
        )

    def authenticateUser(self, *, email: str, password: str) -> Optional[User]:
        self.authenticationApi.authenticateUser(email=email, password=password)
