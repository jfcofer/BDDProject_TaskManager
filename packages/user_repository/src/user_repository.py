from typing import List

from packages.models import Report, User
from packages.user_api import UserApi


class UserRepository:
    def __init__(self, *, userApi: UserApi) -> None:
        self.userApi = userApi

    def getUserById(self, *, userId: int) -> User:
        self.userApi.getUserById(userId=userId)

    def updateUser(self, *, user: User)->None:
        self.userApi.updateUser(user=user)

    def getReportsForUser(self, *, user: User) -> List[Report]:
        self.userApi.getReportsForUser(user=user)

    def addReportForUser(self, *, report: Report)->None:
        self.userApi.addReportForUser(report=report)
