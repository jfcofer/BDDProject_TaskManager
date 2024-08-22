from packages.models import Task, Status
from typing import List
class DashboardState():
    def __init__(self, *, tasks:List[Task] = []) -> None:
        self.tasks = tasks
        self.completedTasks = [task for task in tasks if task.currentStatus==Status.COMPLETED]
        self.pendingTasks = [task for task in tasks if task.currentStatus==Status.PENDING]
        self.inProgressTasks = [task for task in tasks if task.currentStatus==Status.IN_PROGRESS]
        