# Room
https://tryhackme.com/room/learncyberin25days

# Task 1 - Intro
Intro

# Task 2 - Get Connected
Get Connected

# Task 3 - Day 1 - Web Exploitation
* DNS
* IP
* HTTP/S
  * HTTP is an inherently stateless protocol, data does not persist
* Cookies
  * a constrcut that supports user state

Complete questions, CyberChef is your friend:
* https://gchq.github.io/CyberChef/

# Task 4 - Day 2 - Web Exploitation
* GET parameters
  * ?test=value
    * ? specifies the parameter name is coming next
    * test is the parameter name
    * = specifies the parameter value is coming next
    * value is the parameter value
  * ?test=value&test2=value2
    * ? specifies the parameter name is coming next
    * test is the parameter name
    * = specifies the parameter value is coming next
    * value is the parameter value
    * & specifies another parameter name is coming next
    * test2 is the next parameter name
    * = specifies the parameter value is coming next
    * value2 is the paramemter value
* File Uploads
  * file extension filtering is important
* Reverse Shells
* Reverse Shell Listeners

The questions are completed by using the information on the displayed web page.  You will also use file extension bypassing by changing the name of this reverseshell to .jpg.php

https://raw.githubusercontent.com/pentestmonkey/php-reverse-shell/master/php-reverse-shell.php

After the file is uploaded you can start your listener with nc -nvlp and then execute the reverse shell and grab the flag