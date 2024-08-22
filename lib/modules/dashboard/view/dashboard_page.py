from ..bloc.dashboard_bloc import DashboardBloc, DashboardSubscriptionRequested
import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
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
    "pendiente": "#ff6759",
    "en progreso": "#ffd359",
    "completada": "#caff59",
}

class DashboardPage(ctk.CTkFrame):
    def __init__(self, master, *, taskRepository, user):
        super().__init__(master)
        self.dashboardBloc = DashboardBloc(taskRepository=taskRepository, user=user)
        self.dashboardBloc.add(event=DashboardSubscriptionRequested())

        self.n_completadas = self.dashboardBloc.state.completedTasks
        self.n_en_progreso = self.dashboardBloc.state.inProgressTasks
        self.n_pendientes = self.dashboardBloc.state.pendingTasks
        self.total_tareas = self.dashboardBloc.state.totalTasks

        self.grid_columnconfigure(0, weight=1) # column for back arrow.
        self.grid_columnconfigure(1, weight=1) # column for title.
        self.grid_columnconfigure(2, weight=1) # empty space to the right.

        self.grid_rowconfigure(0, weight=0) # row for back icon and title.
        self.grid_rowconfigure(1, weight=0) # row for total number of tasks.
        self.grid_rowconfigure(2, weight=0) # row for number of completed tasks.
        self.grid_rowconfigure(3, weight=0) # row for number of in progress tasks.
        self.grid_rowconfigure(4, weight=0) # row for number of pending tasks.
        self.grid_rowconfigure(5, weight=1) # row for chart from matplotlib.
        self.grid_rowconfigure(6, weight=0) # row for the go to dashboard button.

        self.back_icon = ctk.CTkLabel(self, image=ICONS["go_back_arrow"], text="")
        # @TODO: implementar router
        self.back_icon.bind("<Button-1>", lambda: None)
        self.back_icon.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.title_label = ctk.CTkLabel(self, text="Dashboard", font=ctk.CTkFont(weight="bold", size=36))
        self.title_label.grid(row=0, column=1, padx=10, pady=10)

        font = ctk.CTkFont(size=20)

        self.total_tareas_frame = ctk.CTkFrame(self)
        _ = ctk.CTkLabel(self.total_tareas_frame, text="Número ", font=font).pack(side="left")
        _ = ctk.CTkLabel(self.total_tareas_frame, text="total ", font=font, text_color="#69c3ff").pack(side="left")
        _ = ctk.CTkLabel(self.total_tareas_frame, text=f"de tareas: {self.total_tareas}", font=font).pack(side="left")
        self.total_tareas_frame.grid(row=1, column=1, padx=20, pady=20)

        self.n_completadas_frame = ctk.CTkFrame(self)
        _ = ctk.CTkLabel(self.n_completadas_frame, text="Número ", font=font).pack(side="left")
        _ = ctk.CTkLabel(self.n_completadas_frame, text="tareas completadas", font=font, text_color=STATE_COLORS["completada"]).pack(side="left")
        _ = ctk.CTkLabel(self.n_completadas_frame, text=f": {self.n_completadas}", font=font).pack(side="left")
        self.n_completadas_frame.grid(row=2, column=1, padx=20, pady=20)

        self.n_en_progreso_frame = ctk.CTkFrame(self)
        _ = ctk.CTkLabel(self.n_en_progreso_frame, text="Número ", font=font).pack(side="left")
        _ = ctk.CTkLabel(self.n_en_progreso_frame, text="tareas en progreso", font=font, text_color=STATE_COLORS["en progreso"]).pack(side="left")
        _ = ctk.CTkLabel(self.n_en_progreso_frame, text=f": {self.n_en_progreso}", font=font).pack(side="left")
        self.n_en_progreso_frame.grid(row=3, column=1, padx=20, pady=20)

        self.n_pendientes_frame = ctk.CTkFrame(self)
        _ = ctk.CTkLabel(self.n_pendientes_frame, text="Número ", font=font).pack(side="left")
        _ = ctk.CTkLabel(self.n_pendientes_frame, text="tareas pendientes", font=font, text_color=STATE_COLORS["pendiente"]).pack(side="left")
        _ = ctk.CTkLabel(self.n_pendientes_frame, text=f": {self.n_pendientes}", font=font).pack(side="left")
        self.n_pendientes_frame.grid(row=4, column=1, padx=20, pady=20)

        porcentajes = [
            (self.n_completadas / self.total_tareas) * 100,
            (self.n_en_progreso / self.total_tareas) * 100,
            (self.n_pendientes  / self.total_tareas) * 100,
        ]

        self.pie_frame = ctk.CTkFrame(self)
        fig, ax = plt.subplots(facecolor="#2b2b2b")
        _, texts, autotexts = ax.pie(porcentajes, labels=["Completadas", "En progreso", "Pendientes"], autopct="%1.1f%%")
        for text in texts:
            text.set_color("white")
            text.set_fontsize(14)
        for text in autotexts:
            text.set_color("white")
            text.set_fontsize(12)
        canvas = FigureCanvasTkAgg(figure=fig, master=self.pie_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()
        self.pie_frame.grid(row=5, column=1, padx=20, pady=20)
