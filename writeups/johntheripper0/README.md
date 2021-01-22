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

# Task 7 - Single Crack Mode
Doesn't use a wordlist but instead uses the username you supply as a source to carry out the cracking.  The process itself is called word mangling.

```
john --single --format=[format] [path to file]
```

* Joker:7bf6d9bb82bed1302f331fc6b816aada
    ```
    hash-identifier 7bf6d9bb82bed1302f331fc6b816aada

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

    john --single --format=raw-md5 hash7.txt

    Using default input encoding: UTF-8
    Loaded 1 password hash (Raw-MD5 [MD5 128/128 SSE2 4x3])
    Warning: no OpenMP support for this hash type, consider --fork=2
    Press 'q' or Ctrl-C to abort, almost any other key for status
    Warning: Only 2 candidates buffered for the current salt, minimum 12 needed for performance.
    Warning: Only 9 candidates buffered for the current salt, minimum 12 needed for performance.
    Warning: Only 5 candidates buffered for the current salt, minimum 12 needed for performance.
    [removed]            (Joker)
    1g 0:00:00:00 DONE (2021-01-22 17:49) 25.00g/s 4900p/s 4900c/s 4900C/s j0ker..J0k3r
    Use the "--show --format=Raw-MD5" options to display all of the cracked passwords reliably
    Session completed

    ```

# Task 8 - Custom Rules
You can create rules to dynamically create passwords.  This helps if you already have intelligence about the password you are trying to crack, such as systems that tell you there must be a capital letter, a number, and a symbol in the password for it to be accepted for use.

Custom rules are defined in john.conf located in /etc/john or /opt/john.  The custom rules reference is located here: https://www.openwall.com/john/doc/RULES.shtml

```
john --wordlist=[path to wordlist] --rule=[rule_name] [path to file]
```

# Task 9 - Cracking Password Protected Zip Files
John can crack zip file passwords, but first you need to convert the zip file to a hash using zip2john, and then crack it.  Zip2john is like unshadow, it converts a zip file to a hash.

```
zip2john [options] [zip file] > [output file]
```

* secure.zip
    ```
    zip2john secure.zip > zip_hash.txt

    ver 1.0 efh 5455 efh 7875 secure.zip/zippy/flag.txt PKZIP Encr: 2b chk, TS_chk, cmplen=38, decmplen=26, crc=849AB5A6
    
    cat zip_hash.txt

    secure.zip/zippy/flag.txt:$pkzip2$1*2*2*0*26*1a*849ab5a6*0*48*0*26*849a*b689*964fa5a31f8cefe8e6b3456b578d66a08489def78128450ccf07c28dfa6c197fd148f696e3a2*$/pkzip2$:zippy/flag.txt:secure.zip::secure.zip

    john --wordlist=/usr/share/wordlists/rockyou.txt zip_hash.txt 

    Using default input encoding: UTF-8
    Loaded 1 password hash (PKZIP [32/64])
    Will run 2 OpenMP threads
    Press 'q' or Ctrl-C to abort, almost any other key for status
    [removed]          (secure.zip/zippy/flag.txt)
    1g 0:00:00:00 DONE (2021-01-22 18:20) 20.00g/s 163840p/s 163840c/s 163840C/s newzealand..whitetiger
    Use the "--show" option to display all of the cracked passwords reliably
    Session completed

    unzip secure.zip 
    Archive:  secure.zip
    [secure.zip] zippy/flag.txt password: 
    extracting: zippy/flag.txt          

    cat zippy/flag.txt 
    [removed]
    ```

# Task 10 - Cracking Password Protected RAR Archives
John can crack rar file passwords, but first you need to convert the rar file to a hash using rar2john, and then crack it.  Rar2john is like unshadow, it converts a rar file to a hash.

```
rar2john [rar file] > [output file]
```

* secure.rar
    ```
    rar2john secure.rar > rar_hash.txt

    cat rar_hash.txt 

    secure.rar:$rar5$16$b7b0ffc959b2bc55ffb712fc0293159b$15$4f7de6eb8d17078f4b3c0ce650de32ff$8$ebd10bb79dbfb9f8

    john --wordlist=/usr/share/wordlists/rockyou.txt rar_hash.txt 

    Using default input encoding: UTF-8
    Loaded 1 password hash (RAR5 [PBKDF2-SHA256 128/128 SSE2 4x])
    Cost 1 (iteration count) is 32768 for all loaded hashes
    Will run 2 OpenMP threads
    Press 'q' or Ctrl-C to abort, almost any other key for status
    [removed]         (secure.rar)
    1g 0:00:00:00 DONE (2021-01-22 18:25) 4.347g/s 139.1p/s 139.1c/s 139.1C/s 123456..butterfly
    Use the "--show" option to display all of the cracked passwords reliably
    Session completed

    unrar e secure.rar 

    UNRAR 6.00 freeware      Copyright (c) 1993-2020 Alexander Roshal

    Enter password (will not be echoed) for secure.rar: 


    Extracting from secure.rar

    Extracting  flag.txt                                                  OK 
    All OK
    
    cat flag.txt
    [removed]
    ```

# Task 11 - Cracking SSH Keys with John
John can crack SSH keys, but first you need to convert the id_rsa private key file to a hash using ssh2john, and then crack it.  ssh2john is like unshadow, it converts a id_rsa private key file to a hash.

