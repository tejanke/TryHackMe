# Room
https://tryhackme.com/room/powershell

# Task 1 - Objectives
Objectives

# Task 2 - What is PowerShell?
PowerShell is the Windows Scripting Language and shell environment that is built using the .NET framework.  PowerShell commands are formatted using Verb-Noun

Common Verbs
* Get
* Start
* Stop
* Read
* Write
* New
* Out

Approved Verbs List
* https://docs.microsoft.com/en-us/powershell/scripting/developer/cmdlet/approved-verbs-for-windows-powershell-commands?view=powershell-7

# Task 3 - Basic PowerShell commands
* get-help
  * get-help commandname
* get-command
  * get-command verb-*
  * get-command *-noun
* pipeline | - used to pass output from one cmdlet to another
  * verb-noun | get-member
* select-object
* where-object
* operators
  * -contains
  * -eq
  * -gt
  * https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/where-object?view=powershell-7.1&viewFallbackFrom=powershell-6
* sort-object

Practical
```
PS C:\> get-childitem -recurse *interesting-file.txt*
```
```
PS C:\> gc "C:\program files\interesting-file.txt.txt"
```
```
PS C:\> get-command -type cmdlet | measure-object | select-object Count

Count
-----
 6638
```
```
PS C:\> get-filehash "C:\Program Files\interesting-file.txt.txt" -alg md5
```
```
PS C:\> get-location

Path
----
C:\
```
```
PS C:\> test-path "C:\Users\Administrator\Documents\Passwords"
False
```
```
invoke-webrequest www.google.com
```
```
[System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String(string_here)
```

# Task 4 - Enumeration
Answer questions based on using PowerShell only

Local users
```
get-localuser
get-localuser | select name,SID
get-localuser | select passwordrequired
```
Local groups
```
get-localgroups | measure
```
Networking
```
get-netipaddress
get-nettcpconnection | where {$_.State -eq "Listen"} | measure | select count
get-nettcpconnection | where {$_.localport -eq "445"}
```
Patches
```
get-hotfix | measure
get-hotfix | where {$_.HotFixID -eq "KB4023834" }
```
Files
```
get-childitem -literalpath c:\ *.bak* -file -recurse | gc
get-childitem c:\ -recurse | select API_KEY | select filename
```
Processes
```
get-process
```
Scheduled Tasks
```
get-scheduledtask
get-scheduledtask taskname
```
Permissions
```
get-acl c:\
```

# Task 5 - Scripting Challenge
Find the password and HTTPS link in the documents in the emails directory
```
$dirs = get-childitem C:\users\Administrator\Desktop\emails
foreach($dir in $dirs){
    $docs = get-childitem C:\users\Administrator\Desktop\emails\$dir
    foreach($doc in $docs){
        write-host $doc
        get-content C:\users\Administrator\Desktop\emails\$dir\$doc | select-string password
        get-content C:\users\Administrator\Desktop\emails\$dir\$doc | select-string https
    }
}
```

# Task 6 - Intermediate Challenge
Make a simple port scanner with Test-NetConnection (very slow)
```
$ip = read-host -Prompt "Enter a single IP address to scan"
$ports = read-host -Prompt "Enter port range to scan such as 10-20"
$ports = $ports.Replace("-","..")
$port_range = invoke-expression $ports
$open_ports = 0
foreach($port in $port_range){
    $result = test-netconnection -computer $ip -port $port | select TcpTestSucceeded
    if($result.TcpTestSucceeded -eq $True){
        write-host "Port $port open."
        $open_ports++
        }
  }
write-host "There are $open_ports open ports on $ip"
```