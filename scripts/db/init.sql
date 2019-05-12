-- FILE: init.sql
-- DATABASE: flask-template-db
-- AUTHOR: Ethan Hunter
-- CREATED: 2019-05-11
-- UPDATED: Null
begin;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO username;

CREATE TABLE Books(
  id          int PRIMARY KEY NOT NULL,
  title       TEXT            NOT NULL,
  authorId    int             NOT NULL);

commit;
