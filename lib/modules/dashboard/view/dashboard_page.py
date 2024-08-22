from packages.models import User
from packages.task_repository import TaskRepository

from ..bloc.dashboard_bloc import DashboardBloc


class DashboardPage:
    def __init__(self, *, taskRepository: TaskRepository, user: User) -> None:
        self.dashboardBloc = DashboardBloc(taskRepository=taskRepository, user=user)

    def build(self):
        num1 = self.dashboardBloc.state.completedTasks
