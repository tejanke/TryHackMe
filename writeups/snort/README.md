# room
https://tryhackme.com/room/snort

# task 1 - intro
* snort is an open source rule based network intrusion detection and prevention system - NIDS/NIPS
* resources
    * https://www.snort.org/

# task 2 - material setup
* material setup

# task 3 - intro to ids/ips
* ids - intrusion detection system
    * passive monitoring solution
    * detects possible malicious activities and patterns, abnormal incidents, and policy violations
    * generates alerts
    * two types
        * nids - network intrusion detection system
            * monitors network traffic flow
        * hids - host intrustion detection system
            * monitors traffic on the host
* ips - intrusion prevention system
    * active solution
    * prevents possible malicious activities and patterns, abnormal incidents, and policy violations
    * responsible for stopping / preventing / terminating the suspicous event
    * four types
        * nips
            * network intrusion prevention system
                * protects at the network traffic flow level
        * nba
            * network behavior analysis
                * protects based on behaviorial analysis of the traffic
        * wips
            * wireless intrusion prevention system
                * protects at the wireless network traffic flow level
        * hips
            * host-based intrusion prevention system
                * protects at the host level
* detection and prevention techniques
    * signature-based - rules that identify specific patterns in known malicious behavior
    * behavior-based - helps detect previously unknown threats through comparison of known models with the behavior displayed
    * policy-based - compares detected activities with system configuration and security policies

# task 4 - practical - interaction with snort
* practical
* get version
    ```
    snort -V

    ,,_     -*> Snort! <*-
    o"  )~   Version 2.9.7.0 GRE (Build 149) 
    ''''    By Martin Roesch & The Snort Team: http://www.snort.org/contact#team
            Copyright (C) 2014 Cisco and/or its affiliates. All rights reserved.
            Copyright (C) 1998-2013 Sourcefire, Inc., et al.
            Using libpcap version 1.9.1 (with TPACKET_V3)
            Using PCRE version: 8.39 2016-06-14
            Using ZLIB version: 1.2.11
    ```
* test config
    ```
    snort -c /etc/snort/snort.conf -T
    Running in Test mode

            --== Initializing Snort ==--
    Initializing Output Plugins!
    Initializing Preprocessors!
    Initializing Plug-ins!
    Parsing Rules file "/etc/snort/snort.conf"
    ```

# task 5 - practical - sniffer mode
* sniffer mode is similar to tcpdump
* option examples
    * snort -v
    * snort -vd
    * snort -de
    * snort -v -d -e
    * snort -X

# task 6 - practical - packet logger mode
* you can sniff and log the packets at the same time
* logs are saved by default in /var/log/snort
* ownership
    * sniffing traffic requires sudo, so the file is owned by that user
* option examples
    * sudo snort -r logname.log -X
    * sudo snort -r logname.log icmp
    * sudo snort -r logname.log tcp
    * sudo snort -r logname.log 'udp and port 53'
    * snort -dvr logname.log -n 10
* filtering resources
    * https://en.wikipedia.org/wiki/Berkeley_Packet_Filter
    * https://biot.com/capstats/bpf.html
    * https://www.tcpdump.org/manpages/tcpdump.1.html
* useful practical example commands
    * sudo snort -r snort.log.1640048004 -n 10
    * sudo snort -r snort.log.1640048004 -n 4 -X
    * sudo snort -r snort.log.1640048004 -n 8 -X
    * sudo snort -r snort.log.1640048004 'tcp and port 80'

# task 7 - practical - ids/ips mode
* ids/ips mode helps you manage the traffic according to user-defined rules
* ids/ips mode depends on rules and configuration
    * example rule
    ```
    alert icmp any any <> any any  (msg: "ICMP Packet Found"; sid: 100001; rev:1;)
    ```
    * default rule location
        * /etc/snort/rules/local.rules
* option examples
    * sudo snort -c /etc/snort/snort.conf -T
    * sudo snort -c /etc/snort/snort.conf -N
    * sudo snort -c /etc/snort/snort.conf -D
    * sudo snort -c /etc/snort/snort.conf -A console
    * sudo snort -c /etc/snort/snort.conf -A cmg
    * sudo snort -c /etc/snort/snort.conf -A fast
    * sudo snort -c /etc/snort/snort.conf -A full
    * sudo snort -c /etc/snort/snort.conf -A none
    * sudo snort -c /etc/snort/rules/local.rules -A console
    * sudo snort -c /etc/snort/snort.conf -q -Q --daq afpacket -i eth0:eth1 -A console

# task 8 - practical - pcap investigation
* pcap investigation mode helps you work with pcap files
* option examples
    * snort -r icmp-test.pcap
    * sudo snort -c /etc/snort/snort.conf -q -r icmp-test.pcap -A console -n 10
    * sudo snort -c /etc/snort/snort.conf -q --pcap-list="icmp-test.pcap http2.pcap" -A console -n 10
    * sudo snort -c /etc/snort/snort.conf -q --pcap-list="icmp-test.pcap http2.pcap" -A console --pcap-show
    * sudo snort -c /etc/snort/snort.conf -A full -l . -r mx-1.pcap
    * sudo snort -c /etc/snort/snortv2.conf -A full -l . -r mx-1.pcap
    * sudo snort -c /etc/snort/snort.conf -A full -l . -r mx-2.pcap
    * sudo snort -c /etc/snort/snort.conf -A full -l . --pcap-list="mx-2.pcap mx-3.pcap"

# task 9 - snort rule structure
* snort rule structure
    * action
        * alert
        * log
        * drop
        * reject
    * protocol
        * tcp
        * udp
        * icmp
    * source ip
        * any
    * source port
        * any
    * direciton
        * <>
        * ->
        * <-
    * destination ip
        * any
    * destination port
        * any
    * options
        * msg - basic prompt when rule is triggered
        * reference - external reference with more info about this rule
        * sid - snort rule id
        * rev - revision number of the current rule
* snort is in passive mode by default
* every rule should have a type of action, protocol, source and destination IP, source and destination port, and option
* practical notes
    * sudo snort -c local.rules -A full -l . -r task9.pcap
    * alert icmp any any <> any any (msg: "id test"; id:35369; sid:1000001; rev:1;)
    * alert tcp any any <> any any (msg: "syn"; flags:S; sid:1000001; rev:1;)
    * alert tcp any any <> any any (msg: "syn"; flags:AP; sid:1000001; rev:1;)
    * alert ip any any <> any any (msg: "same ip"; sameip; sid:1000001; rev:1;)
    * cat alert | grep "TCP\|UDP" | wc

# task 10 - points to remeber
* main components
    * packet decoder
    * pre-processor
    * detection engine
    * logging and alerting
    * outputs and plugins
* types of rules
    * community rules
    * registered rules
    * subscriber rules
* configs  
    * /etc/snort/snort.conf

# task 11 - conclusion
* conclusion