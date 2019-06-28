-- FILE: init.sql
-- DATABASE: flask-template-db
-- AUTHOR: Ethan Hunter
-- CREATED: 2019-05-11
-- UPDATED: 2019-06-27
begin;

CREATE USER username WITH PASSWORD 'password';

CREATE TABLE books(
  id          int PRIMARY KEY NOT NULL,
  title       TEXT            NOT NULL,
  authorId    int             NOT NULL);

GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO username;
commit;
