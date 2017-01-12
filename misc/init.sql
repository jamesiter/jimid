DROP DATABASE IF EXISTS jimid;
CREATE DATABASE IF NOT EXISTS jimid;
USE jimid;

CREATE TABLE IF NOT EXISTS user(
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    login_name VARCHAR(30) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL,
    create_time BIGINT UNSIGNED NOT NULL,
    mobile_phone VARCHAR(13) NOT NULL DEFAULT '',
    email VARCHAR(30) NOT NULL DEFAULT '',
    mobile_phone_verified BOOLEAN NOT NULL DEFAULT FALSE,
    email_verified BOOLEAN NOT NULL DEFAULT FALSE,
    manager BOOLEAN NOT NULL DEFAULT FALSE,
    enabled BOOLEAN NOT NULL DEFAULT TRUE,
    PRIMARY KEY (id))
    ENGINE=InnoDB;

ALTER TABLE user ADD INDEX (login_name);
ALTER TABLE user ADD INDEX (mobile_phone);
ALTER TABLE user ADD INDEX (email);
INSERT INTO user (login_name, password, create_time, manager) VALUES
    ('admin', 'ji_pbkdf2$sha1$1000$Ji98s57956JcVrpwvnXKhC5kiJXZScv6$0e046371e16b913a78181f502c0b05fbadab6df5', UNIX_TIMESTAMP(NOW()) * 1000000, TRUE);


CREATE TABLE IF NOT EXISTS app_key(
  id CHAR(16) NOT NULL,
  secret CHAR(32) NOT NULL,
  create_time BIGINT UNSIGNED NOT NULL,
  name VARCHAR(255) NOT NULL DEFAULT '',
  remark VARCHAR(1024) NOT NULL DEFAULT '',
  PRIMARY KEY (id))
  ENGINE=InnoDB;

ALTER TABLE app_key ADD INDEX (id);
ALTER TABLE app_key ADD INDEX (name);
ALTER TABLE app_key ADD INDEX (remark);


CREATE TABLE IF NOT EXISTS uid_openid_mapping(
    uid BIGINT UNSIGNED NOT NULL,
    appid CHAR(30) NOT NULL,
    openid VARCHAR(30) NOT NULL,
    create_time BIGINT UNSIGNED NOT NULL,
    PRIMARY KEY (uid, appid, openid))
    ENGINE=InnoDB;

ALTER TABLE uid_openid_mapping ADD INDEX (uid, appid);
ALTER TABLE uid_openid_mapping ADD INDEX (appid, openid);

