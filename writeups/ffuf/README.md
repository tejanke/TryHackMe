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

# Task 5 - Fuzzing parameters
ffuf can be used to fuzz parameters in requests.  

```
ffuf -u 'http://10.10.253.28/sqli-labs/Less-1/?FUZZ=1' -c -w /usr/share/seclists/Discovery/Web-Content/burp-parameter-names.txt -fw 39
```

ffuf can read from stdout for a generated wordlist, in this case we are feeding it the values of 0 through 255

```
for i in {0..255}; do echo $i; done | ffuf -u 'http://10.10.253.28/sqli-labs/Less-1/?id=FUZZ' -c -w - -fw 33
```

ffuf can also be used with POST requests

```
ffuf -u http://10.10.253.28/sqli-labs/Less-11/ -c -w /usr/share/seclists/Passwords/Leaked-Databases/hak5.txt -X POST -d 'uname=Dummy&passwd=FUZZ&submit=Submit' -fs 1435 -H 'Content-Type: application/x-www-form-urlencoded' 
```

# Task 6 - Finding vhosts and subdomains
ffuf can be used to find subdomains, but it isn't as efficient as purpose built tools

```
ffuf -u http://FUZZ.tryhackme.com -c -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt
```

# Task 7 - Proxying traffic
You can proxy traffic with ffuf for pivoting or use in Burp Suite.  Examples:

```
 ffuf -u http://10.10.139.124/ -c -w /usr/share/seclists/Discovery/Web-Content/common.txt -x http://127.0.0.1:8080
 ffuf -u http://FUZZ.tryhackme.com -c -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt -replay-proxy http://127.0.0.1:8080
```

# Task 8 - Useful options
ffuf has many useful options, you can find them by using ffuf -h.  Some popular ones are -request for using a raw HTTP request file, -ic to strip comments, and -v for printing full URLs and redirection locations

# Task 9 - Conclusion
Conclusion