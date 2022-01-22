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