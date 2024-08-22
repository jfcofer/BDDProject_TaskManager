CREATE OR REPLACE FUNCTION update_timestamp() RETURNS TRIGGER AS $$ BEGIN NEW.updated_at = CURRENT_TIMESTAMP;
RETURN NEW;
END;
$$ LANGUAGE plpgsql;
CREATE TRIGGER update_report_timestamp BEFORE
UPDATE ON report FOR EACH ROW EXECUTE FUNCTION update_timestamp();
CREATE TRIGGER update_task_timestamp BEFORE
UPDATE ON task FOR EACH ROW EXECUTE FUNCTION update_timestamp();
CREATE TRIGGER update_subtask_timestamp BEFORE
UPDATE ON subtask FOR EACH ROW EXECUTE FUNCTION update_timestamp();
CREATE TRIGGER update_reminder_timestamp BEFORE
UPDATE ON reminder FOR EACH ROW EXECUTE FUNCTION update_timestamp();

