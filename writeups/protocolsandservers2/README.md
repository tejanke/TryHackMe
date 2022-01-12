# Room
https://tryhackme.com/room/protocolsandservers2

# Task 1 - Intro
* Common Attacks
    * Sniffing attack
    * Man in the middle attack
    * Password attack
    * Taking advantage of vulnerabilities

* CIA
    * Confidentiality - keep communication secure
    * Integrity - assure data is accurate
    * Availability - make a service available
* DAD
    * Disclosure
    * Alteration
    * Destruction

# Task 2 - Sniffing Attack
* Sniffing refers to capturing packets
* There are many programs to capture packets including
    * tcpdump
    * wireshark
    * tshark
* tcpdump example
    * sudo tcpdump port 110 -A

# Task 3 - Man in the middle attack
* A man in the middle occurs when a victim is really talking to the attacker instead of the real destination
* Cleartext protocols like HTTP, FTP, and SMTP are very susceptible to man in the middle attacks
* Some software to carry out man in the middle attacks include
    * ettercap
    * bettercap

# Task 4 - Transport Layer Security - TLS
* TLS - Transport Layer Security
* SSL / TLS is a layer 6 protocol that is designed to secure communication via encryption
* SSL / TLS upgrades are available for many cleartext protocols including
    * HTTP > HTTPS
    * FTP > FTPS
    * SMTP > SMTPS
    * POP3 > POP3S
    * IMAP > IMAPS
    * DNS > DOT
* An SSL / TLS channel is built generally as follows
    * establish TCP connection
    * establish SSL / TLS connection
    * send data
* The basics of the SSL / TLS handshake
    1. ClientHello - sends supported algorithms
    2. ServerHello - sends selected algorithm, provides server certificate, 
    3. ServerKeyExchange - information to generate key
    4. ServerHelloDone - server done with negotiation
    5. ClientKeyExchange - information to generate key
    6. Client ChangeCipherSpec - client switches to secure communication
    7. Server ChangeCipherSpec - server switches to secure communication
    8. secure data flow begins

# Task 5 - SSH
* SSH - Secure Shell
* SSH allows
    * confirmation of remote server's identity
    * encrypted message exchange
    * both sides can detect data integrity issues
* SSH uses TCP port 22 and requires both a client and server
* Example SSH syntax
    * ssh abc@1.2.3.4
* SCP is the cp program used over SSH and allows you to copy securely
    * scp abc@1.2.3.4:file.txt .

# Task 6 - Password Attack
* Password attacks can be classified as
    * Password Guessing
    * Dictionary attacks
    * Brute force attacks
* Popular wordlists
    * rockyou.txt
    * seclists
* Common brute forcing tools
    * hydra
* Hydra examples
    * hydra -l username -P /usr/share/wordlists/rockyou.txt 1.2.3.4 ftp
    * hydra -l username -P /usr/share/wordlists/rockyou.txt 1.2.3.4 imap