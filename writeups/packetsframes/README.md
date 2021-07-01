# Room
https://tryhackme.com/room/packetsframes

# Task 1 - Intro
* frame - layer 2 construct
  * mac addresses
* packet - layer 3 construct
  * ip addresses
  * headers
    * TTL - expiry timer for the packet
    * checksum - verify the integrity of the packet
    * source address - sender
    * destination address - receiver

# Task 2 - TCP/IP
* TCP - transmission control protocol
* TCP/IP model
  * application
  * transport
  * internet
  * network interface
* TCP advantages
  * connection orientated
  * guarantees data integrity
  * mutual synchronization
  * reliable
* TCP disadvantages
  * slow connections are a bottleneck
  * slower than UDP
* TCP headers
  * source port
  * destination port
  * source ip
  * destination ip
  * sequence number
  * ack number
  * checksum
  * data
  * flag
* TCP three-way handshake
  * SYN - initiate a connection request by sending ISN
  * SYN/ACK - responder acknowledges the requester ISN, responder sends ISN to requester
  * ACK - requester acknowledges responder ISN
* Other TCP flags
  * DATA - send data
  * FIN - cleanly close the connection
  * RST - abruptly end all communication
* Close a TCP connection
  * FIN - initiate a connection close
  * FIN/ACK - responder acknowledges connection close, responder requests to close
  * ACK - requester acknowledges responder request to close

# Task 3 - Practical - Handshake
Practical research on the three-way handshake

# Task 4 - UDP
* UDP - User Datagram Protocol
* UDP attributes
  * stateless
  * does not require a three-way handshake
  * fast
* UDP disadvantages
  * no data integrity from the protocol itself
  * unstable
* UDP header
  * TTL
  * source address
  * destination address
  * source port
  * destination port
  * data

# Task 5 - Ports 101
* Ports
  * 0 - 65535
  * 0 - 1024 : common ports
* A few well known common ports
  * 21 - FTP
  * 22 - SSH
  * 23 - Telnet
  * 80 - HTTP
  * 443 - HTTPS
  * 445 - SMB
  * 3389 - RDP

# Task 6 - Conclusion
Conclusion