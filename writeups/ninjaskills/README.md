# Room
https://tryhackme.com/room/ninjaskills

# Task 1 - Ninja Skills
Challenge
* Create file with list of files
    ```
    cat files.txt

    8V2L
    bny0
    c4ZX
    D8B3
    FHl1
    oiMO
    PFbD
    rmfX
    SRSq
    uqyw
    v2Vb
    X1Uy
    ```
* Find files in files.txt and print the group to which they belong
    ```
    cat files.txt | xargs -I file sh -c '{ echo "Searching for file"; find / -name file -type f -exec ls -l {} \; 2>/dev/null | cut -d" " -f 4; }'
    ```
* Find files with an IP address inside
    ```
    cat files.txt | xargs -I file sh -c '{ echo "Searching file"; find / -name file -type f -exec egrep "([0-9]{1,3}\.){3}" {} \; 2>/dev/null; }'
    ```
* Find SHA1 hash of files
    ```
    cat files.txt | xargs -I file sh -c '{ echo "Searching file"; find / -name file -type f -exec sha1sum {} \; 2>/dev/null; }'
    ```
* Find word count of files
    ```
    cat files.txt | xargs -I file sh -c '{ echo "Searching file"; find / -name file -type f -exec wc -l {} \; 2>/dev/null; }'
    ```
