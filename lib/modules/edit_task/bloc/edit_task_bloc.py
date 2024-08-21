from packages.models import Task

from .edit_task_event import EditTaskEvent, EditTaskTitleChanged
from .edit_task_state import EditTaskState


class EditTaskBloc:
    def __init__(self, *, taskRepository: TaskRepository, initialTask: Task) -> None:
        self.taskRepository = taskRepository
        self.state = EditTaskState(initialTask=initialTask)

    def add(self, *, event: EditTaskEvent):
        if isinstance(event, EditTaskTitleChanged):
            self._onEditTaskTitleChanged(event.title)
        

    def _onEditTaskTitleChanged(self, *, event: EditTaskTitleChanged):
        self.state = self.state.title = event.title

    def _onEditTaskSubmitted(self):
        task = Task(
            id=self.state.initialTask.id,
            title=self.state.title,
            description=self.state.description,
            currentPriority=self.state.currentPriority,
            currentStatus=self.state.currentStatus,
        )
        self.taskRepository.saveTask(task)
