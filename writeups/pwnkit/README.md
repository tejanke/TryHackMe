# Room
https://tryhackme.com/room/pwnkit

# Task 1 - intro
* CVE-2021-4034 is dubbed pwnkit and is a Local Privilege Escalation (LPE) vulnerability.
* Polkit is installed by default on every major distro of Linux

# Task 2 - background
* resources
    * https://www.qualys.com/2022/01/25/cve-2021-4034/pwnkit.txt
* polkit is part of the linux autorization system and determines whether you have the permissions to elevate
* pkexec
* pkexec useradd test12
* this local vulnerability is for certain versions of pkexec and occurs when the program doesn't handle command line arguments properly

# Task 3 - exploitation
* exploit poc
    * https://github.com/arthepsy/CVE-2021-4034
* this example uses GCONV_PATH variable to include a malicious shared object that calls /bin/sh
* gcc cve-2021-4034-poc.c -o exploit
* ./exploit

# Task 4 - remediations
* for distros that have patched, update the system
    * Ubuntu : sudo apt update && sudo apt upgrade
* for distros that have not patched
    * sudo chmod 0755 'which pkexec'

# Task 5 - conclusion
conclusion