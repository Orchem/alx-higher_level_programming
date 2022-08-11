-- script creates table id_not_null on MySQL server
-- table contains a default value
-- database name will be passed as argument of the mysql command
-- script will not fail if table exists
CREATE TABLE IF NOT EXISTS id_not_null (
		id INT DEFAULT 1,
		name VARCHAR(256)
);

