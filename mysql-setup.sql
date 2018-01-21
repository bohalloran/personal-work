SET PASSWORD FOR 'root'@'localhost' = PASSWRD('P@ssw0rd');

CREATE DATABASE wordpress;

GRANT ALL PRIVILEGES ON wordpress.* TO 'wpuser'@'localhost' IDENTIFIED BY 'P@ssw0rd';

DROP DATABASE test;
