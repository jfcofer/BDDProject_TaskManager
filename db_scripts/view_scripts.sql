CREATE VIEW user_view AS
SELECT id,
    first_name,
    last_name,
    email
FROM user;
CREATE VIEW report_view AS
SELECT id,
    creation_date,
    user_id
FROM report;
CREATE VIEW task_view AS
SELECT id,
    title,
    description,
    due_date,
    current_status,
    current_priority,
    user_id
FROM task;
CREATE VIEW subtask_view AS
SELECT id,
    title,
    current_status,
    current_priority,
    main_task_id
FROM subtask;
CREATE VIEW reminder_view AS
SELECT id,
    description,
    reminder_date,
    task_id
FROM reminder;