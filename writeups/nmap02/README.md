# Room
https://tryhackme.com/room/nmap02

# Task 1 - Intro
* Intro explaining
    * TCP connect scan
    * TCP SYN scan
    * UDP scan

# Task 2 - TCP and UDP Ports
* Two basic port states
    * Open - service is up and listening
    * Closed - service is down, not listening
* nmap port states
    * open - service is up and listening
    * closed - no service is listening or a firewall is blocking the scan
    * filtered - nmap can't determine if the port is open or closed, not accessible
    * unfiltered - port is accessible, but nmap can't determine if open or closed
    * open|filtered - nmap cannot determine whether port is open or filtered
    * closed|filtered -nmap cannot determine whether port is closed or filtered

# Task 3 - TCP Flags
* TCP header is 24 bytes
* Reference
    * https://datatracker.ietf.org/doc/html/rfc793.html
* TCP header breakdown
    * line 1 - source port 16 bits, destination port 16 bits
    * line 2 - sequence number 32 bits
    * line 3 - acknowledgement number 32 bits
    * line 4 - data offset 4 bits, reserved 6 bits, flags 6 bits, window 16 bits
    * line 5 - checksum 16 bits, urgent pointer 16 bits
    * line 6 - options 24 bits, padding 8 bits
    * line 7 - data begins : 32 bits
* TCP flags in order
    * URG - indicates urgent pointer field is used, incoming data is urgent and should be processed immediately
    * ACK - acknowledgement number filed is used, acknowledge recipt of TCP segment
    * PSH - ask TCP to pass data to the application
    * RST - reset the connection, firewalls may emit RSTs if there is a deny policy, a responding host may emit this flag when there is no service for the data
    * SYN - initiates TCP 3-way handshake, synchronize sequence numbers, sequence numbers should be set randomly
    * FIN - sender has no more data to send

# Task 4 - TCP connect scan
* A TCP connect scan works by completeing the TCP 3-way handshake
* TCP 3-way handshake
    * SYN
    * SYN, ACK
    * ACK
* To launch a TCP connect scan
    * nmap -sT [target_ip]
* TCP connect scan can run as an unprivileged user (non-root)
* TCP connect scan scans the 1000 most common ports in random order
* TCP connect scan will RST immediately if it detects the port is open
* The -F option enables fast mode and scans the 100 most common ports instead of the 1000 most common ports
* the -r option scans the ports in consecutive order instead of random

# Task 5 - TCP SYN scan
* TCP SYN scan is the default scan mode for nmap
* TCP SYN scans require a privileged user (root or sudo)
* TCP SYN scan does not complete the 3-way handshake
* TCP SYN scan is launched via
    * nmap -sS [target_ip]
* TCP SYN scan vs TCP connect scan results for an open port
    * connect scan
        * SYN
        * SYN, ACK
        * ACK
        * RST, ACK
    * SYN scan
        * SYN
        * SYN, ACK
        * RST

# Task 6 - UDP scan
* UDP is connectionless
* UDP scans return an ICMP port unreachable when the port is closed (type 3, code 3)
* UDP scans that do not return a response are considered open ports
* UDP scan is launched via
    * nmap -sU [target_ip]

# Task 7 - Fine Tuning your scans
* specifying ports
    * a list : -p22,23,30
    * a range : -p33-55
    * all ports : -p-
    * top 100 : -F
    * top 10 : --top-ports 10
* adjusting scan time and aggressiveness
    * -T0 : paranoid
    * -T1 : sneaky (used during real engagements)
    * -T2 : polite
    * -T3 : normal (default)
    * -T4 : aggressive
    * -T5 : insane
* rate limiting packets per second
    * --min-rate [number]
    * --max-rate [number]
* adjusting parallel scans
    * --min-parallelism [number_of_probes]
    * --max-parallelism [number_of_probes]

# Task 8 - Summary
Summary