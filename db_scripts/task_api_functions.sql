-- Function to get tasks for a user
CREATE OR REPLACE FUNCTION get_tasks_for_user(p_user_id INT) RETURNS TABLE (
        id INT,
        title VARCHAR,
        description TEXT,
        due_date DATE,
        status status,
        priority priority,
        user_id INT
    ) LANGUAGE plpgsql SECURITY DEFINER AS $$ BEGIN RETURN QUERY
SELECT id,
    title,
    description,
    due_date,
    current_status,
    current_priority,
    user_id
FROM task_view
WHERE user_id = p_user_id;
-- Use parameter name with prefix
END;
$$;
-- Function to save a task
CREATE OR REPLACE FUNCTION save_task(
        p_user_id INT,
        p_title VARCHAR,
        p_description TEXT,
        p_due_date DATE,
        p_status status,
        p_priority priority
    ) RETURNS VOID LANGUAGE plpgsql SECURITY DEFINER AS $$ BEGIN
INSERT INTO task (
        user_id,
        title,
        description,
        due_date,
        current_status,
        current_priority
    )
VALUES (
        p_user_id,
        p_title,
        p_description,
        p_due_date,
        p_status,
        p_priority
    );
END;
$$;
-- Function to update a task
CREATE OR REPLACE FUNCTION update_task(
        p_task_id INT,
        p_title VARCHAR,
        p_description TEXT,
        p_status status,
        p_priority priority
    ) RETURNS VOID LANGUAGE plpgsql SECURITY DEFINER AS $$ BEGIN
UPDATE task
SET title = p_title,
    description = p_description,
    current_status = p_status,
    current_priority = p_priority
WHERE id = p_task_id;
-- Use parameter name with prefix
END;
$$;
-- Function to delete a task
CREATE OR REPLACE FUNCTION delete_task(p_task_id INT) RETURNS VOID LANGUAGE plpgsql SECURITY DEFINER AS $$ BEGIN
DELETE FROM task
WHERE id = p_task_id;
-- Use parameter name with prefix
END;
$$;
-- Function to get subtasks for a task
CREATE OR REPLACE FUNCTION get_subtasks_for_task(p_task_id INT) RETURNS TABLE (
        id INT,
        title VARCHAR,
        status status,
        priority priority,
        main_task_id INT
    ) LANGUAGE plpgsql SECURITY DEFINER AS $$ BEGIN RETURN QUERY
SELECT id,
    title,
    current_status,
    current_priority,
    main_task_id
FROM subtask_view
WHERE main_task_id = p_task_id;
-- Use parameter name with prefix
END;
$$;
-- Function to save a subtask
CREATE OR REPLACE FUNCTION save_subtask(
        p_main_task_id INT,
        p_title VARCHAR,
        p_status status,
        p_priority priority
    ) RETURNS VOID LANGUAGE plpgsql SECURITY DEFINER AS $$ BEGIN
INSERT INTO subtask (
        main_task_id,
        title,
        current_status,
        current_priority
    )
VALUES (p_main_task_id, p_title, p_status, p_priority);
END;
$$;
-- Function to update a subtask
CREATE OR REPLACE FUNCTION update_subtask(
        p_subtask_id INT,
        p_title VARCHAR,
        p_status status,
        p_priority priority
    ) RETURNS VOID LANGUAGE plpgsql SECURITY DEFINER AS $$ BEGIN
UPDATE subtask
SET title = p_title,
    current_status = p_status,
    current_priority = p_priority
WHERE id = p_subtask_id;
-- Use parameter name with prefix
END;
$$;
-- Function to delete a subtask
CREATE OR REPLACE FUNCTION delete_subtask(p_subtask_id INT) RETURNS VOID LANGUAGE plpgsql SECURITY DEFINER AS $$ BEGIN
DELETE FROM subtask
WHERE id = p_subtask_id;
-- Use parameter name with prefix
END;
$$;
-- Function to get reminders for a task
CREATE OR REPLACE FUNCTION get_reminders_for_task(p_task_id INT) RETURNS TABLE (
        id INT,
        description VARCHAR,
        reminder_date DATE,
        task_id INT
    ) LANGUAGE plpgsql SECURITY DEFINER AS $$ BEGIN RETURN QUERY
SELECT id,
    description,
    reminder_date,
    task_id
FROM reminder_view
WHERE task_id = p_task_id;
-- Use parameter name with prefix
END;
$$;
-- Function to save a reminder
CREATE OR REPLACE FUNCTION save_reminder(
        p_task_id INT,
        p_description VARCHAR,
        p_reminder_date DATE
    ) RETURNS VOID LANGUAGE plpgsql SECURITY DEFINER AS $$ BEGIN
INSERT INTO reminder (task_id, description, reminder_date)
VALUES (p_task_id, p_description, p_reminder_date);
END;
$$;
-- Function to delete a reminder
CREATE OR REPLACE FUNCTION delete_reminder(p_reminder_id INT) RETURNS VOID LANGUAGE plpgsql SECURITY DEFINER AS $$ BEGIN
DELETE FROM reminder
WHERE id = p_reminder_id;
-- Use parameter name with prefix
END;
$$;