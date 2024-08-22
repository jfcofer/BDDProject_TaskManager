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
        userData = self._executeStoredProcedureWithReturn(
            procedureName="get_user_info", params=(userId,)
        )
        if userData:
            return User(
                id=userData[0][0],
                email=userData[0][1],
                firstName=userData[0][2],
                lastName=userData[0][3],
            )

    def updateUser(self, *, user: User)->None:
        self._executeStoredProcedure(
            procedureName="update_user",
            params=(user.email, user.firstName, user.lastName),
        )

    def getReportsForUser(self, *, user: User) -> List[Report]:
        reportsData = self._executeStoredProcedureWithReturn(
            procedureName="get_user_reports", params=(user.id,)
        )
        return [
            Report(id=report[0], creationDate=report[1], user=user)
            for report in reportsData
        ]

    def addReportForUser(self, *, report: Report)->None:
        self._executeStoredProcedure(
            procedureName="add_report", params=(report.creationDate, report.user.id)
        )
