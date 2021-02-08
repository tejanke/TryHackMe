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
