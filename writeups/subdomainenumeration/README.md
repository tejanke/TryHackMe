# Room
https://tryhackme.com/room/subdomainenumeration

# Task 1 - Intro
* Subdomain enumeration is the process of finding valid subdomains for a domain
* Enumeration methods
    * Brute Force
    * OSINT
    * Virtual Host

# Task 2 - OSINT - SSL/TLS Certificates
* There are publicly accessible logs of every SSL/TLS certificate created for a domain name found in Certificate Transparency log sources
* CT logs
    * https://crt.sh/
    * https://transparencyreport.google.com/https/certificates

# Task 3 - OSINT - Search Engines
* You can use Google dorks to research and find more subdomains
* Example
    * -site:www.domain.com site:*.domain.com

# Task 4 - DNS Brute force
* DNS brute forcing is trying a combination of thousands of possible subdomains for a domain looking for results

# Task 5 - OSINT - sublist3r
* sublist3r is an automated tool that speeds up subdomain discovery

# Task 6 - Virtual Hosts
* subdomains don't have to have a DNS record, they could be accessed via hosts file and the web server may process them using a virtual host
* the web server will process a virtual host using the host header "Host:"
* ffuf fuzzing example
    * ffuf -w /usr/share/wordlists/SecLists/Discovery/DNS/namelist.txt -H "Host: FUZZ.acmeitsupport.thm" -u http://10.10.116.37