```
ssh2john [id_rsa private key file] > [output file]
```

* id_rsa
    ```
    ssh2john.py id_rsa > id_rsa.hash

    cat id_rsa.hash 

    id_rsa:$sshng$1$16$3A98F468854BB3836BF689310D864CE9$1200$08ca19b68bc606b07875701174131b9220d23ef968befc1230eeff0d7c0f904e6734765fe562e8671972e409091f32c80b754ab248976228a5f2c38e8ac63572d7452e75669aeda932275989ce4c077d43287ed227b8f9053e53f2b1c9bb9dfe876378a32e87e7be4e91a845ae8ee4073bf7ac5aad8414253c97cfb73b083107712907da8c704678f46d0b006f7a77b13a04305a988c8e17d83abd2449ed5c3defc8203d7c5f70cef3470b0bbe3fa5a2e957ac55a57ea08b1de4d3fa5436c6160a14b461ac7bc4a3052ddf858de657ecb210989507beb96f7219ac3c3790e89f3af71f7f61ebe23570284a482b1504b067fb1e03ed62201c6db71dab65e5f1577751ddb006fe14ceed4525965fce19f8141373094d1aedbb58cb903f58f6d80695be0382c31e61baaf366d4f2e722316e91ff4dcb3df15702008b5be3c0b2a81b3f452ef3257c425dd26119324b4de3652e90b91afd87ca2bc41c70abd0d97557d4037952b63c0a0d7c7ab6ed538c3d76bdf488683213e8d8e897ab51c4990b137d04e5044ccbf8cadbdce9eeec5e50f3d487b1f21e86a2b2785caedbf9503d2d8585b2138d82b35e70d1da03c9c574962cdb6e4d2de761a594ab8c082d88b43a027649012feb28b6a022c0ab49cf05e8b91e36bda935f188c1bb05925da2168dd15af917ba20a8532010892853da5cb1a8ff80cc5d3aa1dd3fe66543bf14d9b44d082261fd61976718bb5eea1d911ddb7fb0cc0505b39cec36ef7bd8e8d9d826eda5f7e1a5a51067ead2f78cf69f85de97be5a8f371174356788554b6bf134072b93bf6728ec26fe19c2485be9e7428208a66cc1e79329ac16f3034605c63550a424ed8cac39f965b6ffe83240c6709607eaef99b189100ef33e000b4195e07ec5c67bdaf2ca1acbd08327f0c4dcfae322883f7be964cb22393541e883c8c5b748237a900aab709b6286cea66a214a9fe4e3a1203f999fd995aa049767355e2658828c4a82d58ca15343f0abe6b2779e880ed2682b4730103a84a3410e6c822098d82b04d665b8bf98bc3b69cae0c8d8c9d140dc99056279d5f330bc439bfdceaf38a56fd1362ce78e96deb49a9f6756ec9b64eeba8f4725ec056ab206e37823d052d539d38016abf792858a169cbbe0f6f0d0049c6d49228833aa8ec10ede0c183ac737e54346949485e5ffc1bc3105e5686c8b1f6fb8cdb14949aa97b833757d02b970e96cb1281c472a5cb26cfa7cfda0be5bd45cf14d4bc28ccd2be4dd09c6a2ce0cf668035d2aa39a8345ea154543491436bf8f5e605d86e266d40227f48684e696a225877624ddddf0afe05d0aeec29ad28edb0f8cda0f341ddbbd454bd3c238d1c499effa6bf6f796dae0983182f36fae4781552cb8d9426fc57132c27a735c5365a5d355a4c4f21d5d7ed2ea11bb2ed856156390673545418f47359fd1092767f6dfb3321ee14a0043352fdbaa5cb0e75fde2ec5909c0533251f30bd56ad7e34a8a31b009b53c64e9f2de9fd57a0f561564e6a961158cc0b54fcfc43046d9641788ac5e25b89bdb7890c4e6532d1bfabd4d49ae7d3740506c4ecb6bc5cb6a12bc24ed2e0f913338c7dfa08ada66a6128e7de56794d1d2170d6324af0cd72bc8abcff177f0942d9df5d99d48c8f946fd856d9ccb424966835aa06c94996abcc169aef6f246bbbd7489ec026a

    john --wordlist=/usr/share/wordlists/rockyou.txt id_rsa.hash 

    Using default input encoding: UTF-8
    Loaded 1 password hash (SSH [RSA/DSA/EC/OPENSSH (SSH private keys) 32/64])
    Cost 1 (KDF/cipher [0=MD5/AES 1=MD5/3DES 2=Bcrypt/AES]) is 0 for all loaded hashes
    Cost 2 (iteration count) is 1 for all loaded hashes
    Will run 2 OpenMP threads

    Note: This format may emit false positives, so it will keep trying even after
    finding a possible candidate.
    Press 'q' or Ctrl-C to abort, almost any other key for status
    [removed]            (id_rsa)
    1g 0:00:00:01 11.52% (ETA: 18:32:43) 0.9900g/s 1808Kp/s 1808Kc/s 1808KC/s emilucha..emilly6
    1g 0:00:00:08 DONE (2021-01-22 18:32) 0.1236g/s 1772Kp/s 1772Kc/s 1772KC/sa6_123..*7¡Vamos!
    Session completed
    ```