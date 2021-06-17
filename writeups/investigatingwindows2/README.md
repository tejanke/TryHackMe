# Room
https://tryhackme.com/room/investigatingwindows2

# Task 1
A practical exam focused on Windows internal investigation

Research
* Utilize autoruns from sysinternals to answer a few challenge questions
  * https://docs.microsoft.com/en-us/sysinternals/downloads/autoruns
* Examine the script file
* Locate the script file
  * get-childitem [scriptname] -recurse
* Disable the script stopping process explorer
* Use process monitor and process explorer to track what the script is doing
* Use loki to scan the local system looking for IOCs
  * loki -l log.txt
