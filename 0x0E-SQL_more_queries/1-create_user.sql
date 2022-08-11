-- scripts creats user_0d_1 on MySQL server
-- password is set to user_0d_1_pwd
-- script does not fail if user exists
GRANT ALL PRIVILEGES ON *.*
	TO 'user_0d_1'@'localhost'
	IDENTIFIED BY 'user_0d_1_pwd';

