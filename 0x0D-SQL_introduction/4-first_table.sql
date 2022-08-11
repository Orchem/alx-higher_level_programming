-- creates a table called first_table in the current MySQL server
-- script does not fail if table exists
-- database name is passed as mysql argument
CREATE TABLE IF NOT EXISTS first_table (id INT, name VARCHAR(256));

