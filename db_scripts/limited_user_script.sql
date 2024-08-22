CREATE USER limited_user WITH PASSWORD 'limited_user';
GRANT USAGE ON SCHEMA public TO limited_user;
GRANT SELECT,
    INSERT,
    UPDATE,
    DELETE ON user_view TO limited_user;
GRANT SELECT,
    INSERT,
    UPDATE,
    DELETE ON report_view TO limited_user;
GRANT SELECT,
    INSERT,
    UPDATE,
    DELETE ON task_view TO limited_user;
GRANT SELECT,
    INSERT,
    UPDATE,
    DELETE ON subtask_view TO limited_user;
GRANT SELECT,
    INSERT,
    UPDATE,
    DELETE ON reminder_view TO limited_user;