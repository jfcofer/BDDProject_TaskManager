from abc import ABC, abstractmethod
from typing import Optional

from packages.models import User


class AuthenticationApi(ABC):
    @abstractmethod
    def registerUser(
        self, *, email: str, password: str, firstName: str, lastName: str
    ) -> None:
        pass

    @abstractmethod
    def authenticateUser(self, *, email: str, password: str) -> User | None:
        pass
