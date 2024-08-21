from dataclasses import dataclass, field
from datetime import date

from packages.models.src.priority import Priority
from packages.models.src.status import Status
from packages.models.src.user import User


@dataclass(frozen=True)
class Task:
    id: int
    title: str
    description: str
    due_date: date
    user: User
    current_status: Status = Status.PENDING
    current_priority: Priority = Priority.PRIORITY_1
