from packages.models import Task, Status

class TaskDetailsState():
    def __init__(self, *, task: Task = None) -> None:
        self.task = task
