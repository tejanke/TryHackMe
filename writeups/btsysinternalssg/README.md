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

