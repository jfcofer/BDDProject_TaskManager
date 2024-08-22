from packages.models import Task, Subtask, Status
from ..bloc.task_details_bloc import TaskDetailsBloc, TaskDetailsSubscriptionRequested
import customtkinter as ctk
import PIL

def load_image(path, size=None):
    image = PIL.Image.open(f"./images/{path}")
    return ctk.CTkImage(light_image=image, dark_image=image, size=size)

ICONS = {
    "go_back_arrow": load_image("go_back_arrow.png", (30, 30)),
    "edit": load_image("edit.png", (30, 30)),
    "trash": load_image("trash.png", (30, 30)),
}

STATE_COLORS = {
    Status.PENDING: "#ff6759",
    Status.IN_PROGRESS: "#ffd359",
    Status.COMPLETED: "#caff59",
}

# Esto solo es un widget, no la pagina.
class SubTaskWidget(ctk.CTkFrame):
    def __init__(self, parent, bloc, subtarea: Subtask, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.subtarea = subtarea
        self.bloc = bloc

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=0)

        # state and priority frame
        self.sapf = ctk.CTkFrame(self)
        self.sapf.grid(row=0, column=0, padx=40, pady=20, sticky="ew")

        self.state_label = ctk.CTkLabel(self.sapf, text=subtarea.currentStatus.value, text_color=STATE_COLORS[subtarea.currentStatus.value], font=ctk.CTkFont(size=12))
        self.state_label.pack()

        self.priority_label = ctk.CTkLabel(self.sapf, text=subtarea.currentPriority.value, font=ctk.CTkFont(size=16))
        self.priority_label.pack()

        self.title = ctk.CTkLabel(self, text=subtarea.title, font=ctk.CTkFont(weight="bold", size=20))
        self.title.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        self.trash_sub_icon = ctk.CTkLabel(self, image=ICONS["trash"], text="")
        self.trash_sub_icon.bind("<Button-1>", lambda _: self.trash())
        self.trash_sub_icon.grid(row=0, column=2, padx=40, pady=20, sticky="ew")

    def trash(self):
        self.bloc.taskRepository.deleteSubtask(self.subtarea)
        self.destroy()


class TaskDetailsPage(ctk.CTkFrame):
    def __init__(self, parent, controller, *, taskRepository, user):
        super().__init__(parent)
        self.controller = controller
        self.taskDetailsBloc = TaskDetailsBloc(taskRepository=taskRepository, user=user)
        self.taskDetailsBloc.add(event=TaskDetailsSubscriptionRequested())

        self.titulo = self.taskDetailsBloc.state.task.title
        self.descripcion = self.taskDetailsBloc.state.task.description
        self.subtareas = self.taskDetailsBloc.state.subtasks

        self.grid_columnconfigure(0, weight=1) # column for everything.

        self.grid_rowconfigure(0, weight=0) # row for icon and label.
        self.grid_rowconfigure(1, weight=0) # row for the description.
        self.grid_rowconfigure(2, weight=1) # row for the frame of subtareas.
        self.grid_rowconfigure(3, weight=0) # filler space between.
        self.grid_rowconfigure(4, weight=0) # row for the go to dashboard button.

        self.back_icon = ctk.CTkLabel(self, image=ICONS["go_back_arrow"], text="")
        # @TODO: implement router.
        self.back_icon.bind("<Button-1>", lambda: None)
        self.back_icon.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.title_label = ctk.CTkLabel(self, font=ctk.CTkFont(weight="bold", size=36), justify="center", text=self.titulo)
        self.title_label.grid(row=0, column=0, padx=10, pady=10)

        self.desc_label = ctk.CTkLabel(self, font=ctk.CTkFont(size=24), text=self.descripcion)
        self.desc_label.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        self.subtareas_frame = ctk.CTkScrollableFrame(self)
        self.subtareas_frame.grid_columnconfigure(0, weight=1)
        self.subtareas_frame.bind_all("<Button-4>", lambda _: self.subtareas_frame._parent_canvas.yview_scroll(-1, "units"))
        self.subtareas_frame.bind_all("<Button-5>", lambda _: self.subtareas_frame._parent_canvas.yview_scroll(+1, "units"))

        for index, subtarea in enumerate(self.subtareas):
            widget = SubTaskWidget(self.subtareas_frame, self.taskDetailsBloc, subtarea, border_color=STATE_COLORS[subtarea.state], border_width=2)
            widget.grid(row=index, column=0, padx=10, pady=10, sticky="ew")
        self.subtareas_frame.grid(row=2, column=0, padx=50, pady=20, sticky="nsew")

        self.go_to_dashboard_button = ctk.CTkButton(
            self,
            text="Ir al Dashboard",
            # @TODO: implementar router.
            command=lambda: None)
        self.go_to_dashboard_button.grid(row=3, column=0, padx=10, pady=10)

        self.bind("<Button-1>", lambda _: self.focus_set())


