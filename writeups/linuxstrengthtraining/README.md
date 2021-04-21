# Room
https://tryhackme.com/room/linuxstrengthtraining

# Task 1 - Intro
Intro

# Task 2 - Find
Find command examples
* find /home/user -type f -name sales.txt
* find /home/user -type d -name pictures
* find /home/user -type f -size 10c
* find /etc/server -type f -user john
* find /etc/server -type f -group admins
* find /etc/server -type f -newermt '6/3/2019 0:10:00'
* find /etc/server -type f -newermt 2019-06-03 ! -newermt 2020-06-03

Command explanations
* https://explainshell.com/

# Task 3 - Working with files
File commands
* cp
* mv
* touch
* cat

# Task 4 - Hashing
Hashing is a one way function that turns something into a specific fixed length output.  John the Ripper is used to crack hashes

# Task 5 - Encoding
Base64 is a popular encoding scheme.  You can use the base64 command to encode (-e) and decode (-d)

# Task 6 - gpg
Encryption transforms sensitive information into something obscure.  Two main types include symmetric which uses one key to encrypt and decrypt, and asymmetric which uses one key to encrypt and one key to decrypt

gpg encrypt
* gpg --cipher-algo AES-256 --symmetric secret.txt

gpg decrypt
* gpg --pinentry-mode=loopback file.txt

# Task 7 - Cracking gpg files
To crack a gpg file with john, first hash it with gpg2john and then use john to crack that hash

hash
* gpg2john [file].gpg > hash

crack
* john --wordlist=rockyou.txt --format=gpg hash

# Task 8 - Reading SQL databases
SQL is a language for storing, manipulating, and retrieving data from databases

Review
* https://www.elated.com/mysql-for-absolute-beginners/

# Task 9 - Challenge
Read a chat log to get a clue on what to do next.  Search for more chat logs using find and the -size option to narrow down clutter.  Other clues give you creds to login as another user.  With that you user you are able to cat out a database backup config file and grab the password to the database.  Decrypt the gpg encrypted database and unzip it.  Login to SQL with mysql -u root -p, no password, and source the load database to import.  Read through the database searching for the user in question given in the challenge to find his password.  su to that user and then elevate to root (sudoer with all privs)