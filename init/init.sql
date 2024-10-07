CREATE EXTENSION IF NOT EXISTS dblink;

-- Check if the 'auth_db' exists, and create it if it doesn't
DO $$ 
BEGIN
    IF NOT EXISTS (SELECT FROM pg_database WHERE datname = 'auth_db') THEN
        PERFORM dblink_exec('dbname=postgres', 'CREATE DATABASE auth_db');
    END IF;
END
$$;

-- Check if the 'account_db' exists, and create it if it doesn't
DO $$ 
BEGIN
    IF NOT EXISTS (SELECT FROM pg_database WHERE datname = 'account_db') THEN
        PERFORM dblink_exec('dbname=postgres', 'CREATE DATABASE account_db');
    END IF;
END
$$;
