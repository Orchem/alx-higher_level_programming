-- script lists all cities of california in hbtn_0d_usa database
-- result is sorted in ascending order using cities.id
-- database name is passed as argument of mysql statement
SELECT id, name FROM cities WHERE state_id = (
	SELECT id FROM states WHERE name = 'California'
) ORDER BY id;

