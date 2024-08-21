class TaskRepository:
    def __init__(self, db_connector):
        self.db_connector = db_connector

    def get_tasks_for_user(self, user_id: int) -> List[Task]:
        tasks_data = self.db_connector.execute("CALL get_tasks_for_user(?)", (user_id,))
        tasks = []
        for task_data in tasks_data:
            subtasks = self.get_subtasks_for_task(task_data['id'])
            reminders = self.get_reminders_for_task(task_data['id'])
            tasks.append(Task(id=task_data['id'], title=task_data['title'], description=task_data['description'], 
                              due_date=task_data['due_date'], status=task_data['status'], priority=task_data['priority'],
                              subtasks=subtasks, reminders=reminders))
        return tasks

    def add_task_for_user(self, user_id: int, task: Task):
        task_data = self.db_connector.execute("CALL add_task(?, ?, ?, ?)", (user_id, task.title, task.status, task.priority))
        task.id = task_data['id']
        return task

    def get_subtasks_for_task(self, task_id: int) -> List[Subtask]:
        subtasks_data = self.db_connector.execute("CALL get_subtasks_for_task(?)", (task_id,))
        return [Subtask(id=subtask['id'], title=subtask['title'], status=subtask['status'], priority=subtask['priority']) for subtask in subtasks_data]

    def get_reminders_for_task(self, task_id: int) -> List[Reminder]:
        reminders_data = self.db_connector.execute("CALL get_reminders_for_task(?)", (task_id,))
        return [Reminder(id=reminder['id'], description=reminder['description'], reminder_date=reminder['reminder_date']) for reminder in reminders_data]

    def add_subtask_to_task(self, task_id: int, subtask: Subtask):
        subtask_data = self.db_connector.execute("CALL add_subtask(?, ?, ?, ?)", (task_id, subtask.title, subtask.status, subtask.priority))
        subtask.id = subtask_data['id']
        return subtask

    def add_reminder_to_task(self, task_id: int, reminder: Reminder):
        reminder_data = self.db_connector.execute("CALL add_reminder(?, ?, ?)", (task_id, reminder.description, reminder.reminder_date))
        reminder.id = reminder_data['id']
        return reminder
    




class AuthRepository:
    def __init__(self, db_connector):
        self.db_connector = db_connector

    def authenticate_user(self, email: str, password: str) -> Optional[User]:
        user_data = self.db_connector.execute("CALL authenticate_user(?, ?)", (email, password))
        if user_data:
            return User(id=user_data['id'], email=user_data['email'], first_name=user_data['first_name'], last_name=user_data['last_name'])
        return None

    def register_user(self, email: str, password: str, first_name: str, last_name: str) -> User:
        user_data = self.db_connector.execute("CALL register_user(?, ?, ?, ?)", (email, password, first_name, last_name))
        return User(id=user_data['id'], email=user_data['email'], first_name=user_data['first_name'], last_name=user_data['last_name'])





class UserRepository:
    def __init__(self, db_connector):
        self.db_connector = db_connector

    def get_user_by_id(self, user_id: int) -> User:
        user_data = self.db_connector.execute("CALL get_user_info(?)", (user_id,))
        reports_data = self.db_connector.execute("CALL get_user_reports(?)", (user_id,))
        reports = [Report(id=report['id'], creation_date=report['creation_date']) for report in reports_data]
        return User(id=user_data['id'], email=user_data['email'], first_name=user_data['first_name'], last_name=user_data['last_name'], reports=reports)

    def update_user(self, user: User):
        self.db_connector.execute("CALL update_user(?, ?, ?, ?)", (user.id, user.email, user.first_name, user.last_name))

    def get_reports_for_user(self, user_id: int) -> List[Report]:
        reports_data = self.db_connector.execute("CALL get_user_reports(?)", (user_id,))
        return [Report(id=report['id'], creation_date=report['creation_date']) for report in reports_data]

    def add_report_for_user(self, user_id: int, report: Report):
        self.db_connector.execute("CALL add_report(?, ?)", (user_id, report.creation_date))




