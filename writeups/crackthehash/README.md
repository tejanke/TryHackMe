# Room
https://tryhackme.com/room/crackthehash

# Task 1 - Level 1
* 48bb6e862e54f2a795ffc4e541caed4d
```
hash-identifier 48bb6e862e54f2a795ffc4e541caed4d              

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

echo "48bb6e862e54f2a795ffc4e541caed4d" > h1.txt

john --format=raw-md5 --wordlist=/usr/share/wordlists/rockyou.txt h1.txt

Using default input encoding: UTF-8
Loaded 1 password hash (Raw-MD5 [MD5 128/128 SSE2 4x3])
Warning: no OpenMP support for this hash type, consider --fork=2
Press 'q' or Ctrl-C to abort, almost any other key for status
[removed]
1g 0:00:00:00 DONE (2021-01-17 19:26) 20.00g/s 3448Kp/s 3448Kc/s 3448KC/s erinbear..eagames
Use the "--show --format=Raw-MD5" options to display all of the cracked passwords reliably
Session completed
```
* CBFDAC6008F9CAB4083784CBD1874F76618D2A97 
```
hash-identifier CBFDAC6008F9CAB4083784CBD1874F76618D2A97

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

hashcat --help | grep SHA1 

    100 | SHA1                                             | Raw Hash
    150 | HMAC-SHA1 (key = $pass)                          | Raw Hash, Authenticated
    160 | HMAC-SHA1 (key = $salt)                          | Raw Hash, Authenticated
  12000 | PBKDF2-HMAC-SHA1                                 | Generic KDF
  12001 | Atlassian (PBKDF2-HMAC-SHA1)                     | Generic KDF
   5400 | IKE-PSK SHA1                                     | Network Protocols
  23200 | XMPP SCRAM PBKDF2-SHA1                           | Network Protocols
   7300 | IPMI2 RAKP HMAC-SHA1                             | Network Protocols
  22600 | Telegram Desktop App Passcode (PBKDF2-HMAC-SHA1) | Network Protocols
  11200 | MySQL CRAM (SHA1)                                | Network Protocols
   8100 | Citrix NetScaler (SHA1)                          | Operating System
   9800 | MS Office <= 2003 $3/$4, SHA1 + RC4              | Documents
   9810 | MS Office <= 2003 $3, SHA1 + RC4, collider #1    | Documents
   9820 | MS Office <= 2003 $3, SHA1 + RC4, collider #2    | Documents
  15500 | JKS Java Key Store Private Keys (SHA1)           | Password Managers
  13300 | AxCrypt in-memory SHA1                           | Archives
  18100 | TOTP (HMAC-SHA1)                                 | One-Time Passwords

.\hashcat.exe -m 100 -a 0 CBFDAC6008F9CAB4083784CBD1874F76618D2A97 .\rockyou.txt

hashcat (v6.1.1) starting...

Host memory required for this attack: 222 MB

Dictionary cache hit:
* Filename..: .\rockyou.txt
* Passwords.: 14349525
* Bytes.....: 139965214
* Keyspace..: 14349525

cbfdac6008f9cab4083784cbd1874f76618d2a97:[removed]

Session..........: hashcat
Status...........: Cracked
Hash.Name........: SHA1
Hash.Target......: cbfdac6008f9cab4083784cbd1874f76618d2a97
Time.Started.....: Sun Jan 17 19:40:04 2021 (0 secs)
Time.Estimated...: Sun Jan 17 19:40:04 2021 (0 secs)
Guess.Base.......: File (.\rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........: 30528.7 kH/s (8.16ms) @ Accel:1024 Loops:1 Thr:64 Vec:1
Recovered........: 1/1 (100.00%) Digests
Progress.........: 589824/14349525 (4.11%)
Rejected.........: 0/589824 (0.00%)
Restore.Point....: 0/14349525 (0.00%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidates.#1....: 123456 -> sideways2
Hardware.Mon.#1..: Temp: 30c Fan: 51% Util: 13% Core:1506MHz Mem:3802MHz Bus:8
```

