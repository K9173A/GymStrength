CREATE DATABASE gymstrength;
CREATE USER admin with PASSWORD ':v1';
GRANT ALL PRIVILEGES ON DATABASE gymstrength TO admin;
ALTER ROLE admin SET CLIENT_ENCODING TO 'UTF8';
ALTER ROLE admin SET default_transaction_isolation TO 'READ COMMITTED';
ALTER ROLE admin SET TIME ZONE 'Europe/Moscow';