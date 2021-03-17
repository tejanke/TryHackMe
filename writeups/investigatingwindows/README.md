# Room
https://tryhackme.com/room/investigatingwindows

# Task 1 - Investigating Windows
* Find current Windows version with year
    ```
    systeminfo | findstr /C:"OS Name:"
    ```
* Find the last logged in user
    ```
    PS C:\Users\Administrator> get-winevent -filterhashtable @{logname='Security'; id=4648} | sort | select -first 1 | fl | findstr /c:"Account Name:"    
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