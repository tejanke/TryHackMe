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