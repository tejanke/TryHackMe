# Room
https://tryhackme.com/room/btsysinternalssg

# Task 1 - Intro
Sysinternals is a tool collection of 70+ tools for Windows
* File and Disk
* Networking
* Process
* Security
* System Information
* Miscellaneous

https://docs.microsoft.com/en-us/sysinternals/

# Task 2 - Install
Download

https://docs.microsoft.com/en-us/sysinternals/downloads/

Download-SysInternalsTools C:\Tools\Sysint

# Task 3 - Sysinternals Live
Sysinternals Live is a service that enables you to execute Sysinternals tools directly from the Web without hunting for an manually downloading them.

Running from CLI
* Turn on webdav
    * start-service webclient
* Turn on network discovery
    * control.exe /name Microsoft.NetworkandSharingCenter
    * click Change advanced sharing settings
    * turn on network discovery
* Run the tool of your choice with a UNC path
    * \\live.sysinternals.com\tools\procmon.exe

Running from Mapped Drive
* Map a drive
    * net use * \\live.sysinternals.com\tools
    * the * will auto choose a drive letter
* Launch the tool from the mapped drive

# Task 4 - File and Disk
File and Disk Utilities

Sigcheck - command line utility that shows file version number, timestamp information, and digital signature details including certificate chains
* Syntax
    * sigcheck -u -e c:\windows\system32

Streams - Alternate Data Streams is a file attribute specific to NTFS, every file has at least one data stream ($DATA) and ADS allows files to contain more than one stream of data
* Syntax
    * streams c:\file.txt -accepteula

SDelete - Secure Delete - allows you to delete one or more files securely using DoD 5220.22-M Wipe Method

# Task 5 - Networking
Network Utilities

TCPView - shows a detailed listing of all TCP and UDP ports on your system including local and remote addresses and the state of TCP connections

Resource Monitor - a builtin Windows utility that does some of what TCPView does

# Task 6 - Process
Process Utilities

Autoruns - a startup monitor that shows you what programs are configured to run during system boot or login
* Syntax
    * autoruns -accepteula

Procdump - command line utility to monitor an application for CPU spikes and generating crash dumps
* Syntax
    * procdump -accepteula

Process Explorer - displays active processes and their information, allows you to map loaded DLLs for each process
* Syntax
    * procexp -accepteula

Process Monitor - advanced monitoring tool for the file system, registry, and process/thread activity
* Syntax
    * procmon -accepteula

PsExec - lightweight telnet replacement, allows you to launch interactive command prompts
* Syntax
    * psexec -accepteula

# Task 7 - Security
Security Utilities

Sysmon

System Monitor (Sysmon) is a device driver that stays resident across reboots to monitor and log system activity to the Windows event log.  It provides detailed information about process creation, network connections, and changes to file creation time.

# Task 8 - System Information
System Information

WinObj

WinObj displays information on the NT Object Manager's namespace

# Task 9 - Misc
Miscellaneous

BgInfo - automatically displays relevant information about a Windows computer on the desktop's background

RegJump - jumps to a specific path in the registry

Strings - scans a file for ASCII strings

# Task 10 - Conclusion

Resources
* https://docs.microsoft.com/en-us/archive/blogs/markrussinovich/
* https://techcommunity.microsoft.com/t5/windows-blog-archive/bg-p/Windows-Blog-Archive/label-name/Mark%20Russinovich
* https://www.youtube.com/watch?v=A_TPZxuTzBU
* https://www.youtube.com/watch?v=vW8eAqZyWeo