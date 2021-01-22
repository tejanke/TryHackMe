# Room
https://tryhackme.com/room/johntheripper0

# Task 1 - John who?
John the Ripper is a hash cracking tool that uses brute forcing with a dictionary.

A hash is a one way function that takes a piece of input of any length and coverts it to a fixed length output.  The algorithm that performs this operation can be MD5 or SHA1, among others.  Changing one character in the input results in a completely different hash output.

* MD5 hash examples
    ```
    echo test123 | md5sum
    4a251a2ef9bbf4ccc35f97aba2c9cbda  -

    echo test124 | md5sum
    0af9cdec30bc6e4e42178a3918b0fbe9  -

    echo test124asdofiuwer982374raspdfoisdfkjwerjh23498asdpofiuasdfkl | md5sum
    ca158883c73432f3ea520ce7e1920eaa  -
    ```

# Task 2 - Setup
There is a standard core distribution of John.  A popular community edition is called Jumbo John.

* Ubuntu
    * sudo apt install john
* Windows
    * 64 : https://www.openwall.com/john/k/john-1.9.0-jumbo-1-win64.zip
    * 32 : https://www.openwall.com/john/k/john-1.9.0-jumbo-1-win32.zip

# Task 3 - Wordlists
Dictionary attacks require wordlists.  There are many available, you can also create your own.

* Parrot, Kali, AttackBox
    * /usr/share/wordlists
* SecLists
    * https://github.com/danielmiessler/SecLists

# Task 4 - Cracking Basic Hashes
* Basic syntax: 
    ```
    john [options] [path to file]
    ```
* Automatic cracking with a wordlist: 
    ```
    john --wordlist=[path to wordlist] [path to file]
    ```
* Specifying a hash when cracking:
    ```
    john --format=[format] --wordlist=[path to wordlist] [path to file]

    * note - standard hash types require a raw- prefix
    ```
