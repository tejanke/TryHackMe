# Room
https://tryhackme.com/room/dnsindetail

# Task 1 - What is DNS?
DNS stands for the Domain Name System (or Service).  DNS provides a simple way to communicate with IP based devices without having to remember or program IP addresses for those devices.  DNS translates domain names to IP addresses

# Task 2 - Domain Hierarchy
TLDs
* TLD = Top Level Domain
* The TLD is the right most part of a domain, so .com, or .org
* Two types
  * gTLD - generic top level domain : .com, .org
  * ccTLD - country code top level domain : .ca, .co.uk
* List
  * https://data.iana.org/TLD/tlds-alpha-by-domain.txt

Second Level Domain
* limited to 63 characters plus the TLD
* can only use a-z and 0-9
  * hyphens are allowed but a name cannot start with one, end with one, or be used consecutively
* google.com : google is the second level domain

Subdomain
* left side of the second level domain
* www.google.com : www is the subdomain
* can only use a-z and 0-9
  * hyphens are allowed but a name cannot start with one, end with one, or be used consecutively
* you can use multiple subdomains split with periods
  * maximum length of the entire domain name is 253 characters
  * a.b.c.com

# Task 3 - DNS Record Types
Record Types
* A
  * resolve to IPv4 addresses
* AAAA
  * resolve to IPv6 addresses
* CNAME
  * resolve to another domain name
  * a.b.com > d.e.com
* MX
  * resolve to the email server for the domain
  * contains a priority so multiple can be defined
* TXT
  * multiple uses
  * can list servers that have authority to send an email
  * can verify ownership of the domain

# Task 4 - Making a DNS request
DNS Request semi-simplified
* client opens web browser to www.google.com
  * check localhost DNS cache
  * check localhost browser DNS cache (not all browsers do this)
  * check localhost hosts file
  * check configured DNS servers
  * DNS timeout
* configured DNS server
  * usually provided by your ISP
  * check local server cache
  * check root servers
* root servers
  * identify .com TLD server
* TLD servers
  * identify authoritative google.com nameserver
* Authoritative google.com nameserver
  * check for www subdomain
  * respond to configured DNS server
* configured DNS server
  * configured DNS server caches the IP address for www.google.com
  * cache is only good for the configured TTL
  * configured DNS server responds to client with the IP address for www.google.com
* client receives DNS answer
  * client caches the IP address for www.google.com
  * cache is only good for the configured TTL
  * web browser connects to www.google.com and displays the web page

# Task 5 - Practical
Use an example website to answer DNS based questions