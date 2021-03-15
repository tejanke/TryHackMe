# Room
https://tryhackme.com/room/sysmon

# Task 1 - Intro
Sysmon is a tool used to monitor and log events on Windows and is part of the Windows Sysinternals package

# Task 2 - Sysmon Overview
Sysmon is a Windows system service and device driver that remains resident across system reboots to monitor and log system activity to the Windows event log.  Sysmon is most commonly used in conjunction with a SIEM

Sysmon requires a config file to analyze events, examples

https://github.com/SwiftOnSecurity/sysmon-config

Sysmon analyzes a lot of Event IDs, here are a few
* 1 - process creation
* 3 - network connection
* 7 - image loaded
* 8 - createremotethread
* 11 - file created
* 12, 13, 14 - registry event
* 15 - filecreatestreamhash
* 22 - dnsevent

# Task 3 - Installation
Either install the standalone tool itself or the entire suite

https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon

https://docs.microsoft.com/en-us/sysinternals/downloads/sysinternals-suite

Configs are also required, examples

https://github.com/SwiftOnSecurity/sysmon-config

https://github.com/ion-storm/sysmon-config/blob/develop/sysmonconfig-export.xml

# Task 4 - Practice
The Sysmon configuration file is very important

Sysmon Best Practices
* Prioritize excluding events rather than including them, this prevents you from missing something crucial
* Remember CLI access using Get-WinEvent and wevutil.exe
* Know the environment before implementation

Practice with Get-WinEvent
* Count number of events with an ID of 3
    ```
    Get-WinEvent -path .\Filtering.evtx -filterxpath '*/System/EventID=3' | Measure-Object
    ```

# Task 5 - Hunting Metasploit
Metasploit is a commonly used exploit framework for penetration testing and red team ops

```
get-winevent -path .\HuntingMetasploit.evtx -filterxpath '*/System/EventID=3 and */EventData/Data[@Name="DestinationPort"] and */EventData/Data=444'


   ProviderName: Microsoft-Windows-Sysmon

TimeCreated                      Id LevelDisplayName Message
-----------                      -- ---------------- -------
1/4/2021 9:21:32 PM               3
```

# Task 6 - Detecting Mimikatz
Mimikatz is a well known credential dumping tool used mainly for getting information from LSASS

```
get-winevent -path .\HuntingMimikatz.evtx -filterxpath '*/System/EventID=10 and */EventData/Data[@Name="TargetImage"] and */EventData/Data="C:\Windows\system32\lsass.exe"'


   ProviderName: Microsoft-Windows-Sysmon

TimeCreated                      Id LevelDisplayName Message
-----------                      -- ---------------- -------
1/4/2021 10:22:52 PM             10
```

# Task 7 - Hunting Malware
Two popular forms of malware are RATs and backdoors.  RATs are remote access trojans used to gain remote access, examples are Xeexe and Quasar.  

```
get-winevent -path .\HuntingRats.evtx -filterxpath '*/System/EventID=3 and */EventData/Data[@Name="DestinationPort"] and */EventData/Data=8080'


   ProviderName: Microsoft-Windows-Sysmon

TimeCreated                      Id LevelDisplayName Message
-----------                      -- ---------------- -------
1/4/2021 11:44:35 PM              3
```

# Task 8 - Hunting Persistence
Persistence is used by attackers to maintain access after compromise

# Task 9 - Detecting Evasion Techniques
Malware authors use evasion techniques to remain undetected from anti-virus

Resources
* https://attack.mitre.org/techniques/T1564/004/
* https://attack.mitre.org/techniques/T1055/

# Task 10 - Practical
* Searching for processes and registry keys
    ```
    get-winevent -filterhashtable @{path=".\Investigation-1.evtx"; id=13;} | select-object -expandproperty properties | where-object {($_.value -match "svc") -or ($_.value -match "HKLM\\System")}
    ```
* Searching for access devices
    ```
    get-winevent -filterhashtable @{path=".\Investigation-1.evtx";} | select-object -expandproperty properties | where-object {($_.value -match "device\\")}
    ```
* Searching for executables
    ```
    get-winevent -filterhashtable @{path=".\Investigation-1.evtx";} | select-object -expandproperty properties | where-object {($_.value -match "exe")}
    ```
* Basic searching for IPs
    ```
    get-winevent -filterhashtable @{path=".\Investigation-2.evtx";} | select-object -expandproperty properties | where-object {($_.value -match "[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}")}
    ```
