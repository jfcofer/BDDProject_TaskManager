class DashboardEvent():
    pass

class DashboardSubscriptionRequested(DashboardEvent):
    def __init__(self) -> None:
        super().__init__()
