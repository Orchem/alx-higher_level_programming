-- script lists the number of records with the same score in the table second_table
-- The database name will be passed as an argument of the mysql command
-- number of records is displayed with label number
-- list is sorted in descending order using number of records
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY number DESC;

