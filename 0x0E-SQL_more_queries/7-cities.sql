-- creates hbtn_0d_usa database and cities table in hbtn_0d_usa
-- script does not fail if htbn_0d_usa exists or if cities exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
	id INT PRIMARY KEY AUTO_INCREMENT,
	state_id INT,
	name VARCHAR(256) NOT NULL,
	FOREIGN KEY(state_id) REFERENCES hbtn_0d_usa.states(id)
);

