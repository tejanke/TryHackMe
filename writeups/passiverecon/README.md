# Room
https://tryhackme.com/room/passiverecon

# Task 1 - Intro
Intro

# Task 2 - Passive vs Active Recon
* Recon - preliminary survey to gather information about a target
* Passive Recon - relying on publicly available knowledge without directly engaging the target
    * looking up DNS records
    * checking job ads
    * reading news articles
* Active Recon - direct engagement with the target
    * connecting to a web site, FTP server, etc
    * social engineering
* Resources
    * https://www.unifiedkillchain.com/

# Task 3 - Whois
* Whois is a request response protocol
* Follows RFC 3912
* Registrar responsible maintains whois records for the domain
* whois tryhackme.com

# Task 4 - nslookup and dig
* nslookup and dig returns DNS records from the command line
* nslookup tryhackme.com
* nslookup -type=TXT tryhackme.com
* dig tryhackme.com MX

# Task 5 - DNSDumpster
* DNSDumpster is a free domain research tool that can help discover subdomains
* https://dnsdumpster.com/

# Task 6 - Shodan.io
* Shodan.io is a service that tries to connect to every reachable device online and builds a profile of them
* https://www.shodan.io

# Task 7 - Summary
Summary