# Room
https://tryhackme.com/room/sqlinjectionlm

# Task 1 - Intro
* SQL - Structured Query Language
* SQLi is an attack on a web app database sever that causes malicious queries to be executed

# Task 2 - What is a database
* A database is a way to electronically store collections of data in an oragnized manner
* Databases are controlled by a DBMS - Database management system
* There are two types of databases
    * Relational - stores information in tables, has unique IDs (primary key) that can link to other tables
        * MySQL, MS SQL, PostgreSQL
    * Non-Relational - doesn't use tables and doesn't have a specific layout
        * MongoDB, Cassandra, ElasticSearch
* Tables - made up of columns and rows - stores data
* Columns - the field identifying the type of data
* Rows - the actual data

# Task 3 - What is SQL
* SQL is a feature rich language used for querying databases
* Queries referred to statements
* Common commands
    * SELECT
        * select * from users;
    * UNION
        * select name, address from customers UNION select name, address from suppliers;
    * INSERT
        * insert into users (username, password) values ('bob', '123');
    * UPDATE
        * update users SET username='root', password='123' where username='admin';
    * DELETE
        * delete from users where username='abc';

# Task 4 - What is SQL injection?
* When user provided data gets included and executed by a SQL query
* The ; character is the end of a SQL statement

# Task 5 - in-band SQLi
* Same method used to exploit the vulnerability that is used to receive the result

# Task 6 - Authentication Bypass
Authentication Bypass

# Task 7 - Boolean Based
Boolean Based

# Task 8 - Time Based
Time Based
 
# Task 9 - Out of band SQLi
Out of band SQLi

# Task 10 - Remediation
* Input validation
* Prepared Statements