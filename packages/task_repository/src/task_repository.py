from packages.task_api import TaskApi


class TaskRepository:
    def __init__(self, *, taskApi: TaskApi) -> None:
        self.taskApi = taskApi
    
