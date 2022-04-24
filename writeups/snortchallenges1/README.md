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