* 1C8BFE8F801D79745C4631D09FFF36C82AA37FC4CCE4FC946683D7B336B63032

```
hash-identifier 1C8BFE8F801D79745C4631D09FFF36C82AA37FC4CCE4FC946683D7B336B63032

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

Used https://crackstation.net/
```

* $2y$12$Dwt1BZj6pcyc3Dy1FWZ5ieeUznr71EeNkJkUlypTsgbX1H68wsRom

```
hash-identifier $2y$12$Dwt1BZj6pcyc3Dy1FWZ5ieeUznr71EeNkJkUlypTsgbX1H68wsRom
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

 Not Found.

Used https://hashcat.net/wiki/doku.php?id=example_hashes

Looks like bcrypt
3200 	bcrypt $2*$, Blowfish (Unix) 	$2a$05$LhayLxezLhK1LhWvKxCyLOj0j1u.Kj0jZ0pEmm134uzrQlFvQJLF6 

.\hashcat.exe -m 3200 -a 0 -w 3 .\4.hash .\rockyou.txt

hashcat (v6.1.1) starting...

Host memory required for this attack: 91 MB

Dictionary cache hit:
* Filename..: .\rockyou.txt
* Passwords.: 14349525
* Bytes.....: 139965214
* Keyspace..: 14349525

Session..........: hashcat
Status...........: Running
Hash.Name........: bcrypt $2*$, Blowfish (Unix)
Hash.Target......: $2y$12$Dwt1BZj6pcyc3Dy1FWZ5ieeUznr71EeNkJkUlypTsgbX...8wsRom
Time.Started.....: Sun Jan 17 20:54:52 2021 (45 secs)
Time.Estimated...: Wed Jan 20 03:05:52 2021 (2 days, 6 hours)
Guess.Base.......: File (.\rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:       74 H/s (21.04ms) @ Accel:2 Loops:32 Thr:11 Vec:1
Recovered........: 0/1 (0.00%) Digests
Progress.........: 3168/14349525 (0.02%)
Rejected.........: 0/3168 (0.00%)
Restore.Point....: 3168/14349525 (0.02%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:2944-2976
Candidates.#1....: verny -> vegaslas
Hardware.Mon.#1..: Temp: 40c Fan: 56% Util: 99% Core:1911MHz Mem:3802MHz Bus:8

Looking at 2 days of cracking, didn't want to wait that long.  Checked the answer length we are looking for, 4 chars.

Created new 4 char rockyou.txt and cracked with that:

awk 'length($1) == 4 { print $1 }' rockyou.txt > 4rockyou.txt

hashcat took 45 seconds this time around.

$2y$12$Dwt1BZj6pcyc3Dy1FWZ5ieeUznr71EeNkJkUlypTsgbX1H68wsRom:[removed]

Session..........: hashcat
Status...........: Cracked
Hash.Name........: bcrypt $2*$, Blowfish (Unix)
Hash.Target......: $2y$12$Dwt1BZj6pcyc3Dy1FWZ5ieeUznr71EeNkJkUlypTsgbX...8wsRom
Time.Started.....: Sun Jan 17 21:02:17 2021 (45 secs)
Time.Estimated...: Sun Jan 17 21:03:02 2021 (0 secs)
Guess.Base.......: File (.\4rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:       71 H/s (43.53ms) @ Accel:32 Loops:4 Thr:11 Vec:1
Recovered........: 1/1 (100.00%) Digests
Progress.........: 3168/34453 (9.20%)
Rejected.........: 0/3168 (0.00%)
Restore.Point....: 0/34453 (0.00%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:4092-4096
Candidates.#1....: rock -> 2283
Hardware.Mon.#1..: Temp: 48c Fan: 59% Util: 94% Core:1898MHz Mem:3802MHz Bus:8
```

* 279412f945939ba78ce0758d3fd83daa

```
hash-identifier 279412f945939ba78ce0758d3fd83daa

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

Used https://hashes.com/en/decrypt/hash
```

# Task 2 - Level 2