from ..bloc.dashboard_bloc import DashboardBloc
from

class DashboardPage():
    def __init__(self,*,taskRepository, user) -> None:
        self.dashboardBloc = DashboardBloc(taskRepository=taskRepository, user=user)