download php (zib file),next extract file and cut the file and paste to c drive ,then create path
download xampp(open click start)
mysql sever and mysql workbanch

sql queries;

CREATE DATABASE user_auth_db;

USE user_auth_db;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
select *from users;