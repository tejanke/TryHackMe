# Room
https://tryhackme.com/room/btwindowsinternals

# Task 1 - Intro
Intro

# Task 2 - Task Manager
Task Manager allows you to see and manage processes running in Windows.  It allows you to view statistics such as memory and CPU utilized by each process

Process Types
* Apps
* Background process
* Windows process

Process Tab
* Type
* Publisher
* PID
* Process Name
* Command line
* CPU
* Memory

Details
* Image path name
* Command line
* Parent process

Tools similar to Task Manager
* Process Hacker
* Process Explorer
* tasklist
* get-process

# Task 3 - System
The first Windows process is System.  The PID for system is always 4

Research
* https://docs.microsoft.com/en-us/windows-hardware/drivers/gettingstarted/user-mode-and-kernel-mode

# Task 4 - System : smss.exe
The Session Manager Subsystem is also known as the Windows Session Manager, it is responsible for creating new sessions.  It is also the first user-mode process started by the kernel

Research
* https://en.wikipedia.org/wiki/Architecture_of_Windows_NT

Windows subsystem
* win32k.sys - kernel mode
* winsrv.dll - user mode
* csrss - user mode

Smss.exe starts csrss.exe and wininit.exe in session 0, and csrss.exe and winlogon.exe for session 1.  SMSS is also responsible for creating environment variables, virtual memory paging files, and starts winlogon.exe

# Task 5 - csrss.exe
The Client Server Runtime Process is the user mode side of the Windows subsystem.  It is always running and is critical to system operation.  If the process is killed, it will result in system failure.  It is responsible for the Win32 console window and process thread creation and deletion.

Research
* https://en.wikipedia.org/wiki/Client/Server_Runtime_Subsystem

# Task 6 - wininit.exe
The Windows Initialization Process is responsible for launching services.exe (Service Control Manager), lsass.exe (Local Security Authority), and lsaiso.exe in Session 0.  lsaiso.exe is a process associated with Credential Guard and Key Guard

# Task 7 - wininit.exe > services.exe
The Service Control Manager (SCM) uses the process services.exe.  The primary responsibility it has is to handle system services by loading them, starting and stopping them, etc.

Information regarding services is stored in the registery at HKLM\System\CurrentControlSet\Services

# Task 8 - wininit.exe > services.exe > svchost.exe
The Service Host process - svchost.exe - is in charge of hosting and managing Windows services.  svchost.exe will always have multiple running processes.  The -k parameter is important when launching a service with svchost.exe

# Task 9 - lsass.exe
The Local Security Authority Subsystem Service (LSASS) is responsble for enforcing security policy.  It verifies users logging in, handles password changes, and creates access tokens.  It writes to the Windows Security Log.  It creates security tokens for SAM (Security Account Manager), AD (Active Directory), and NETLOGON.  wininit.exe is the parent process for lsass.exe

# Task 10 - winlogon.exe
Windows Logon, winlogon.exe, handles the Secure Attention Sequence (SAS), this is the CTRL+ALT+DEL key combination.  It also loads a user's profile.  A user's profile is loaded by loading the user's NTUSER.DAT into HKCU and via userinit.exe which loads the user shell.  It also controls locking the screen and running the user's screensaver.  Winlogon.exe is called by smss.exe, after winlogon loads, smss terminates

# Task 11 - explorer.exe
Windows Explorer, explorer.exe, gives the user access to files and folders.  It also provides the start menu and taskbar.  explorer.exe's spawning process is userinit.exe.  Explorer.exe will have many child processes

# Task 12 - Conclusion
Resources
* https://www.threathunting.se/tag/windows-process/
* https://www.sans.org/security-resources/posters/hunt-evil/165/download
* https://docs.microsoft.com/en-us/sysinternals/resources/windows-internals