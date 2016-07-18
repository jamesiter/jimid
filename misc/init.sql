DROP DATABASE IF EXISTS jimauth;
CREATE DATABASE IF NOT EXISTS jimauth;
USE jimauth;

CREATE TABLE IF NOT EXISTS auth(
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    login_name VARCHAR(30) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL,
    create_time BIGINT NOT NULL,
    mobile_phone VARCHAR(13) NOT NULL DEFAULT '',
    email VARCHAR(30) NOT NULL DEFAULT '',
    mobile_phone_verified BOOLEAN NOT NULL DEFAULT FALSE,
    email_verified BOOLEAN NOT NULL DEFAULT FALSE,
    enabled BOOLEAN NOT NULL DEFAULT TRUE,
    PRIMARY KEY (id))
    ENGINE=InnoDB;

ALTER TABLE auth ADD INDEX (login_name);
ALTER TABLE auth ADD INDEX (mobile_phone);
ALTER TABLE auth ADD INDEX (email);
INSERT INTO auth (login_name, password, create_time) VALUES
    ('admin', 'ji_pbkdf2$sha1$1000$Ji98s57956JcVrpwvnXKhC5kiJXZScv6$0e046371e16b913a78181f502c0b05fbadab6df5', unix_timestamp(now()))
