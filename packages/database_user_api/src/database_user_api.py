from typing import List

from packages.database_api import DatabaseApi
from packages.database_connection_manager.src.connection_manager import (
    ConnectionManager,
)
from packages.models import Report, User
from packages.user_api import UserApi


class DatabaseUserApi(UserApi, DatabaseApi):
    def __init__(self, *, connectionManager: ConnectionManager) -> None:
        super().__init__(connectionManager=connectionManager)

    def getUserById(self, *, userId: int) -> User:
        userData = self._execute_stored_procedure("get_user_info", (userId,))
        return User(
            id=userData[0]["id"],
            email=userData[0]["email"],
            firstName=userData[0]["first_name"],
            lastName=userData[0]["last_name"],
        )

    def updateUser(self, *, user: User):
        self._execute_stored_procedure(
            "update_user", (user.email, user.firstName, user.lastName)
        )

    def getReportsForUser(self, *, user: User) -> List[Report]:
        reportsData = self._execute_stored_procedure("get_user_reports", (user.id,))
        return [
            Report(id=report["id"], creation_date=report["creation_date"])
            for report in reportsData
        ]

    def addReportForUser(self, *, report: Report):
        self._execute_stored_procedure(
            "add_report", (report.creationDate, report.user.id)
        )
