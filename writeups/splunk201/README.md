# room
https://tryhackme.com/room/splunk201

# task 1 - intro
* intro

# task 2 - incident handling - life cycle
life cycle
* preparation
* detection and analysis
* containment, eradication, and recovery
* post incident activity / lessons learnt

# task 3 - incident handling - scenario
* cyber kill chain
    * recon
    * weaponization
    * delivery
    * exploitation
    * installation
    * command and control
    * actions on objectives
* splunk
    * interesting log sources
        * wineventlog
        * winregistry
        * xmlwineventlog
        * fortigate_utm
        * iis
        * nessus:scan
        * suricata
        * stream:http
        * stream:dns
        * stream:icmp
* event logs
    * index=botsv1

# task 4 - recon
* recon is an attempt to discover and collection info about a target and can contain knowledge about the system in use, the web app, employees, or location
* task info
    * imreallynotbatman.com
    * index=botsv1 imreallynotbatman.com - look for event logs in the botsv1 index that contain the term imreallynotbatman.com
        * in the new search screen select all time via the time selection drop down and select verbose in the mode drop down
        * use index=botsv1 imreallynotbatman.com for the search query

# task 5 - exploitation
* attackers exploit vulnerabilities to gain access to the system
* task info
    * index=botsv1 imreallynotbatman.com sourcetype=stream* | stats count(src_ip) as Requests by src_ip | sort - Requests
        * uses the stats function to count and display the source IP addresses
    * index=botsv1 sourcetype=stream:http dest_ip="192.168.250.70"
        * looks for inbound traffic to 192.168.250.70 using the HTTP source
    * index=botsv1 sourcetype=stream:http dest_ip="192.168.250.70" http_method=POST
        * further reduce traffic match to those using the HTTP POST method
    * index=botsv1 imreallynotbatman.com sourcetype=stream:http dest_ip="192.168.250.70"  uri="/joomla/administrator/index.php"
        * narrow search results to admin page connections
    * index=botsv1 sourcetype=stream:http dest_ip="192.168.250.70" http_method=POST uri="/joomla/administrator/index.php" | table _time uri src_ip dest_ip form_data
        * creates a table that outputs the time, uri, source ip, dest ip, and form data in the request
    * index=botsv1 sourcetype=stream:http dest_ip="192.168.250.70" http_method=POST uri="/joomla/administrator/index.php" form_data=*username*passwd* | table _time uri src_ip dest_ip form_data
        * create table to reduce the last data set to contain requests with a username and password parameter
    * index=botsv1 sourcetype=stream:http dest_ip="192.168.250.70" http_method=POST form_data=*username*passwd* | rex field=form_data "passwd=(?<creds>\w+)"  | table src_ip creds
        * uses regex on the form_data field to extract the password used and create a list of them in a table along with the source IP
    * index=botsv1 sourcetype=stream:http dest_ip="192.168.250.70" http_method=POST form_data=*username*passwd* | rex field=form_data "passwd=(?<creds>\w+)" |table _time src_ip uri http_user_agent creds
        * add uri and user agent data

# task 6 - installation
* after gaining access an attacker will try to install a backdoor that is used for persistence
* task info
    * index=botsv1 sourcetype=stream:http dest_ip="192.168.250.70" *.exe
        * searching for results with an exe file
    * index=botsv1 sourcetype=stream:http dest_ip="192.168.250.70" "part_filename{}"="3791.exe"
        * searching for results with an exe file
    * index=botsv1 "3791.exe"
        * look at what is executed
    * index=botsv1 "3791.exe" sourcetype="XmlWinEventLog" EventCode=1
        * event code 1 tells us the program executed
        * https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon

# task 7 - action on objectives
* task info
    * index=botsv1 dest=192.168.250.70 sourcetype=suricata
    * index=botsv1 src=192.168.250.70 sourcetype=suricata
    * index=botsv1 src=192.168.250.70 sourcetype=suricata dest_ip=23.22.63.114
    * index=botsv1 url="/poisonivy-is-coming-for-you-batman.jpeg" dest_ip="192.168.250.70" | table _time src dest_ip http.hostname url

# task 8 - command and control
* task info
    * index=botsv1 sourcetype=fortigate_utm"poisonivy-is-coming-for-you-batman.jpeg"
    * index=botsv1 sourcetype=stream:http dest_ip=23.22.63.114 "poisonivy-is-coming-for-you-batman.jpeg" src_ip=192.168.250.70

# task 9 - weaponization
* weaponization
    * create malware / malicious document to gain initial access
    * establish domains similar to target domain
    * create a command and control server
* resources
    * https://www.robtex.com/
    * https://www.threatcrowd.org/
    * https://whois.domaintools.com/
* example
    * https://www.robtex.com/dns-lookup/prankglassinebracket.jumpingcrab.com

# task 10 - delivery phase
* resources
    * https://www.threatminer.org/index.php
    * https://www.hybrid-analysis.com/

# task 10 - conclusion
* conclusion