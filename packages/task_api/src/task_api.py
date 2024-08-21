from abc import ABC, abstractmethod
from typing import List

from packages.models import Reminder, Subtask, Task


class TaskApi(ABC):
    @abstractmethod
    def getTasksForUser(self, user: User) -> List[Task]:
        pass

    @abstractmethod
    def saveTask(self, user_id: int, task: Task) -> None:
        pass

    @abstractmethod
    def getSubtasksForTask(self, task_id: int) -> List[Subtask]:
        pass

    @abstractmethod
    def get_reminders_for_task(self, task_id: int) -> List[Reminder]:
        pass
