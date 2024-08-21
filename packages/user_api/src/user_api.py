from abc import ABC, abstractmethod
from typing import List

from packages.models import Report, User


class UserApi(ABC):
    @abstractmethod
    def getUserById(self, *, userId: int) -> User:
        pass

    @abstractmethod
    def updateUser(self, *, user: User):
        pass

    @abstractmethod
    def getReportsForUser(self, *, user: User) -> List[Report]:
        pass

    @abstractmethod
    def addReportForUser(self, *, report: Report):
        pass
