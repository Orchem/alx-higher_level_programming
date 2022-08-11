-- script that displays the max temperatures of each state
-- output is ordered by state name
-- database name is passed as mysql argument
SELECT state, MAX(value) as max_temp FROM temperatures GROUP BY state ORDER BY state LIMIT 3;

