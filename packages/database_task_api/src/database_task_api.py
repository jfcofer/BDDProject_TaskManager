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
        tasksData = self._executeStoredProcedureWithReturn(
            procedureName="get_tasks_for_user", params=(user.id,)
        )
        if tasksData:
            return [
                Task(
                    id=taskData[0],
                    title=taskData[1],
                    description=taskData[2],
                    dueDate=taskData[3],
                    currentStatus=Status(taskData[4]),
                    currentPriority=Priority(taskData[5]),
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
                task.currentPriority.value,
            ),
        )

    def deleteTask(self, *, task: Task) -> None:
        self._executeStoredProcedure(procedureName="delete_task", params=(task.id,))

    def getSubtasksForTask(self, *, task: Task) -> List[Subtask]:
        subtasksData = self._executeStoredProcedureWithReturn(
            procedureName="get_subtasks_for_task", params=(task.id,)
        )
        if subtasksData:

            return [
                Subtask(
                    id=subtask[0],
                    title=subtask[1],
                    currentStatus=Status(subtask[2]),
                    currentPriority=Priority(subtask[3]),
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
                subtask.currentPriority.value,
            ),
        )

    def deleteSubtask(self, *, subtask: Subtask) -> None:
        self._executeStoredProcedure(
            procedureName="delete_subtask",
            params=(subtask.id,),
        )

    def getRemindersForTask(self, task: Task) -> List[Reminder]:
        remindersData = self._executeStoredProcedureWithReturn(
            procedureName="get_reminders_for_task", params=(task.id,)
        )
        if remindersData:

            return [
                Reminder(
                    id=reminder[0],
                    description=reminder[1],
                    reminderDate=reminder[2],
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
