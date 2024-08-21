from abc import ABC, abstractmethod

from packages.models import User


class AuthenticationApi(ABC):
    @abstractmethod
    def registerUser(self, *, user: User):
        pass

    @abstractmethod
    def authenticateUser(self, *, email: str, password: str):
        pass
