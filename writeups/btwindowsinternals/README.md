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

# Task 5