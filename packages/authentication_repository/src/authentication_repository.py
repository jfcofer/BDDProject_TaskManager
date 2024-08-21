from packages.authentication_api import AuthenticationApi
from packages.models import User


class AuthenticationRepository:
    def __init__(self, *, authenticationApi: AuthenticationApi) -> None:
        self.authenticationApi = authenticationApi

    def registerUser(self, *, user: User):
        self.authenticationApi.registerUser(user=user)

    def authenticateUser(self, *, email: str, password: str):
        self.authenticationApi.authenticateUser(email=email, password=password)
