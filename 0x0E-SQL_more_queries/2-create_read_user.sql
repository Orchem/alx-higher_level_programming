-- creates database hbtn_0d_2 and user user_0d_2
-- user_0d_2 have SELECT privilege in database hbtn_0d_2
-- script does not fail if user or database exists;
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
GRANT SELECT ON hbtn_0d_2.*
	TO 'user_0d_2'@'localhost'
	IDENTIFIED BY 'user_0d_2_pwd';

