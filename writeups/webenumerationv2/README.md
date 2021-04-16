# Room
https://tryhackme.com/room/webenumerationv2

# Task 1 - Intro
Review of tools for web enumeration

# Task 2 - Manual Enumeration
Manual browsing will produce results.  Viewing source and your browser's developer console are very useful practices

# Task 3 - Intro to Gobuster
Gobuster is a web scanning application written in Go.  You can install it using sudo apt install gobuster.  A few useful flags are:
* -t - threads, default is 10
* -v - verbose
* -z - doesn't display progress
* -q - don't print banner or other items
* -o - write output to a file

# Task 4 - Gobuster modes
Gobuster has a few different modes.  First is dir mode, which allows you to scan for directories on the target.  In scanning through dir mode, Gobuster will return the directory name as well as an HTTP status code.

Example dir mode command:
```
gobuster dir -u http://1.2.3.4 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
```

Useful flags for dir mode:
* -c - use cookies
* -x - file extensions to search for
* -H - specify HTTP headers
* -k - skip TLS verification
* -n - don't print status codes
* -P - password to use for basic auth
* -s - print positive status codes
* -b - print negative status codes
* -U - username for basic auth

Example dir mode command with -x:
```
gobuster dir -u http://1.2.3.4 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x html,php,js
```

The second mode Gobuster offers is dns mode.  This mode allows Gobuster to brute force subdomains.  DNS mode is prefixed with gobuster dns

Example dns mode command:
```
gobuster dns -d http://mydomain.com -w /usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-5000.txt
```

Useful flags for dns mode:
```
-c - show CNAME records
-i - show IPs
-r - use a custom DNS server
```

The last mode Gobuster has is vhost mode.  This mode allows you to brute force virtual hosts on a target site.  vhost mode is prefixed with gobuster vhost

Example vhost mode command:
```
gobuster vhost -u http://mydomain.com -w /usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-5000.txt
```

# Task 5 - Useful wordlists
Kali has a lot of default wordlists installed at the /usr/share/wordlists directory including:
* /usr/share/wordlists/dirbuster
* /usr/share/wordlists/dirb

The best 3rd party wordlists come from Daniel Miessler
* https://github.com/danielmiessler/SecLists

# Task 6 - Gobuster Practical
Practical with Gobuster

# Task 7 - Intro to WPScan
WPScan is a framework that allows you to enumerate security vulnerabilities in WordPress, some of those include:
* Sensitive Information Disclosure
* Path Discovery
* Weak Password Policies
* Presence of Default Installation
* Testing of WAF

Installing WPScan
```
sudo apt update && sudo apt install wpscan
```

Updating the WPScan database
```
wpscan --update
```

# Task 8 - WPScan modes
WPScan can usually detect the theme that is running

```
wpscan --url http://site --enumerate t
```

WPScan can also enumerate the plugins that are installed

```
wpscan --url http://site --enumerate p
```

WPScan can enumerate users

```
wpscan --url http://site --enumerate u
```

WPScan detecting vulnerabilities

```
wpscan --url http://site --enumerate vp
```

WPScan and password attacks

```
wpscan --url http://site -passwords rockyou.txt -usernames user
```

WPScan flags
* --plugins-detection aggressive - the default is passive
* --enumerate p - plugins
* --enumerate t - themes
* --enumerate u - usernames
* --enumerate v - cross reference vulnerabilities

# Task 9 - WPScan Practical
Answer questions based on using WPScan against the challenge target