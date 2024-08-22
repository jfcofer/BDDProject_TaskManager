from packages.models import User
from packages.task_repository import TaskRepository
from .dashboard_state import DashboardState
from .dashboard_events import DashboardEvent, DashboardSubscriptionRequested


class DashboardBloc:
    def __init__(self, *, taskRepository: TaskRepository, user: User) -> None:
        self.taskRepository = taskRepository
        self.user = user
        self.state = DashboardState()
    
    def add(self, *, event: DashboardEvent):
        if isinstance(event, DashboardSubscriptionRequested):
            self._onDashboardSubscriptionRequested(event=event)

    def _onDashboardSubscriptionRequested(self, *, event: DashboardSubscriptionRequested):
        self.state.tasks = self.taskRepository.getTasksForUser(user=self.user)
