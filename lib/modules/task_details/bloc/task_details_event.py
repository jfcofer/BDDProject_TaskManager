class TaskDetailsEvent():
    pass

class TaskDetailsSubscriptionRequested(TaskDetailsEvent):
    def __init__(self) -> None:
        super().__init__()