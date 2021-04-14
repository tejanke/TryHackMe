# Room
https://tryhackme.com/room/hardeningbasicspart1

# Task 1 - Hardening Basics
Topics
* User Accounts
* Firewall Security
* SSH and Encryption
* Mandatory Access Control

Book Resources
* https://learning.oreilly.com/library/view/mastering-linux-security/9781788620307/

# Task 2 - User Accounts
* Principle of least privilege
* sudo
* complex passwords
* disabling root access
* locking down home directories

# Task 3 - Dangers of root
* Highest level user on the system able to do anything
* sudo

# Task 4 - Sudo part 1
* sudo - super user do, allows a non-root user to run applications as root
* allows non privileged users to perform tasks by entering their own passwords
* follows principle of least privilege
* requires membership in the sudo group
  * usermod -aG sudo [user]
  * useradd -G sudo [user]
* check the current user sudo permissions
  * sudo -l
  * visudo
    * opens /etc/sudoers
* user aliases

# Task 5 - Sudo part 2
* command aliases
  * maps specific commands that a user is allowed to run, useful for many different commands being referenced by one shortcut (alias)
* host aliases

# Task 6 - Disabling Root Access
There are three methods to restrict root access
* Disable the login shell
  * Edit /etc/passwd and change the shell command to /usr/sbin/nologin, this will will prevent users from using sudo -s
* Disable root SSH login  
  * Edit /etc/ssh/sshd_config.conf and uncomment the line PermitRootLogin, then change the value to no
* Disable root using PAM
  * PAM is the password authentication module 
  * You will modify /etc/pam.d or /etc/pam.conf
Beyond the methods above you can also disable shell escaping by possibly using sudoedit instead of vim for example

# Task 7 - Locking Home Directories
Ubuntu's default permission for user home directories is 755.  This default can be modified in /etc/login.defs using UMASK values.  A UMASK value is like a wildcard mask. To get the effective permissions using a UMASK value of 022 you subtract the UMASK value from 777:
```
  777 (max permission)
- 022 (UMASK)
  ---
  755 (effective permission)
```

# Task 8 - Configure Password Complexity
PAM allows you to configure password complexity using the pwquality module.  You can install it using sudo apt install libpam-pwquality.  Configure it using pwquality.conf in /etc/security

# Task 9 - Configuring Other Password Requirements
Four important password attributes are:
* Expiration
  * Configured in the password aging section of /etc/login.defs
* History
  * Configured using /etc/pam.d/common-password
* Complexity
* Length

# Task 10 - Dangers of lxd group
By default Ubuntu places users in the lxd group which is a known privilege escalation point, users should be removed from this group unless absolutely needed

# Task 11 - Quiz
Answer quiz questions

# Task 12 - Firewalls
Firewall - a network security device that monitors incoming and outgoing network traffic and decides whether to allow or block specific traffic based on a defined set of security rules

Types of firewalls
* Host Based
  * Installed on the Operating System
* Network Based
  * A physical appliance

WAFs - typically a web based application aware firewall

# Task 13 - iptables
iptables is the frontend for netfilter.  netfilter is the backend firewall included in all Linux distros.  Ubuntu uses ufw as a frontend to netfilter

Components of iptables
* filter table - basic protection
* NAT table - keeps track of NAT sessions
* Mangle table - keeps track of mangling
* Security table - used for SELinux

View the current iptables with sudo iptables -L

iptables chain actions
* INPUT - packets inbound
* FORWARD - packets sent to another NIC or network
* OUTPUT - packets outbound

# Task 14 - iptables configuration
Security rules are commonly referred to as ACLs, they are read and applied in order, top down

Basic command walkthrough
```
sudo iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELEATED -j ACCEPT

* -A INPUT - append to the INPUT chain
* -m conntrack - call the conntrack module to keep track of connections
* --ctstate ESTABLISHED,RELATED - keeps track of connections that are already ESTABLISHED and connections RELATED to the already ESTABLISHED connections
* -j ACCEPT - the j stands for jump, and the packet will be accepted, stop processing other rules
```

Port command walkthrough
```
sudo iptables -A INPUT -p tcp --dport ssh -j ACCEPT

* -p {protocol} - which protocol to use
* --dport - controls the destination port
```

Block command walkthrough
```
sudo iptables -A INPUT -p tcp --dport smb -j DROP

* j DROP - the packet will be dropped, stop processing other rules
```

Saving configuration
```
sudo iptables-save
```

# Task 15 - ufw and a quiz
By default ufw is disabled

ufw commands
* sudo ufw status - check firewall status
* sudo ufw enable - enable the firewall
* sudo ufw disable - disable the firewall
* sudo ufw allow 9000/tcp - allow TCP port 9000
* sudo ufw deny 23/tcp - block TCP port 23

Answer quiz questions and fin