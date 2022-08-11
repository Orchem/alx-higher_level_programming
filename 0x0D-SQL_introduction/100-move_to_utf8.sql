-- converts database htbn_0c_0 character set and collation to utf8
-- converts first_table table in htbn_0c_0 database character set to utf8
ALTER DATABASE hbtn_0c_0 CHARACTER SET = utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE hbtn_0c_0.first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

