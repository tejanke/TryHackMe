# Room
https://tryhackme.com/room/windowseventlogs

# Task 1 - What are event logs?
Event logs record events taking place in the execution of a system to provide an audit trail that can be used to understand activity of the system and diagnose problems

# Task 2 - Event Viewer
Windows Event Logs are not text files, they are proprietary binary formatted files stored with an .evt or .evtx extension.  These files can be converted to XML using the Windows API.  They are stored in C:\windows\system32\winevt\logs

Windows Event Logs method of access
* Event Viewer - GUI via the MMC or launched directly via eventvwr.msc
* wevtutil.exe - CLI
* Get-WinEvent - PowerShell

Event Types
* Error - a significant problem or loss of data, e.g., a service failure
* Warning - may indicate a possible future problem, e.g., low disk space
* Information - describes a successful operation, e.g., a driver loaded
* Success Audit - access attempt is successful, e.g., a user login
* Failure Audit - access attempt fails, e.g., no access to a network drive

Log Types
* Application - events logged by an application, e.g., a database app
* Security - security access and resources, e.g., creating an object
* System - logs by system components, e.g., failure of a driver

# Task 3 - wevtutil.exe
wevtutil.exe is a CLI tool that is useful when you need to sift through a lot of events

* Count log names
  ```
  C:\Users\Administrator\Desktop>wevtutil.exe el > e.txt

  C:\Users\Administrator\Desktop>find /v /c "" e.txt

  ---------- E.TXT: 1071
  ```

# Task 4 - Get-WinEvent
Get-WinEvent is a PowerShell cmdlet you can use to search through Windows Event Logs

Docs
* https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.diagnostics/get-winevent?view=powershell-5.1

Example
* Get-WinEvent -LogName Application | Where-Object { $_.ProviderName -Match 'WLMS'}

Microsoft recommends using the FilterHashtable parameter to filter logs using one key-value pair at a time

Docs
* https://docs.microsoft.com/en-us/powershell/scripting/samples/Creating-Get-WinEvent-queries-with-FilterHashtable?view=powershell-7.1

Examples

https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.diagnostics/Get-WinEvent?view=powershell-7.1

* Search for logs
    ```
    PS C:\Users\Administrator\Desktop> Get-WinEvent -ListLog * | Where-Object { $_.LogName -Match 'Open' }

    LogMode   MaximumSizeInBytes RecordCount LogName
    -------   ------------------ ----------- -------
    Circular             1052672           0 OpenSSH/Admin
    Circular             1052672           0 OpenSSH/Operational    
    ```
* Providers
    ```
    PS C:\Users\Administrator\Desktop> Get-WinEvent -ListProvider *PowerShell*


    Name     : PowerShell
    LogLinks : {Windows PowerShell}
    Opcodes  : {}
    Tasks    : {Engine Health
            , Command Health
            , Provider Health
            , Engine Lifecycle
            ...}

    Name     : Microsoft-Windows-PowerShell
    LogLinks : {Microsoft-Windows-PowerShell/Operational, Microsoft-Windows-PowerShell/Analytic, Microsoft-Windows-PowerShell/Debug,
            Microsoft-Windows-PowerShell/Admin}
    Opcodes  : {win:Start, win:Stop, Open, Close...}
    Tasks    : {CreateRunspace, ExecuteCommand, Serialization, Powershell-Console-Startup...}

    Name     : Microsoft-Windows-PowerShell-DesiredStateConfiguration-FileDownloadManager
    LogLinks : {Microsoft-Windows-PowerShell-DesiredStateConfiguration-FileDownloadManager/Operational,
            Microsoft-Windows-PowerShell-DesiredStateConfiguration-FileDownloadManager/Analytic,
            Microsoft-Windows-PowerShell-DesiredStateConfiguration-FileDownloadManager/Debug}
    Opcodes  : {}
    Tasks    : {FileDownloadManagerDownload, FileDownloadManagerValidate}
    ```
* Get Event Ids
    ```
    PS C:\Users\Administrator\Desktop> (Get-WinEvent -ListProvider Microsoft-Windows-PowerShell).Events | Format-Table Id, Description

    Id Description
    -- -----------
    4097 Computer Name $null or . resolve to LocalHost
    4098 Resolving to default scheme http
    4099 Remote shell name resolved to default Microsoft.PowerShell
    4100 %3...
    4101 %3...
    4102 %3...
    4103 %3...
    4104 Creating Scriptblock text (%1 of %2):...
    4105 Started invocation of ScriptBlock ID: %1...
    4106 Completed invocation of ScriptBlock ID: %1...
    7937 %3...    
    ...
    ...
    ...
    ...
    ```
