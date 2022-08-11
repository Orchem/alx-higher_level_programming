-- script lists all cities contained in the database
-- results is sorted in ascending order by cities.id
-- the database name is passed as mysql argument
SELECT cities.id, cities.name, states.name FROM cities
	JOIN states WHERE states.id = cities.state_id ORDER BY cities.id;

