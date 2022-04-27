# room
https://tryhackme.com/room/snortchallenges1

# task 1 - intro
* intro

# task 2 - writing IDS rules - HTTP
* practical notes
    * with your rule selection, make sure sid is different between all rules, otherwise you won't see everything
    ```
    cat local.rules

    # ----------------
    # LOCAL RULES
    # ----------------
    # This file intentionally does not come with signatures.  Put your local
    # additions here.
    #
    alert tcp any 80 <> any any (msg: "HTTP Packet found"; sid: 100001; rev:1;)
    alert tcp any any <> any 80 (msg: "HTTP Packet found"; sid: 100002; rev:1;)
    ```
    * sudo snort -c local.rules -A full -l . -r mx-3.pcap 
    * sudo snort -r snort.log.1650658626 -n 63 -X -q
    * sudo snort -r snort.log.1650658626 -n 64 -X -q    
    * sudo snort -r snort.log.1650658626 -n 62 -X -q        
    * sudo snort -r snort.log.1650658626 -n 65 -X -q        

# task 3 - writing IDS rules - FTP
* practical notes
    * with your rule selection, make sure sid is different between all rules, otherwise you won't see everything
    ```
    cat local.rules

    # ----------------
    # LOCAL RULES
    # ----------------
    # This file intentionally does not come with signatures.  Put your local
    # additions here.
    alert tcp any 21 <> any any (msg: "FTP Packet found"; sid: 100001; rev:1;)
    alert tcp any any <> any 21 (msg: "FTP Packet found"; sid: 100002; rev:1;)
    ```
    * sudo snort -c local.rules -A full -l . -r ftp-png-gif.pcap 
    * sudo snort -r snort.log.1650659223 -X -q -n 10
    * sudo snort -r snort.log.1650659223 -X -q -n 222
    ```
    cat nologin.rules
    alert tcp any any <> any 21 (msg:"FTP Failed Login"; content:"cannot log in"; sid: 100001; rev:1;)
    ```
    * sudo rm -rf alert snort.log.*
    * sudo snort -c nologin.rules -A full -l . -r ftp-png-gif.pcap 
    * https://en.wikipedia.org/wiki/List_of_FTP_server_return_codes
    ```
    cat loginsuccess.rules 
    alert tcp any any <> any 21 (msg:"FTP Login Success"; content:"230"; sid: 100001; rev:1;)
    ```
    * sudo rm -rf alert snort.log.*
    * sudo snort -c loginsuccess.rules -A full -l . -r ftp-png-gif.pcap     
    ```
    cat badpasswd.rules 
    alert tcp any any <> any 21 (msg:"FTP Bad Password"; content:"331"; sid: 100001; rev:1;)
    ```
    * sudo rm -rf alert snort.log.*
    * sudo snort -c badpasswd.rules -A full -l . -r ftp-png-gif.pcap         
    ```
    cat adminattempt.rules 
    alert tcp any any <> any 21 (msg:"FTP Bad Password"; content:"331"; fast_pattern; content:"Admin"; sid: 100001; rev:1;)
    ```
    * sudo rm -rf alert snort.log.*
    * sudo snort -c adminattempt.rules -A full -l . -r ftp-png-gif.pcap             

# task 4 - writing IDS rules - PNG
* practical notes
    * png rule
    * reference PNG magic bytes : https://en.wikipedia.org/wiki/List_of_file_signatures
    ```
    cat local.rules

    # ----------------
    # LOCAL RULES
    # ----------------
    # This file intentionally does not come with signatures.  Put your local
    # additions here.

    alert ip any any <> any any  (msg: "PNG File Found"; content:"|89 50 4E 47|"; sid: 100001; rev:1;)
    ```
    * sudo snort -c local.rules -A full -l . -r ftp-png-gif.pcap 
    * sudo snort -r snort.log.1650759156 -X

    * gif rule
    ```
    cat local.rules

    # ----------------
    # LOCAL RULES
    # ----------------
    # This file intentionally does not come with signatures.  Put your local
    # additions here.

    alert ip any any <> any any  (msg: "GIF File Found"; content:"|47 49 46 38|"; sid: 100001; rev:1;)
    ```
    * sudo snort -c local.rules -A full -l . -r ftp-png-gif.pcap 
    * sudo snort -r snort.log.1650759955 -X    

# task 5 - writing IDS rules - torrent metafile
* practical notes
    * torrent metafiles
    ```
    cat local.rules

    # ----------------
    # LOCAL RULES
    # ----------------
    # This file intentionally does not come with signatures.  Put your local
    # additions here.

    alert ip any any <> any any (msg: "Torrent File Found"; content:".torrent"; sid: 100001; rev:1;)
    ```
    * sudo snort -c local.rules -A full -l . -r torrent.pcap 
    * sudo snort -r snort.log.1651022165 -X

# task 6 - troubleshooting rule syntax errors
* practical notes
    * go through each local*.rules file and fix the syntax errors
    * everything from spaces to incorrect characters

# task 7 - external rules - investigating ms17-010
* practical notes
    * sudo snort -c local.rules -r ms-17-010.pcap -A full -l .
    ```
    cat local-1.rules 

    # ----------------
    # LOCAL RULES
    # ----------------
    # This file intentionally does not come with signatures.  Put your local
    # additions here.

    alert ip any any <> any any (msg: "IPC Payload"; content: "\\IPC$"; sid: 100001; rev: 1;)
    ```
    * https://nvd.nist.gov/vuln/detail/cve-2017-0144

# task 8 - external rules - investigating log4j
* practical notes
    * sudo snort -c local.rules -r log4j.pcap -A full -l .
    * cat alert | grep "\[1:" | sort | uniq
    ```
    cat local-1.rules 

    # ----------------
    # LOCAL RULES
    # ----------------
    # This file intentionally does not come with signatures.  Put your local
    # additions here.

    alert tcp any any <> any any (msg: "770-855"; dsize:770<>855; sid: 100001; rev:1;)
    ```
    * sudo snort -r snort.log.1651024231 -X
    * use a CLI decoder
    * https://nvd.nist.gov/vuln/detail/CVE-2021-44228

# task 9 - conclusion
* conclusion