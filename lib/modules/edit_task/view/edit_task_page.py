from typing import Any, Tuple

import customtkinter as ctk

from packages.models import Task, Status
from packages.task_repository import TaskRepository

from ..bloc.edit_task_bloc import EditTaskBloc
from ..bloc.edit_task_event import EditTaskTitleChanged


class EditTaskPage(ctk.CTkFrame):
    def __init__(
        self,
        master: Any,
        taskRepository: TaskRepository,
        initialTask: Task,
        width: int = 200,
        height: int = 200,
        corner_radius: int | str | None = None,
        border_width: int | str | None = None,
        bg_color: str | Tuple[str, str] = "transparent",
        fg_color: str | Tuple[str, str] | None = None,
        border_color: str | Tuple[str, str] | None = None,
        background_corner_colors: Tuple[str | Tuple[str, str]] | None = None,
        overwrite_preferred_drawing_method: str | None = None,
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
        self.bloc = EditTaskBloc(initialTask=initialTask, taskRepository=taskRepository)

        self._build()

    def _build(self):
        opciones = [status.value for status in Status]
        opcionEscogida = self.bloc.state.currentStatus.value
        