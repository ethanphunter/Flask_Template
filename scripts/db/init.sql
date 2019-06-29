-- FILE: init.sql
-- DATABASE: flask-template-db
-- AUTHOR: Ethan Hunter
-- CREATED: 2019-05-11
-- UPDATED: 2019-06-28
begin;

CREATE TABLE Books(
  id          int PRIMARY KEY NOT NULL,
  title       TEXT            NOT NULL,
  authorId    int             NOT NULL);

commit;
