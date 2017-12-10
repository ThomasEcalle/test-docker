create database test;
use test;

CREATE TABLE user
(
id INTEGER AUTO_INCREMENT,
name TEXT,
PRIMARY KEY (id)
) COMMENT='this is my user table';