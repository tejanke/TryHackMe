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