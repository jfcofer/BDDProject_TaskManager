from abc import ABC


class EditTaskEvent(ABC):
    pass


class EditTaskTitleChanged(EditTaskEvent):
    def __init__(self, *, title: str) -> None:
        self.title = title


class EditTaskSubmitted:
    def __init__(self) -> None:
        pass
