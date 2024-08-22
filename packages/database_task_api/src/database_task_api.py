from datetime import date
from typing import List

from packages.database_api import DatabaseApi
from packages.database_connection_manager.src.connection_manager import (
    ConnectionManager,
)
from packages.models import Priority, Reminder, Status, Subtask, Task, User
from packages.task_api import TaskApi


class DatabaseTaskApi(TaskApi, DatabaseApi):
    def __init__(self, *, connectionManager: ConnectionManager) -> None:
        super().__init__(connectionManager=connectionManager)

    def getTasksForUser(self, *, user: User) -> List[Task]:
        tasksData = self._executeStoredProcedure(
            procedureName="get_tasks_for_user", params=(user.id,)
        )
        if tasksData:
            return [
                Task(
                    id=taskData["id"],
                    title=taskData["title"],
                    description=taskData["description"],
                    dueDate=taskData["due_date"],
                    currentStatus=Status(taskData["status"]),
                    currentPriority=Priority(taskData["priority"]),
                    user=user,
                )
                for taskData in tasksData
            ]
        else:
            return []

    def saveTask(
        self,
        *,
        user: User,
        taskTitle: str,
        taskDescription: str,
        taskDate: date,
        taskStatus: Status = Status.PENDING,
        taskPriority: Priority = Priority.PRIORITY_1
    ) -> None:
        self._executeStoredProcedure(
            procedureName="save_task",
            params=(
                user.id,
                taskTitle,
                taskDescription,
                taskDate,
                taskStatus.value,
                taskPriority.value,
            ),
        )

    def updateTask(self, *, task: Task) -> None:
        self._executeStoredProcedure(
            procedureName="update_task",
            params=(
                task.id,
                task.title,
                task.description,
                task.currentStatus.value,
                task.currentStatus.value,
            ),
        )

    def deleteTask(self, *, task: Task) -> None:
        self._executeStoredProcedure(procedureName="delete_task", params=(task.id))

    def getSubtasksForTask(self, *, task: Task) -> List[Subtask]:
        subtasksData = self._executeStoredProcedure(
            procedureName="get_subtasks_for_task", params=(task.id,)
        )
        if subtasksData:

            return [
                Subtask(
                    id=subtask["id"],
                    title=subtask["title"],
                    currentStatus=Status(subtask["status"]),
                    currentPriority=Priority(subtask["priority"]),
                    mainTask=task,
                )
                for subtask in subtasksData
            ]
        else:
            return []

    def saveSubtask(
        self,
        *,
        mainTask: Task,
        subtaskTitle: str,
        subtaskStatus: Status = Status.PENDING,
        subtaskPriority: Priority = Priority.PRIORITY_1
    ) -> None:
        self._executeStoredProcedure(
            procedureName="save_subtask",
            params=(
                mainTask.id,
                subtaskTitle,
                subtaskStatus.value,
                subtaskPriority.value,
            ),
        )

    def updateSubtask(self, *, subtask: Subtask) -> None:
        self._executeStoredProcedure(
            procedureName="update_subtask",
            params=(
                subtask.id,
                subtask.title,
                subtask.currentStatus.value,
                subtask.currentStatus.value,
            ),
        )

    def deleteSubtask(self, *, subtask: Subtask) -> None:
        self._executeStoredProcedure(
            procedureName="delete_subtask",
            params=(subtask.id,),
        )

    def getRemindersForTask(self, task: Task) -> List[Reminder]:
        remindersData = self._executeStoredProcedure(
            procedureName="get_reminders_for_task", params=(task.id,)
        )
        if remindersData:

            return [
                Reminder(
                    id=reminder["id"],
                    description=reminder["description"],
                    reminderDate=reminder["reminderDate"],
                    task=task,
                )
                for reminder in remindersData
            ]
        else:
            return []

    def saveReminder(
        self, *, task: Task, reminderDescription: str, reminderDate: date
    ) -> None:
        self._executeStoredProcedure(
            procedureName="save_subtask",
            params=(
                task.id,
                reminderDescription,
                reminderDate.ctime(),
            ),
        )

    def deleteReminder(self, *, reminder: Reminder) -> None:
        self._executeStoredProcedure(
            procedureName="delete_reminder",
            params=(reminder.id,),
        )
