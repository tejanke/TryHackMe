# Room
https://tryhackme.com/room/burpsuitebasics

# Task 1 - Intro
Intro

# Task 2 - What is Burp Suite
* Burp Suite
    * Framework written in Java
    * Used for webapp testing, pentesting, mobile testing, and assessments
    * Captures and manipulates all traffic between attacker and web server
    * Editions
        * Community - free
        * Pro - paid, adds automations, removes rate limiters, more functionality
        * Enterprise - paid, used for continous scanning like Nessus

# Task 3 - Burp Community Features
* Burp Community features
    * proxy - allows interception and modification of requests and responses
    * repeater - capture, modify, and resend a request multiple times
    * intruder - brute forcing
    * decoder - decodes and encodes captured information
    * comparer - allows comparing text or bytes
    * sequencer - examination of session randomness
* Extensions
    * 3rd parties can add functionality to Burp
    * can be written in Java, Python, or Ruby

# Task 4 - Installation
* Resources
    * https://portswigger.net/
    * https://portswigger.net/burp/releases/professional-community-2021-10-3?requestededition=community

# Task 5 - Burp Dashboard
* Once you've opened Burp and started a temp project you'll be looking at the dashboard
* The dashboard is split in 4
    * tasks - status of background tasks running in Burp
    * event log - show what Burp is doing
    * issue activity - pro only - shows what vulnerabilites are found by the automated scanner
    * advisory - more info on vulns

# Task 6 - Navigation
* Burp has a standard menu that can be used to navigate with
* Keyboard shortcuts
    * dashboard - ctrl+shift+d
    * target - ctrl+shift+t
    * proxy - ctrl+shift+p
    * intruder - ctrl+shift+i
    * repeater - ctrl+shift+r

# Task 7 - Options
* Global settings are found on the User Options tab
* Project settings are found on the Project Options tab

# Task 8 - Intro to the proxy
* Capture requests and responses between attacker and target
* When 'intercept is on' is enabled, requests and responses are actively intercepted for a user to manipulate and either forward or drop
* When 'intercept is on' is not enabled, requests and responses are logged, but nothing further is done

# Task 9 - FoxyProxy
* FoxyProxy is a Firefox browser extension that allows easy redirection to Burp
* By default Burp listens on 127.0.0.1:8080, FoxyProxy allows you to quickly turn off and on sending to Burp
