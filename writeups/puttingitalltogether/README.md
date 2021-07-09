# Room
https://tryhackme.com/room/puttingitalltogether

# Task 1 - Putting it all together
* Request web site > need IP > use DNS
* Use HTTP > HTML, JavaScript, CSS

# Task 2 - Other Components
* Load Balancers
  * distribute load across many servers
  * provides high availability
  * uses different algorithms
    * round robin
    * weighted
  * performs health checking to verify backend
* CDN
  * allows you to host static content as close as possible to the user
  * increases speed for the user experience
* Databases
  * stores data
  * used with the web to recall content information
  * can be plain text or complex cluster
  * examples
    * MySQL
    * MSSQL
    * MongoDB
    * GraphQL
    * Postgres
* WAF
  * sits between the web request and the web server
  * attempts to protect the server by analyzing web requests 

# Task 3 - How web servers work
A web server listens for incoming connections that utilize the HTTP protocol.  Examples of web server software include Apache, Nginx, and IIS.  Web servers can host a single web site or multiple using virtual hosts.  Virtual hosts use the host header in order to direct the traffic to the proper application.  Static content doesn't change.  Dynamic content does change, such as an interactive map or user poll.  Websites utilize many scripting langauges on the backend including PHP, Python, Ruby, and NodeJS

# Task 4 - Practical
Answer a quiz in the practical exam