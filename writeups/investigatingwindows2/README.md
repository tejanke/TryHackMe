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
* Use process hacker to view disk activity
* Use loki to scan the local system looking for IOCs
  * loki -l log.txt
* Use strings and dump the results to a text file, then with regex find a pattern to improve yara
  * ^[a-zA-Z]{2,2}\.[a-zA-Z]{3,3}
  * ^[a-zA-Z0-9]{2,2}\.[a-zA-Z0-9]{3,3}
  * ^[a-zA-Z0-9]{2,2}\.[a-zA-Z0-9]{1,1}\.[a-zA-Z0-9]{5,5}