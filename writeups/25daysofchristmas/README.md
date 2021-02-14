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