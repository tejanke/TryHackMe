# Room
https://tryhackme.com/room/netsecchallenge

# Task 1 - Intro
Intro

# Task 2 - Challenge
* The first six questions are asking about what and how many ports are open as well as a few header flags.  Scan the target into grepable info to answer the questions.
    ```
    nmap -A -T4 -p- 10.10.143.234 -oG challenge.txt
    ```
* The next to last question can be solved by using hydra to brute force the FTP users you discovered, login, and grab the flag.
    ```
    hydra -l username -P /usr/share/wordlists/rockyou.txt 1.2.3.4 -s 12345 ftp
    ```
* The last question will require you to use one of the scans located in the nmap03 room to evade IDS detection

# Task 3 - Summary
Summary