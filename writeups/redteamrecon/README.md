# Room
https://tryhackme.com/room/redteamrecon

# Task 1 - intro
* room tasks
    * types of recon activities
    * whois and dns recon
    * advanced searching
    * searching by image
    * google hacking
    * specialized search engines
    * recon-ng
    * maltego

# Task 2 - taxonomy of recon
* recon is divided into two parts
    * active recon - requires interacting with the target
        * port scan
    * passive recon - carried out by watching passively
        * OSINT
        * DNS, etc
* active recon
    * external - conducted outside the target network
    * internal - conducted inside the target network

# Task 3 - builtin tools
* whois
    * request and response protocol
    * RFC 3912
    * TCP 43
    * provides whois records for a domain
    * whois example.com
* nslookup
    * performs dns lookups
    * common among windows, linux, and macos
    * nslookup www.example.com
* dig
    * performs dns lookups
    * limited to linux based systems by default
    * dig dev.example.com
* host
    * performs dns lookups
    * limited to linux based systems by default
    * host portal.example.com
* traceroute
    * path taken to reach destination
    * limited to linux based systems by default
    * traceroute shop.example.com
* tracert
    * path taken to reach destination
    * limited to windows based systems by default
    * traceroute garage.example.com        

# Task 4 - advanced searching
* search syntax
    * "search phrase"
    * OSINT filetype:pdf
    * salary site:blog.tryhackme.com
    * pentest -site:example.com
    * walkthrough intitle:tryhackme
    * challenge inurl:tryhackme
* resources
    * google hacking database : https://www.exploit-db.com/google-hacking-database

# Task 5 - specialized search engines
* https://viewdns.info/
* https://threatintelligenceplatform.com/
* https://search.censys.io/
* https://www.shodan.io/
* https://cli.shodan.io/

# Task 6 - recon-ng
* recon-ng is a framework that helps automate OSINT work
    * https://github.com/lanmaster53/recon-ng

# Task 7 - maltego
* maltego blends mind mapping with OSINT
    * https://github.com/lanmaster53/recon-ng
* transform hub
    * https://www.maltego.com/transform-hub/

# Task 8 - summary
summary