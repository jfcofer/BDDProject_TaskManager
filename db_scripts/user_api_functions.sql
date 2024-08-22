-- Function to get user information
CREATE OR REPLACE FUNCTION get_user_info(p_user_id INT) RETURNS TABLE (
        id INT,
        email VARCHAR,
        first_name VARCHAR,
        last_name VARCHAR
    ) LANGUAGE plpgsql SECURITY DEFINER -- Add SECURITY DEFINER here
    AS $$ BEGIN RETURN QUERY
SELECT id,
    email,
    first_name,
    last_name
FROM user_view
WHERE id = p_user_id;
-- Use parameter name with prefix
END;
$$;
-- Function to update user information
create or replace function update_user(
        p_user_id INT,
        p_email VARCHAR,
        p_first_name VARCHAR,
        p_last_name VARCHAR
    ) returns VOID language plpgsql security definer -- Add SECURITY DEFINER here
    as $$ begin
update "user"
set email = p_email,
    -- Use parameter name with prefix
    first_name = p_first_name,
    -- Use parameter name with prefix
    last_name = p_last_name -- Use parameter name with prefix
where id = p_user_id;
-- Use parameter name with prefix
end;
$$;
-- Function to get user reports
CREATE OR REPLACE FUNCTION get_user_reports(p_user_id INT) RETURNS TABLE (
        id INT,
        creation_date DATE,
        user_id INT
    ) LANGUAGE plpgsql SECURITY DEFINER -- Add SECURITY DEFINER here
    AS $$ BEGIN RETURN QUERY
SELECT id,
    creation_date,
    user_id
FROM report_view
WHERE user_id = p_user_id;
-- Use parameter name with prefix
END;
$$;
-- Function to add a report
CREATE OR REPLACE FUNCTION add_report(p_creation_date DATE, p_user_id INT) RETURNS VOID LANGUAGE plpgsql SECURITY DEFINER -- Add SECURITY DEFINER here
    AS $$ BEGIN
INSERT INTO report (creation_date, user_id)
VALUES (p_creation_date, p_user_id);
-- Use parameter names with prefix
END;
$$;