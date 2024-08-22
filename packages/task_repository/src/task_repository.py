from typing import List

from packages.models import Reminder, Subtask, Task, User
from packages.task_api import TaskApi


class TaskRepository:
    def __init__(self, *, taskApi: TaskApi) -> None:
        self.taskApi = taskApi

    def getTasksForUser(self, *, user: User) -> List[Task]:
        self.taskApi.getTasksForUser(user=user)

    def saveTask(self, *, task: Task) -> None:
        self.taskApi.saveTask(task=task)

    def deleteTask(self, *, task: Task) -> None:
        self.taskApi.deleteTask(task=Task)

    def getSubtasksForTask(self, *, task: Task) -> List[Subtask]:
        self.taskApi.getSubtasksForTask(task=task)

    def saveSubtask(self, *, subtask: Subtask) -> None:
        self.taskApi.saveSubtask(subtask=subtask)

    def deleteSubtask(self, *, subtask: Subtask) -> None:
        self.taskApi.deleteSubtask(subtask=subtask)

    def getRemindersForTask(self, task: Task) -> List[Reminder]:
        self.taskApi.getRemindersForTask(task=task)

    def saveReminder(self, *, reminder: Reminder) -> None:
        self.taskApi.saveReminder(reminder=reminder)

    def deleteReminder(self, *, reminder: Reminder) -> None:
        self.taskApi.deleteReminder(reminder=reminder)
