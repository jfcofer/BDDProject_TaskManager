from typing import Any, Tuple

import customtkinter as ctk

from packages.models import User
from packages.task_repository import TaskRepository

from ..bloc.dashboard_bloc import DashboardBloc
from ..bloc.dashboard_events import DashboardSubscriptionRequested


class DashboardPage(ctk.CTkFrame):
    def __init__(
        self,
        master: Any,
        width: int = 200,
        height: int = 200,
        corner_radius: int | str | None = None,
        border_width: int | str | None = None,
        bg_color: str | Tuple[str, str] = "transparent",
        fg_color: str | Tuple[str, str] | None = None,
        border_color: str | Tuple[str, str] | None = None,
        background_corner_colors: Tuple[str | Tuple[str, str]] | None = None,
        overwrite_preferred_drawing_method: str | None = None,
        *,
        taskRepository: TaskRepository,
        user: User,
        **kwargs
    ):
        super().__init__(
            master,
            width,
            height,
            corner_radius,
            border_width,
            bg_color,
            fg_color,
            border_color,
            background_corner_colors,
            overwrite_preferred_drawing_method,
            **kwargs
        )
        self.dashboardBloc = DashboardBloc(taskRepository=taskRepository, user=user)
        self.dashboardBloc.add(event=DashboardSubscriptionRequested())

    def build(self):
        num1 = len(self.dashboardBloc.state.completedTasks)
