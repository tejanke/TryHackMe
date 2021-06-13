# Room
https://tryhackme.com/room/catpictures

# Task 1 - Deploy
Deploy

# Task 2 - Flags

Enumeration - nmap
```
nmap -A -T4 10.10.44.205 | tee nmap.txt
Starting Nmap 7.91 ( https://nmap.org ) at 2021-06-13 13:36 EDT
Nmap scan report for 10.10.44.205
Host is up (0.22s latency).
Not shown: 998 closed ports
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 37:43:64:80:d3:5a:74:62:81:b7:80:6b:1a:23:d8:4a (RSA)
|   256 53:c6:82:ef:d2:77:33:ef:c1:3d:9c:15:13:54:0e:b2 (ECDSA)
|_  256 ba:97:c3:23:d4:f2:cc:08:2c:e1:2b:30:06:18:95:41 (ED25519)
8080/tcp open  http    Apache httpd 2.4.46 ((Unix) OpenSSL/1.1.1d PHP/7.3.27)
| http-open-proxy: Potentially OPEN proxy.
|_Methods supported:CONNECTION
|_http-server-header: Apache/2.4.46 (Unix) OpenSSL/1.1.1d PHP/7.3.27
|_http-title: Cat Pictures - Index page
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 25.44 seconds
```

Enumeration - browsing site
```
user@example.com
Total posts 1 • Total topics 1 • Total members 1 • Our newest member user

POST ALL YOUR CAT PICTURES HERE :)

Knock knock! Magic numbers: 1111, 2222, 3333, 4444

a9cc5101f329c9625a4702acec8de374
1111222233334444
http://10.10.44.205:8080/download/
```

Enumeration - gobuster
```
gobuster dir -w /usr/share/seclists/Discovery/Web-Content/big.txt -u http://10.10.44.205:8080 -t 10 | tee gobuster.txt
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.44.205:8080
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/seclists/Discovery/Web-Content/big.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Timeout:                 10s
===============================================================
2021/06/13 13:41:13 Starting gobuster in directory enumeration mode
===============================================================
/.htaccess            (Status: 403) [Size: 199]
/.htpasswd            (Status: 403) [Size: 199]
/adm                  (Status: 301) [Size: 237] [--> http://10.10.44.205:8080/adm/]
/assets               (Status: 301) [Size: 240] [--> http://10.10.44.205:8080/assets/]
/bin                  (Status: 301) [Size: 237] [--> http://10.10.44.205:8080/bin/]   
/cache                (Status: 403) [Size: 199]                                       
/config               (Status: 403) [Size: 199]                                       
/docs                 (Status: 301) [Size: 238] [--> http://10.10.44.205:8080/docs/]  
/download             (Status: 301) [Size: 242] [--> http://10.10.44.205:8080/download/]
/ext                  (Status: 301) [Size: 237] [--> http://10.10.44.205:8080/ext/]     
/feed                 (Status: 200) [Size: 1462]                                        
/files                (Status: 403) [Size: 199]                                         
/images               (Status: 301) [Size: 240] [--> http://10.10.44.205:8080/images/]  
/includes             (Status: 403) [Size: 199]                                         
/language             (Status: 301) [Size: 242] [--> http://10.10.44.205:8080/language/]
/licenses             (Status: 301) [Size: 242] [--> http://10.10.44.205:8080/licenses/]
/phpbb                (Status: 301) [Size: 239] [--> http://10.10.44.205:8080/phpbb/]   
/store                (Status: 403) [Size: 199]                                         
/styles               (Status: 301) [Size: 240] [--> http://10.10.44.205:8080/styles/]  
/vendor               (Status: 301) [Size: 240] [--> http://10.10.44.205:8080/vendor/]  
                                                                                        
===============================================================
2021/06/13 14:56:06 Finished
===============================================================
```

Enumeration - sqlmap
```
sqlmap -u http://10.10.44.205:8080 --forms --dump
```