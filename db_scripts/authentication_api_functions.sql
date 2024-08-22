CREATE OR REPLACE FUNCTION authenticate_user(email VARCHAR)
RETURNS TABLE (id INT, email VARCHAR, first_name VARCHAR, last_name VARCHAR, password VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT u.id, u.email, u.first_name, u.last_name, u.password
    FROM "user" u
    WHERE u.email = email;
END;
$$ LANGUAGE plpgsql;

