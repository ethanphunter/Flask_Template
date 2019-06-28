-- FILE: init.sql
-- DATABASE: flask-template-db
-- AUTHOR: Ethan Hunter
-- CREATED: 2019-05-11
-- UPDATED: Null
begin;

CREATE USER username WITH PASSWORD 'password';

CREATE TABLE Books(
  id          int PRIMARY KEY NOT NULL,
  title       TEXT            NOT NULL,
  authorId    int             NOT NULL);

GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO username;
commit;
