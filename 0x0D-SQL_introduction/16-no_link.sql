-- scripts list all records of the table second_table from database
-- The database name will be passed as an argument of the mysql command
-- records without names are not displayed
-- records are arranged in descending order by score
-- result is displayed as score and name
SELECT score, name FROM second_table WHERE name != "NULL" ORDER BY score DESC;

