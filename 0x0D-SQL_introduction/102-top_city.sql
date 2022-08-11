-- script displays average temperature (fahrenheit) by city
-- output is ordered by average temperature in descending order
-- database name is pass as mysql argument
SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE month = 7 OR month = 8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;

