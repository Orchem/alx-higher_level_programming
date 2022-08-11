-- script creates the table force_name
-- database will be pass as argument of mysql statement
-- script does not fail when table exists
CREATE TABLE IF NOT EXISTS force_name (
		id INT,
		name VARCHAR(256) NOT NULL
);

