from packages.models import Task, Status
from typing import List

class DashboardState():
    def __init__(self, *, tasks: List[Task] = []) -> None:
        self.tasks = tasks
        self.calculateValues()

    def calculateValues(self) -> None:
        self.totalTasks = len(self.tasks)
        self.completedTasks = len([task for task in self.tasks if task.currentStatus==Status.COMPLETED])
        self.pendingTasks = len([task for task in self.tasks if task.currentStatus==Status.PENDING])
        self.inProgressTasks = len([task for task in self.tasks if task.currentStatus==Status.IN_PROGRESS])
