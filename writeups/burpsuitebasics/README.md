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

# Task 10 - Proxying HTTPS
* To view HTTPS traffic in Burp you'll need to install the Burp CA
* Turn on intercept mode and go to http://burp/cert, download the cert
* In Firefox go to about:preferences and search for cert
* Click View Certificates and then Import the downloaded cert

# Task 11 - Burp Suite Browser
* Burp comes with a builtin Chromium based browser that can be used as an alternative to setting up FoxyProxy or similar in your browser of choice
* If you are running the Burp browser in a sandbox environment you will have to check "Allow the embedded browser to run without a sandbox" in Project options > MISC > Embedded Browser

# Task 12 - Scoping and Targeting
* Scoping allows you to filter out and display only what you are researching
* Selecting a scope is found in the Target tab
* If you'd like to restrict this further you can set "And URL Is in target scope" option in Proxy Options > Intercept Client Requests

# Task 13 - Site map and issue definitions
* Site map - allows you to map out the site, this is only done with manual browsing using the community edition, the pro edition allows an automated spider
* Scope - control the output to display only what we are researching
* Issue Definitions - list of web vulnerabilities

# Task 14 - Example Attack
* Navigate to the VM support site to create a ticket
* Notice how there is client side filtering to prevent testing XSS
* Setup Burp in intercept mode
* Enter a valid email and submit the request, in Burp modify the request and replace the email with a XSS test like <script>alert("success")</script>, forward it along

# Task 15 - Conclusion
Conclusion