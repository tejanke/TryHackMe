# Room
https://tryhackme.com/room/learnowaspzap

# Task 1 - Intro
ZAP is a free security testing framework like Burp Suite, from OWASP.  It is a enumeration tool used for testing web applications.

# Task 2 - Disclaimer
Documentation for ZAP is limited

# Task 3 - Installation
You can download ZAP here:

https://www.zaproxy.org/download/

# Task 4 - Automated scan
Automated scans perform both passive active scans to build a sitemap.  A traditional spider scan is passive and enumerates links and directories.  A Ajax Spider scan is an add-on that integrates AJAX and is used in conjunction with HTMLUnit.

# Task 5 - Manual Scanning
You'll want to import the ZAP certificate into your browser first.

Inside ZAP:
* Click Tools > Options
* Click Local Proxies
    * Set the address to 127.0.0.1
    * Change the port to whatever you wish, we'll use 8081
* Click Dynamic SSL Certificates
    * Click Save
    * Save the ZAP cert to your Desktop
    * Click Ok

Inside your browser (example Firefox):
* Click main menu > Preferences
* Search for "cert" in the Find Preferences search box
* Click View Certificates
    * Click Import
    * Point the file dialogue to the ZAP cert
    * Check both Trust this CA boxes
    * Click OK

Install FoxyProxy (example Firefox):
* Install FoxyProxy: https://addons.mozilla.org/en-US/firefox/addon/foxyproxy-standard/
* Once FoxyProxy is installed open it
* Click Options
    * Click Add
    * For Title type ZAP
    * For IP type 127.0.0.1
    * For Port type 8081 or whatever you used above
    * Click Save
* Activate the proxy by clicking FoxyProxy and choosing ZAP
* Deactivate the proxy by choosing Turn Off

# Task 6 - Scanning an Authenticated Web App
With ZAP open and your browser proxy pointing to it, navigate to the vulnerable DVWA page in your browser.  Login with the default creds.  Set DVWA Security to low.

Go to the ZAP window:
* Click Quick Start
* Click Automated Scan
* Type the IP of the web site you are scanning
* Uncheck use traditional spider
* Check use AJAX spider
* Change the with drop down to HTMLUnit
* Click Attack

# Task 7 - Brute forcing directories
ZAP can be used to brute force directories like dirbuster

Setup a default dictionary
* Click Tools > Options
* Click Forced Browse
* Click Select File and browse to a wordlist
* Click OK

Navigate to the site in your browser
* Right click the site you are browsing in the Sites menu
* Click Attack > Forced Browse Site
* Select your wordlist, click the play button

# Task 8 - Brute forcing web forms
ZAP can be used to brute force web forms like hydra

Setup the proxy and navigate to a login page like normal through the browser
* Enter a username and password
* Click login or submit

In ZAP
* In the Sites window scroll down to vulnerabilities
* Find the web form with the GET:brute{Login,password} field
* Right click and choose Attack > Fuzz
* In Fuzz Locations, in the body of the HTTP request, highlight the password you submitted
* Click Add
* In Payloads click Add
* In Add Payload change Type to File
* Click the Select button and point to your wordlist
* Click Add
* Click Ok
* Click Start Fuzzer

Review brute force
* In ZAP click the Fuzzer window
* Click the State column to sort by state
* Some false positivies may be present

# Task 9 - ZAP Extensions

* ZAP Extensions
    * https://github.com/zaproxy/zap-extensions

* Git clone HUNT from below
    * https://github.com/bugcrowd/HUNT

In ZAP setup passive scanning
* Click Tools > Options
* Click Passive Scanner
    * Check Only scan messages in scope

In ZAP download addons and enable HUNT.py
* Click the Manage Add-ons icon (colored cube)
* Install Community Scripts and Python Scripting Addons
* Install Custom Payload Addons
* Click the + sign next to Sites, select Scripts
* Select Passive Rules
* Select HUNT.py, right click, Enable script

# Task 10 - ZAP docs
* https://www.zaproxy.org/docs/desktop/ui/
* https://groups.google.com/g/zaproxy-users?pli=1
* https://www.alldaydevops.com/zap-in-ten