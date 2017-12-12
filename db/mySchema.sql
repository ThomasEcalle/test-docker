DROP DATABASE IF EXISTS `test`;
CREATE DATABASE test;
USE test;

CREATE TABLE user (
    id int AUTO_INCREMENT,
    name varchar(255),
	PRIMARY KEY (id)
);
INSERT INTO user (name) VALUES ('Ecalle');
INSERT INTO user (name) VALUES ('Pougetoux');
INSERT INTO user (name) VALUES ('Phee');
INSERT INTO user (name) VALUES ('Babar');