* Practical
    * 2e728dd31fb5949bc39cac5a9f066498
    ```
    hash-identifier 2e728dd31fb5949bc39cac5a9f066498

    #########################################################################
    #     __  __                     __           ______    _____           #
    #    /\ \/\ \                   /\ \         /\__  _\  /\  _ `\         #
    #    \ \ \_\ \     __      ____ \ \ \___     \/_/\ \/  \ \ \/\ \        #
    #     \ \  _  \  /'__`\   / ,__\ \ \  _ `\      \ \ \   \ \ \ \ \       #
    #      \ \ \ \ \/\ \_\ \_/\__, `\ \ \ \ \ \      \_\ \__ \ \ \_\ \      #
    #       \ \_\ \_\ \___ \_\/\____/  \ \_\ \_\     /\_____\ \ \____/      #
    #        \/_/\/_/\/__/\/_/\/___/    \/_/\/_/     \/_____/  \/___/  v1.2 #
    #                                                             By Zion3R #
    #                                                    www.Blackploit.com #
    #                                                   Root@Blackploit.com #
    #########################################################################
    --------------------------------------------------

    Possible Hashs:
    [+] MD5
    [+] Domain Cached Credentials - MD4(MD4(($pass)).(strtolower($username)))

    john --format=raw-md5 --wordlist=/usr/share/wordlists/rockyou.txt hash1.txt

    Using default input encoding: UTF-8
    Loaded 1 password hash (Raw-MD5 [MD5 128/128 SSE2 4x3])
    Warning: no OpenMP support for this hash type, consider --fork=2
    Press 'q' or Ctrl-C to abort, almost any other key for status
    [removed]          (?)
    1g 0:00:00:00 DONE (2021-01-21 18:54) 20.00g/s 53760p/s 53760c/s 53760C/s shamrock..nugget
    Use the "--show --format=Raw-MD5" options to display all of the cracked passwords reliably
    Session completed
    ```

    * 1A732667F3917C0F4AA98BB13011B9090C6F8065
    ```
    hash-identifier 1A732667F3917C0F4AA98BB13011B9090C6F8065

   #########################################################################
   #     __  __                     __           ______    _____           #
   #    /\ \/\ \                   /\ \         /\__  _\  /\  _ `\         #
   #    \ \ \_\ \     __      ____ \ \ \___     \/_/\ \/  \ \ \/\ \        #
   #     \ \  _  \  /'__`\   / ,__\ \ \  _ `\      \ \ \   \ \ \ \ \       #
   #      \ \ \ \ \/\ \_\ \_/\__, `\ \ \ \ \ \      \_\ \__ \ \ \_\ \      #
   #       \ \_\ \_\ \___ \_\/\____/  \ \_\ \_\     /\_____\ \ \____/      #
   #        \/_/\/_/\/__/\/_/\/___/    \/_/\/_/     \/_____/  \/___/  v1.2 #
   #                                                             By Zion3R #
   #                                                    www.Blackploit.com #
   #                                                   Root@Blackploit.com #
   #########################################################################
    --------------------------------------------------

    Possible Hashs:
    [+] SHA-1
    [+] MySQL5 - SHA-1(SHA-1($pass))

    john --format=raw-sha1 --wordlist=/usr/share/wordlists/rockyou.txt hash2.txt

    Using default input encoding: UTF-8
    Loaded 1 password hash (Raw-SHA1 [SHA1 128/128 SSE2 4x])
    Warning: no OpenMP support for this hash type, consider --fork=2
    Press 'q' or Ctrl-C to abort, almost any other key for status
    [removed]         (?)
    1g 0:00:00:00 DONE (2021-01-21 18:56) 12.50g/s 1464Kp/s 1464Kc/s 1464KC/s kanon..kalvin1
    Use the "--show --format=Raw-SHA1" options to display all of the cracked passwords reliably
    Session completed
    ```

    * D7F4D3CCEE7ACD3DD7FAD3AC2BE2AAE9C44F4E9B7FB802D73136D4C53920140A
    ```
    hash-identifier D7F4D3CCEE7ACD3DD7FAD3AC2BE2AAE9C44F4E9B7FB802D73136D4C53920140A

    #########################################################################
    #     __  __                     __           ______    _____           #
    #    /\ \/\ \                   /\ \         /\__  _\  /\  _ `\         #
    #    \ \ \_\ \     __      ____ \ \ \___     \/_/\ \/  \ \ \/\ \        #
    #     \ \  _  \  /'__`\   / ,__\ \ \  _ `\      \ \ \   \ \ \ \ \       #
    #      \ \ \ \ \/\ \_\ \_/\__, `\ \ \ \ \ \      \_\ \__ \ \ \_\ \      #
    #       \ \_\ \_\ \___ \_\/\____/  \ \_\ \_\     /\_____\ \ \____/      #
    #        \/_/\/_/\/__/\/_/\/___/    \/_/\/_/     \/_____/  \/___/  v1.2 #
    #                                                             By Zion3R #
    #                                                    www.Blackploit.com #
    #                                                   Root@Blackploit.com #
    #########################################################################
    --------------------------------------------------

    Possible Hashs:
    [+] SHA-256
    [+] Haval-256

    john --format=raw-sha256 --wordlist=/usr/share/wordlists/rockyou.txt hash3.txt

    Using default input encoding: UTF-8
    Loaded 1 password hash (Raw-SHA256 [SHA256 128/128 SSE2 4x])
    Warning: poor OpenMP scalability for this hash type, consider --fork=2
    Will run 2 OpenMP threads
    Press 'q' or Ctrl-C to abort, almost any other key for status
    [removed]       (?)
    1g 0:00:00:00 DONE (2021-01-21 18:58) 12.50g/s 1024Kp/s 1024Kc/s 1024KC/s ryanscott..janson
    Use the "--show --format=Raw-SHA256" options to display all of the cracked passwords reliably
    Session completed
    ```

    * c5a60cc6bbba781c601c5402755ae1044bbf45b78d1183cbf2ca1c865b6c792cf3c6b87791344986c8a832a0f9ca8d0b4afd3d9421a149d57075e1b4e93f90bf

    ```
    hash-identifier c5a60cc6bbba781c601c5402755ae1044bbf45b78d1183cbf2ca1c865b6c792cf3c6b87791344986c8a832a0f9ca8d0b4afd3d9421a149d57075e1b4e93f90bf

    #########################################################################
    #     __  __                     __           ______    _____           #
    #    /\ \/\ \                   /\ \         /\__  _\  /\  _ `\         #
    #    \ \ \_\ \     __      ____ \ \ \___     \/_/\ \/  \ \ \/\ \        #
    #     \ \  _  \  /'__`\   / ,__\ \ \  _ `\      \ \ \   \ \ \ \ \       #
    #      \ \ \ \ \/\ \_\ \_/\__, `\ \ \ \ \ \      \_\ \__ \ \ \_\ \      #
    #       \ \_\ \_\ \___ \_\/\____/  \ \_\ \_\     /\_____\ \ \____/      #
    #        \/_/\/_/\/__/\/_/\/___/    \/_/\/_/     \/_____/  \/___/  v1.2 #
    #                                                             By Zion3R #
    #                                                    www.Blackploit.com #
    #                                                   Root@Blackploit.com #
    #########################################################################
    --------------------------------------------------

    Possible Hashs:
    [+] SHA-512
    [+] Whirlpool

    john --format=whirlpool --wordlist=/usr/share/wordlists/rockyou.txt hash4.txt

    Using default input encoding: UTF-8
    Loaded 1 password hash (whirlpool [WHIRLPOOL 32/64])
    Warning: poor OpenMP scalability for this hash type, consider --fork=2
    Will run 2 OpenMP threads
    Press 'q' or Ctrl-C to abort, almost any other key for status
    [removed]         (?)
    1g 0:00:00:00 DONE (2021-01-21 19:00) 3.225g/s 2193Kp/s 2193Kc/s 2193KC/s cooldragon..chata74
    Use the "--show" option to display all of the cracked passwords reliably
    Session completed
    ```

# Task 5 - Cracking Windows Authentication Hashes
NTHash/NTLM hashes can be acquired by dumping the SAM database on a Windows machine by using mimikatz or the AD database file ntds.dit.

* Practical

    * 5460C85BD858A11475115D2DD3A82333
    ```
    john --format=nt --wordlist=/usr/share/wordlists/rockyou.txt ntlm.txt

    Using default input encoding: UTF-8
    Loaded 1 password hash (NT [MD4 128/128 SSE2 4x3])
    Warning: no OpenMP support for this hash type, consider --fork=2
    Press 'q' or Ctrl-C to abort, almost any other key for status
    [removed]         (?)
    1g 0:00:00:00 DONE (2021-01-21 19:49) 25.00g/s 76800p/s 76800c/s 76800C/s lance..dangerous
    Use the "--show --format=NT" options to display all of the cracked passwords reliably
    Session completed
    ```

# Task 6 - Cracking /etc/shadow Hashes
The /etc/shadow file stores password hashes, access by privileged users only.

John is very particular about the format when reading a file.  You need to use unshadow to combine /etc/shadow and /etc/passwd.

```
unshadow [path to passwd] [path to shadow] > unshadow.txt
```

* Practical
    ```
    cat passwd
    root:x:0:0::/root:/bin/bash

    cat shadow
    root:$6$Ha.d5nGupBm29pYr$yugXSk24ZljLTAZZagtGwpSQhb3F2DOJtnHrvk7HI2ma4GsuioHp8sm3LJiRJpKfIf7lZQ29qgtH17Q/JDpYM/:18576::::::

    unshadow passwd shadow > unshadowed.txt

    cat unshadowed.txt
    root:$6$Ha.d5nGupBm29pYr$yugXSk24ZljLTAZZagtGwpSQhb3F2DOJtnHrvk7HI2ma4GsuioHp8sm3LJiRJpKfIf7lZQ29qgtH17Q/JDpYM/:0:0::/root:/bin/bash    

    john --wordlist=/usr/share/wordlists/rockyou.txt --format=sha512crypt unshadowed.txt 

    Using default input encoding: UTF-8
    Loaded 1 password hash (sha512crypt, crypt(3) $6$ [SHA512 128/128 SSE2 2x])
    Cost 1 (iteration count) is 5000 for all loaded hashes
    Will run 2 OpenMP threads
    Press 'q' or Ctrl-C to abort, almost any other key for status
    [removed]             (root)
    1g 0:00:00:01 DONE (2021-01-21 19:58) 0.5649g/s 650.8p/s 650.8c/s 650.8C/s kucing..summer1
    Use the "--show" option to display all of the cracked passwords reliably
    Session completed
    ```