# Room
https://tryhackme.com/room/protocolsandservers

# Task 1 - Intro
* Intro to protocols
    * HTTP
    * FTP
    * POP3
    * SMTP
    * IMAP

# Task 2 - Telnet
* Telnet is a cleartext protocol used for remote terminal access, it used TCP port 23

# Task 3 - HTTP
* HTTP - Hypertext Transfer Protocol
* HTTP is a cleartext protocol that serves web pages and other related content.  It works using the TCP port 80
* HTTP is a request/response protocol
* You can use telnet to forge an HTTP request and receive a response
    * telnet 1.2.3.4 80
    * GET / HTTP/1.1
    * host: telnet
    * [enter twice]
* Popular HTTP servers include
    * nginx
    * IIS
    * apache
* Popular HTTP clients include
    * firefox
    * chrome
    * edge

# Task 4 - FTP
* FTP - File Transfer Protocol
* FTP is a cleartext protocol that is used for file transfers.  It uses TCP ports 20 and 21
* FTP has two modes
    * Active - client connects to TCP port 21 on the server (control channel), data is sent over TCP port 20 on the server (data channel)
    * Passive - client connects to TCP port 21 on the server (control channel), data is sent from the client with a port above TCP 1023 (data channel)
* Popular FTP servers include
    * vsftpd
    * proftpd
* FTP clients include
    * ftp
    * filezilla

# Task 5 - SMTP
* Email is one of the most used services on the Internet
* Email delivery has the following components
    * mail submission agent - msa
    * mail transfer agent - mta
    * mail delivery agent - mda
    * mail user agent - mua
* Email delivery mostly follows the path below
    * a user creates an email and sends it using a MUA to the MSA
    * the MSA is an email server and pre-processes the email to verify integrity
    * after the pre-processing is done, the MSA transfers the email to the MTA
    * the MTA is almost always the same server as the MSA
    * the MTA sends the email to the MTA of the recipient
    * the recipient MTA receives the email and sends it to the MDA
    * the MDA is almost always the same server as the MTA
    * the recipient connects to the MDA to grab email
* Three common protocols for email include
    * SMTP - sending emails
    * POP3 - receiving emails
    * IMAP - receiving emails
* SMTP is a cleartext protocol that uses TCP port 25 to send email
* SMTP is used by the MUA to send an email message to the MSA

# Task 6 - POP3
* POP3 is a cleartext protocol that uses TCP port 110 to retrieve email
* POP3 is used by the MUA to receive an email message from the MDA

# Task 7 - IMAP
* IMAP is a cleartext protocol that uses TCP port 143 to retrieve email
* IMAP is used by the MUA to receive an email message from the MDA

# Task 8 - Summary
Summary