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

