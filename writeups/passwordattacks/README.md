# room
https://tryhackme.com/room/passwordattacks

# task 1 - intro
* passwords are used as an authentication method

# task 2 - password attacking techniques
* password cracking - discover passwords from encrypted or hash data
* password guessing - guess passwords based on dictionaries

# task 3 - default, weak, leaked, combined, and username wordlists
* default passwords
* weak passwords
* leaked passwords
* wordlists
    * cewl

# task 4 - keyspace, cupp
* keyspace - limit total character space
    * crunch
        * crunch 2 2 01234abcd -o crunch.txt
        * crunch 5 5 -t THM^^ -o tryhackme.txt
* cupp - common user password profiler
    * create custom wordlists based on a user profile

# task 5 - dictionary and brute force
* dictionary attack - use well known words, phrases
* hashes
    * hashcat, hashid
* brute force - guess using a wordlist
    * hashcat, john
* hashid 8d6e34f987851aa599257d3831a1af040886842f
* john -w=/usr/share/wordlists/rockyou.txt h.txt
* hashcat -a 3 -m 0 h2.txt ?d?d?d?d
