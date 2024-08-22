from packages.models import User
from packages.task_repository import TaskRepository
from .task_details_event import TaskDetailsEvent, TaskDetailsSubscriptionRequested
from .task_details_state import TaskDetailsState
from packages.models import Task 

class TaskDetailsBloc:
    def __init__(self, *, taskRepository: TaskRepository, task: Task) -> None:
        self.taskRepository = taskRepository
        self.task = task
        self.state = TaskDetailsState()
    
    def add(self, *, event: TaskDetailsEvent):
        if isinstance(event, TaskDetailsSubscriptionRequested):
            self._onDashboardSubscriptionRequested(event=event)

    def _onTaskDetailSubscriptionRequested(self, *, event: TaskDetailsSubscriptionRequested):
        self.state.subtasks = self.taskRepository.getSubtasksForTask(self.task)