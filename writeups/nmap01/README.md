# Room
https://tryhackme.com/room/nmap01

# Task 1 - Intro
Intro

# Task 2 - Subnetworks
* A network segment is a group of computers connected to a shared medium
* A subnetwork is a one or more network segments connected together via the same router, a logical separation
* ARP is used to map MAC addresses to IP addresses
* ARP is a layer 2 protocol and uses broadcasts on the local network

# Task 3 - Enumerating Targets
* Target specifications
    * list 
    * range
    * subnet
    * input file : nmap -iL hosts.txt
    * nmap -sL targets
    * -n : no DNS

# Task 4 - Discovering Live Hosts
* ARP - layer 2
    * ARP request
    * ARP response
* ICMP - layer 3
    * type 8 - echo
    * type 0 - echo reply
* TCP, UDP - layer 4

# Task 5 - Nmap host discovery using ARP
* nmap host discovery
    * privileged user - local network - arp requests
    * privileged user - remote network - ICMP, TCP ACK, TCP SYN, ICMP timestamp
    * unprivileged user - either network - TCP 3-Way handshake
* nmap ARP scan
    * nmap -PR -sn [network]
* arp-scan
    * arp scan is a purpose built tool that does arp scanning
    * arp-scan -l
    * sudo arp-scan -I eth0 -l

# Task 6 - Nmap host discovery using ICMP
* nmap
    * -sn : disable port scanning
    * -pp : ICMP timestamp request
    * -pm : ICMP address mask discovery
    * -pe : ICMP echo discovery

# Task 7 - Nmap host discovery using TCP and UDP
* nmap
    * -ps : TCP SYN ping
    * -pa : TCP ACK ping
    * -pu : UDP ping
* masscan
    * apt install masscan

# Task 8 - Reverse DNS lookup
* nmap
    * -n : skip DNS lookup
    * -r : query DNS server for all hosts
    * --dns-servers [server] : specify a DNS server to use for lookups

# Task 9 - Summary
Summary