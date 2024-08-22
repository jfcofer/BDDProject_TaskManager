CREATE OR REPLACE FUNCTION authenticate_user(p_email VARCHAR) RETURNS TABLE (
        id INT,
        email VARCHAR,
        first_name VARCHAR,
        last_name VARCHAR
    ) LANGUAGE plpgsql SECURITY DEFINER AS $$ BEGIN RETURN QUERY
SELECT u.id,
    u.email,
    u.first_name,
    u.last_name,
    u.password
FROM "user" u
WHERE u.email = p_email;
END;
$$;
CREATE OR REPLACE FUNCTION register_user(
        p_email VARCHAR,
        p_hashed_password VARCHAR,
        p_first_name VARCHAR,
        p_last_name VARCHAR
    ) RETURNS VOID LANGUAGE plpgsql SECURITY DEFINER AS $$ BEGIN
INSERT INTO "user" (email, password, first_name, last_name)
VALUES (
        p_email,
        p_hashed_password,
        p_first_name,
        p_last_name
    );
END;
$$;