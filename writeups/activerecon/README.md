# Room
https://tryhackme.com/room/activerecon

# Task 1 - Intro
Intro

# Task 2 - Web Browser
* The web browser is a convenient tool to help with active recon
* HTTP = TCP/80, HTTPS = TCP/443
* Browser developer tools are useful for inspecting some web logic
* Helpful addons
    * FoxyProxy
    * User-Agent Switcher and Manager
    * Wappalyzer

# Task 3 - Ping
* The primary purpose of ping is to check whether you can reach the remote system and the remote system can reach you
* ping 1.2.3.4
* ping -c 10 1.2.3.4
* ping -n 10 1.2.3.4

# Task 4 - Traceroute
* Traceroute traces the route taken by packets from your system to another host
* Find the IP addresses of routers or hops along the path
* traceroute 1.2.3.4
* tracert 1.2.3.4

# Task 5 - Telnet
* Telnet is a cleartext protocol that was developed in 1969, it used TCP port 23 by default.
* Using telnet from the CLI
    * telnet 1.2.3.4 80
* Submitting an HTTP request via telnet
    * telnet 1.2.3.4 80
    * GET / HTTP/1.1
    * host: telnet
    * [enter twice]

# Task 6 - Netcat
* netcat, nc, can both connect on and listen for TCP and UDP ports.
* nc -nvlp 9871
    * -n : no DNS resolution
    * -v : verbose output
    * -l : listen mode
    * -p : specify port
* nc 1.2.3.4 80

# Task 7 - Conclusion
Conclusion