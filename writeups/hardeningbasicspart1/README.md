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