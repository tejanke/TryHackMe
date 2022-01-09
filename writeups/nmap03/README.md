# Room
https://tryhackme.com/room/nmap03

# Task 1 - Intro
* Advanced scanning techniques for
    * null scan
    * fin scan
    * xmas scan
    * maimon scan
    * ack scan
    * window scan
    * custom scan

# Task 2 - TCP null scan, fin scan, xmas scan
* null scan
    * no TCP flags are set - all 0
    * nmap -sN [target_ip]
    * if open or blocked by a firewall
        * no response
    * if closed
        * receive a RST
        * firewalls may silently drop with a RST        
    * requires elevated privileges to run this nmap scan
* fin scan
    * fin bit set
    * nmap -sF [target_ip]
    * if open or blocked by a firewall
        * no response
    * if closed
        * receive a RST
        * firewalls may silently drop with a RST
* xmas scan
    * sets fin, psh, and urg flags
    * nmap -sX [target_ip]
    * if open or blocked by a firewall
        * no response
    * if closed
        * receive a RST
        * firewalls may silently drop with a RST        

# Task 3 - TCP Maimon Scan
* maimon scan
    * fin and ack bits set
    * nmap -sM [target_ip]
    * open or closed
        * receive a RST
        * some BSD systems drop the packet if a port is open

# Task 4 - TCP ack, window, and custom scan
* ack scan
    * ack flag set
    * nmap -sA [target_ip]
    * open or closed
        * receive a RST
    * useful for detecting certain firewalls
* window scan
    * similar to ack scan, ack flag set
    * examines TCP window field of the returned RST packet
    * nmap -sW [target_ip]
    * useful for detecting certain firewalls
* custom scan
    * build your own custom flag set
    * --scanflags
    * nmap --scanflags RSTSYNFIN [target_ip]

# Task 5 - Spoofing and decoys
* IP spoofing only works in some network environments
* IP spoofing is only useful if you have some way to capture the packets destined to the spoofed IP address
* nmap -s [spoofed_ip] [target_ip]
* MAC spoofing only works when you are on the same local network as your target and other hosts
* MAC spoofing allows your scan to appear to be coming from multiple devices
* nmap -D [decoy1_ip], me [attacker_ip], [target_ip]

# Task 6 - Fragmented Packets
* firewalls are hardware or software
* firewalls block all traffic with exceptions or allow all traffic with exceptions
* older firewalls usually only inspect up to layer 4, newer firewalls inspect and filter up to layer 7
* ids can look at the content of packets and detect malicious activity
* nmap can fragment IP data packets
    * -f divides by 8
    * -ff divides by 16

# Task 7 - Idle Zombie Scan
* Idle scans utilize a host device that is not busy at all, no or very little traffic
* Idle scans will first trigger the idle host and record the current IP ID
* Idle scans will then scan the target IP but spoof the source IP with that of the idle host device
* Finally, the attacker again poll the idle host and record the current IP ID
* By comparing and contrasing the IP ID field you may discover open/closed ports on the original target
* This only works if the idle host is truly very low traffic
* nmap -sI [zombie_ip] [target_ip]

# Task 8 - More details
* --reason provides you with details as to why a port was open or close
* -v or -vv gives you more verbose output
* -d gives you debug level detail
* nmap -sS -F --reason [target_ip]

# Task 9 - Summary
* Summary