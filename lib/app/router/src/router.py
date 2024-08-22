from lib.modules.dashboard import DashboardPage



class Router:
    def __init__(self, parent):
        self.parent = parent
        self.routes = {"home": HomePage, "contact": ContactPage, "about": AboutPage}

    def create_frames(self):
        for route, FrameClass in self.routes.items():
            frame = FrameClass(self.parent, self)
            frame.grid(row=0, column=0, sticky="nsew")

    def go(self, page_route):
        frame = self.frames[page_route]
        frame.tkraise()
