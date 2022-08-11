-- scripts that creates table unique_id
-- database name will be passed as mysql argument
-- script does not fail if table exists
CREATE TABLE IF NOT EXISTS unique_id (
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256)
);

