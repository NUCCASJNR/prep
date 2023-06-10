-- Write a script that prepares a MySQL server for the project:

-- A database alareef_dev_db
-- A new user alareef_dev (in localhost)
-- The password of alareef_dev should be set to alareef_dev_pwd
-- alareef_dev should have all privileges on the database alareef_dev_db (and only this database)
-- hbnb_dev should have SELECT privilege on the database performance_schema (and only this database)
-- If the database alareef_dev_db or the user alareef_dev already exists, your script should not fail

CREATE DATABASE IF NOT EXISTS alareef_dev_db;
CREATE USER IF NOT EXISTS alareef_dev@'localhost' IDENTIFIED BY 'alareef_dev_pwd';
GRANT ALL PRIVILEGES ON alareef_dev_db.* TO alareef_dev@'localhost';
GRANT SELECT ON performance_schema.* TO alareef_dev@'localhost';
