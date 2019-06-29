-- FILE: init-user.sql
-- DATABASE: flask-template-db
-- AUTHOR: Ethan Hunter
-- CREATED: 2019-06-28
-- UPDATED: Null

begin;

CREATE USER username WITH PASSWORD 'password';

GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO username;
commit;
