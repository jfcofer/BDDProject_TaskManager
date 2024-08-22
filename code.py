class TaskRepository(BaseRepository):
    def get_tasks_for_user(self, user_id: int) -> List[Task]:
        tasks_data = self._execute_stored_procedure("get_tasks_for_user", (user_id,))
        tasks = []
        for task_data in tasks_data:
            subtasks = self.get_subtasks_for_task(task_data['id'])
            reminders = self.get_reminders_for_task(task_data['id'])
            tasks.append(Task(id=task_data['id'], title=task_data['title'], description=task_data['description'], 
                              due_date=task_data['due_date'], status=task_data['status'], priority=task_data['priority'],
                              subtasks=subtasks, reminders=reminders))
        return tasks

    def add_task_for_user(self, user_id: int, task: Task):
        task_data = self._execute_stored_procedure("add_task", (user_id, task.title, task.status, task.priority))
        task.id = task_data[0]['id']
        return task

    def get_subtasks_for_task(self, task_id: int) -> List[Subtask]:
        subtasks_data = self._execute_stored_procedure("get_subtasks_for_task", (task_id,))
        return [Subtask(id=subtask['id'], title=subtask['title'], status=subtask['status'], priority=subtask['priority']) for subtask in subtasks_data]

    def get_reminders_for_task(self, task_id: int) -> List[Reminder]:
        reminders_data = self._execute_stored_procedure("get_reminders_for_task", (task_id,))
        return [Reminder(id=reminder['id'], description=reminder['description'], reminder_date=reminder['reminder_date']) for reminder in reminders_data]

    def add_subtask_to_task(self, task_id: int, subtask: Subtask):
        subtask_data = self._execute_stored_procedure("add_subtask", (task_id, subtask.title, subtask.status, subtask.priority))
        subtask.id = subtask_data[0]['id']
        return subtask

    def add_reminder_to_task(self, task_id: int, reminder: Reminder):
        reminder_data = self._execute_stored_procedure("add_reminder", (task_id, reminder.description, reminder.reminder_date))
        reminder.id = reminder_data[0]['id']
        return reminder