# Room
https://tryhackme.com/room/investigatingwindows

# Task 1 - Investigating Windows
* Find current Windows version with year
    ```
    systeminfo | findstr /C:"OS Name:"
    ```
* Find the last logged in user
    ```
    get-winevent -filterhashtable @{logname='Security'; id=4648} | sort | select -first 1 | fl | findstr /c:"Account Name:"    
    ```
* Check user logins
    ```
    get-winevent -filterhashtable @{logname='Security'; id=4648} | sort | fl | findstr "TimeCreated John"
    ```
* Basic targetted search for specific IP
    ```
    get-winevent -logname system | fl | findstr "[0-9][0-9]\.[0-9][0-9]\.[0-9]\."
    ```
* Check Windows startup in the registry
  * https://lazyadmin.nl/it/windows-10-startup-folder-location/

* List users in the Administrators group
    ```
    get-localgroupmember -Group "Administrators"
    ```

* List custom scheduled tasks
    ```
    get-scheduledtask | where-object {$_.taskpath -eq "\"}
    ```

* Grab information on a scheduled task
    ```
    schtasks /query /tn "clean file system" /xml    
    ```

* Check for last login
    ```
    get-eventlog -logname security -instanceid 4624 | ?{$_.message -match "Jenny"}
    ```