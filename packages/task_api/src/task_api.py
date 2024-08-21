from abc import ABC, abstractmethod
from typing import List

from packages.models import Reminder, Subtask, Task, User


class TaskApi(ABC):
    @abstractmethod
    def getTasksForUser(self, *, user: User) -> List[Task]:
        pass

    @abstractmethod
    def saveTask(self, *, task: Task) -> None:
        pass

    @abstractmethod
    def deleteTask(self, *, task: Task) -> None:
        pass

    @abstractmethod
    def getSubtasksForTask(self, *, task: Task) -> List[Subtask]:
        pass

    @abstractmethod
    def saveSubtask(self, *, subtask: Subtask) -> None:
        pass

    @abstractmethod
    def deleteSubtask(self, *, subtask: Subtask) -> None:
        pass

    @abstractmethod
    def getRemindersForTask(self, task: Task) -> List[Reminder]:
        pass

    @abstractmethod
    def saveReminder(self, *, reminder: Reminder) -> None:
        pass

    @abstractmethod
    def deleteReminder(self, *, reminder: Reminder) -> None:
        pass
