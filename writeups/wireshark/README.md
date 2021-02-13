# Room
https://tryhackme.com/room/wireshark

# Task 1 - Intro
Wireshark is a tool used for analyzing network packet captures

# Task 2 - Install
Download and install
* https://www.wireshark.org/

# Task 3 - Overview
Wireshark allows you to capture live using interfaces connected to your device or read packets from a PCAP file

# Task 4 - Collection Methods
You can capture traffic using many methods including
* Network taps
    * a physical implant
* MAC flooding
    * used by red teams to force a switch to send all frames to all ports where an operator can capture and review
* ARP poisoning
    * used by read teams to redirect traffic where an operator can become inline with the traffic flow and perform analysis

# Task 5 - Filtering Captures
A PCAP can be filtered to zero in on data that you want to analyze and remove the noise

Filtering Operators
* and: and / &&
* or: or / ||
* equals: eq / ==
* not equal: ne / !=
* greater than: gt / >
* less than: lt / <>

Filtering Resources
* https://www.wireshark.org/docs/wsug_html_chunked/ChWorkBuildDisplayFilterSection.html

Examples
* IP addresses
    * ip.addr == [ip]
    * ip.src == [src_ip]
    * ip.dst == [dst_ip]
    * ip.src == [src_ip] and ip.dst == [dst_ip]
* TCP ports
    * tcp.port eq [port]
* UDP ports
    * udp.port == [port]

# Task 6 - Packet Dissection
Wireshark dissects each packet in a PCAP file into a layer of the OSI model

Layers
* Frame - layer 1
* MAC - layer 2
* IP - layer 3
* Protocol - layer 4
* Protocol Errors
* Application - layer 5+

# Task 7 - ARP PCAP analysis
ARP is a layer 2 protocol that is used to connect IP and MAC addresses.  Traffic will consist of two operations: Request (1) and Reply (2).  Wireshark automatically identifies OUIs that it knows about when viewing a PCAP

# Task 8 - ICMP PCAP analysis
ICMP is used to analyze various nodes on a network, used with tools like ping and traceroute

ICMP request
* Type 8, Code 0
ICMP reply
* Type 0, Code 0

# Task 9 - TCP Traffic
TCP handles the delivery of packets including sequencing and errors.  TCP has a 3-way handshake: SYN, SYN/ACK, ACK.  TCP uses sequence numbers to keep track of packet flows

Wireshark setting
* Edit > Preferences > Protocols > TCP > Relative Sequence Numbers

# Task 10 - DNS PCAP analysis
The Domain Name Service protocol is used to resolve names with IPs.  In PCAP analysis pay attention to the query and the reply (answer)

# Task 11 - HTTP PCAP analysis
The Hypertext Transfer Protocol is used on the world wide web for web pages and other applications.  HTTP is plaintext, uses GET and POST methods among others, and is a request response protocol

Wireshark HTTP export
* File > Export Objects > HTTP

Protocol Analysis
* Statistics > Protocol Hierarchy

# Task 12 - HTTPS PCAP analysis
HTTPS is the secure encrypted version of HTTP.  It uses PKI to establish security and integrity for the data transported by it

HTTPS handshake overview
* Client and server agree on a protocol version
* Client and server select a cryptographic algorithm
* [optional] Client and server can authenticate to each other
* Create a secure tunnel

Wireshark import a private key
* Edit > Preferences > Protocols > TLS > RSA Keys List > Edit
    * Click +
    * Add the ip address of the host encrypting the traffic in the PCAP for which you have its private key
    * Add port: start_tls
    * Add protocol: http
    * Navigate to the private key file
    * OK

# Task 13 - Analyzing Exploit PCAPs
Review capture

# Task 14 - Conclusion
Documentation
* https://www.wireshark.org/docs/

Sample Captures
* https://wiki.wireshark.org/SampleCaptures

DFIR Madness practice
* https://dfirmadness.com/case-001-pcap-analysis/