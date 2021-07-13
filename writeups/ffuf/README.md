# Room
https://tryhackme.com/room/ffuf

# Task 1 - Intro
ffuf - fuzz faster u fool, a tool for web enumeration, fuzzing, and directory brute forcing

* ffuf install instructions
  * https://github.com/ffuf/ffuf#installation
* seclists install instructions
  * https://github.com/danielmiessler/SecLists#install

# Task 2 - Basics
* help
  * ffuf -h
* minimum options
  * ffuf -u [url_here] -w [wordlist_here]
* default fuzzing keyword
  * FUZZ

example
```
ffuf -u http://10.10.66.77/FUZZ -w /usr/share/seclists/Discovery/Web-Content/big.txt 
```

# Task 3 - Finding pages and directories
Use ffuf to find common extensions, and then uses those extensions with your first pass of enumeration to find interesting files.  This will cut down on the potential scope of invalid extensions during your scan.  Next, search for directories

```
ffuf -u http://10.10.66.77/indexFUZZ -w /usr/share/seclists/Discovery/Web-Content/web-extensions.txt
```
```
ffuf -u http://10.10.66.77/FUZZ -w /usr/share/seclists/Discovery/Web-Content/raft-medium-directories-lowercase.txt
```

# Task 4 - Using filters
You can filter out HTTP status codes with -fc, match HTTP status codes with -mc, and filter or match a lot of other things like size, word count, and number of lines

```
ffuf -u http://MACHINE_IP/FUZZ -w /usr/share/seclists/Discovery/Web-Content/raft-medium-files-lowercase.txt -fr '/\..*'

ffuf -u http://MACHINE_IP/FUZZ -fc 403 -w /usr/share/seclists/Discovery/Web-Content/raft-medium-files-lowercase.txt -fr '/\..*'

ffuf -u http://MACHINE_IP/FUZZ -mc 200 -w /usr/share/seclists/Discovery/Web-Content/raft-medium-files-lowercase.txt -fr '/\..*'
```