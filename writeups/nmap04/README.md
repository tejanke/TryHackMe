# Room
https://tryhackme.com/room/nmap04

# Task 1 - Intro
* Use nmap to
    * detect service versions
    * detect OS versions
    * use traceroute
    * use nmap scripts
    * save scan results

# Task 2 - Service Detection
* nmap can discover service versions
* service versions can only be discovered when using a TCP connect scan
* nmap -sV [target_ip]

# Task 3 - OS Detection and traceroute
* nmap can discover the OS for a target
    * nmap -O [target_ip]
* nmap can also run a traceroute to your target and list out the hops between you and it
    * nmap --traceroute [target_ip]

# Task 4 - nmap scripting engine - NSE
* nmap provides a lua interpreter that allows script extensions to be run to extend the product
* nmap contains about 600 scripts by default
    * located in /usr/share/nmap/scripts
* you may run default scripts by using
    * --script=default
    * or
    * -sC
    * you can also replace the word default with a category as listed below
* nmap -sC [target_ip]
* nmap script categories
    * auth - authentication scripts
    * broadcast - discover hosts by using broadcasts
    * brute - password brute forcing
    * default - the default script runner
    * discovery - database table names, DNS names
    * dos - detect if the target is vulnerable to denial of service
    * exploit - exploit vulnerable services
    * external - check with a 3rd party service like virustotal or geoplugin
    * fuzzer - launch fuzzing attacks against the target
    * intrusive - brute force and exploitation
    * malware - scan for backdoors
    * safe - scripts that won't crash the target
    * version - retrieve service version numbers
    * vuln - check for service vulnerabilities
* you can also specify the script name directly as per the file in /usr/share/nmap/scripts dir
    * --script [script name]
    * the script name can also be a wildcard
        --script [script name*]

# Task 5 - Saving the output
* nmap allows you to save output directly to a file
    * normal
        * -oN [filename]
    * grepable
        * -oG [filename]
    * xml
        * -oX [filename]
    * skidz
        * -oS [filename]

# Task 6 - Summary
Summary