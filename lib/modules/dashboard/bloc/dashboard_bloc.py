from packages.models import User
from packages.task_repository import TaskRepository


class DashboardBloc:
    def __init__(self, *, taskRepository: TaskRepository, user: User) -> None:
        self.taskRepository = taskRepository
        self.user = user
    
    def
