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

# Task 5 - XPath Queries
XPath - XML Path Language.  Windows Event Log supports a subset of XPath 1.0

Docs
* https://docs.microsoft.com/en-us/windows/win32/wes/consuming-events#xpath-10-limitations

XPath example using Get-WinEvent (the filter is case sensitive)
```
PS C:\Users\Administrator> Get-WinEvent -logname application -filterxpath '*/System/EventID=100'


ProviderName: WLMS

TimeCreated                     Id LevelDisplayName Message
-----------                     -- ---------------- -------
12/21/2020 4:23:47 AM          100
12/18/2020 3:18:57 PM          100
12/15/2020 8:50:22 AM          100
12/15/2020 8:18:34 AM          100
12/15/2020 7:48:34 AM          100
12/14/2020 6:42:18 PM          100
12/14/2020 6:12:18 PM          100
12/14/2020 5:39:08 PM          100
12/14/2020 5:09:08 PM          100    
```
XPath example using wevtutil.exe (the filter is case sensitive)

```
PS C:\Users\Administrator> wevtutil.exe qe application /q:*/System[EventID=100] /f:text /c:1
Event[0]:
Log Name: Application
Source: WLMS
Date: 2020-12-14T17:09:08.940
Event ID: 100
Task: None
Level: Information
Opcode: Info
Keyword: Classic
User: N/A
User Name: N/A
Computer: WIN-1O0UJBNP9G7
Description:
N/A
```

To filter on a provider use the Name attribute
```
PS C:\Users\Administrator> Get-WinEvent -logname application -filterxpath '*/System/Provider[@Name="WLMS"]'


   ProviderName: WLMS

TimeCreated                     Id LevelDisplayName Message
-----------                     -- ---------------- -------
12/21/2020 4:23:47 AM          100
12/18/2020 3:18:57 PM          100
12/15/2020 8:50:22 AM          100
12/15/2020 8:48:34 AM          101
12/15/2020 8:18:34 AM          100
12/15/2020 7:48:34 AM          100
12/14/2020 7:12:18 PM          101
12/14/2020 6:42:18 PM          100
12/14/2020 6:12:18 PM          100
12/14/2020 6:09:09 PM          101
12/14/2020 5:39:08 PM          100
12/14/2020 5:09:08 PM          100
```

Two queries together
```
PS C:\Users\Administrator> Get-WinEvent -logname application -filterxpath '*/System/EventID=101 and */System/Provider[@Name="WLMS"]'


   ProviderName: WLMS

TimeCreated                     Id LevelDisplayName Message
-----------                     -- ---------------- -------
12/15/2020 8:48:34 AM          101
12/14/2020 7:12:18 PM          101
12/14/2020 6:09:09 PM          101
```

Getting EventData
```
PS C:\Users\Administrator> Get-WinEvent -logname security -filterxpath '*/EventData/Data[@Name="TargetUserName"]="System"' -maxevents 1


   ProviderName: Microsoft-Windows-Security-Auditing

TimeCreated                     Id LevelDisplayName Message
-----------                     -- ---------------- -------
3/7/2021 3:31:49 PM           4624 Information      An account was successfully logged on....
```
Filtering for a specific time
```
PS C:\Users\Administrator> Get-WinEvent -logname application -filterxpath '*/System/Provider[@Name="WLMS"] and */System/TimeCreated[@SystemTime="2020-12-15T01:09:08.940277500Z"]'


   ProviderName: WLMS

TimeCreated                     Id LevelDisplayName Message
-----------                     -- ---------------- -------
12/14/2020 5:09:08 PM          100
```
Filtering for user and event id
```
PS C:\Users\Administrator> Get-WinEvent -logname security -filterxpath '*/EventData/Data[@Name="TargetUserName"]="Sam" and */System/EventID=4724'


   ProviderName: Microsoft-Windows-Security-Auditing

TimeCreated                     Id LevelDisplayName Message
-----------                     -- ---------------- -------
12/17/2020 1:57:14 PM         4724 Information      An attempt was made to reset an account's password..
```

Further docs
* https://docs.microsoft.com/en-us/previous-versions/dotnet/netframework-4.0/ms256115(v=vs.100)

# Task 6 - Event IDs
Resources
* Windows Logging Cheat Sheet
  * https://static1.squarespace.com/static/552092d5e4b0661088167e5c/t/580595db9f745688bc7477f6/1476761074992/Windows+Logging+Cheat+Sheet_ver_Oct_2016.pdf
* Spotting the Adversary with Windows Event Log Monitoring
  * https://apps.nsa.gov/iaarchive/library/reports/spotting-the-adversary-with-windows-event-log-monitoring.cfm
* MITRE ATT&CK
  * https://attack.mitre.org/
* Events to Monitor
  * https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/plan/appendix-l--events-to-monitor
* Windows 10 and Windows Server 2016 Security Auditing and Monitoring Reference
  * https://www.microsoft.com/en-us/download/confirmation.aspx?id=52630
* Logging Windows
  * https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_logging_windows?view=powershell-7.1
* Greater Visibility Through PowerShell Logging
  * https://www.fireeye.com/blog/threat-research/2016/02/greater_visibilityt.html
* Configure PowerShell logging to see PowerShell anomalies in Splunk
  * https://docs.splunk.com/Documentation/UBA/5.0.4/GetDataIn/AddPowerShell
* Search the event log with PowerShell
  * https://4sysops.com/archives/search-the-event-log-with-the-get-winevent-powershell-cmdlet/

# Task 7 - Practice

* Searching events from an offline event file
   ```
   Get-WinEvent -filterhashtable @{path="merged.evtx"; id=400; }
   ```
* Searching for a keyword in the event message
   ```
   Get-WinEvent -filterhashtable @{path="merged.evtx"} | where-object -property Message -Match 'net1.exe' | format-list
   ```

# Task 8 - Conclusion
Reading Material
* https://github.com/sbousseaden/EVTX-ATTACK-SAMPLES
* https://devblogs.microsoft.com/powershell/powershell-the-blue-team/
* https://medium.com/palantir/tampering-with-windows-event-tracing-background-offense-and-defense-4be7ac62ac63