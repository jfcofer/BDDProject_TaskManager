CREATE USER limited_user WITH PASSWORD 'limited_user';
GRANT EXECUTE ON ALL FUNCTIONS IN SCHEMA public TO limited_user;