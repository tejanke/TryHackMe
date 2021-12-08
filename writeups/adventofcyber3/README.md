# Room
https://tryhackme.com/room/adventofcyber3

# Task 1 - Intro
Intro

# Task 2 - Socials
Socials

# Task 3 - Swag
Swag

https://store.tryhackme.com/

# Task 4 - Rules
Rules

# Task 5 - Story
McSkidy is back, yeah!

# Task 6 - Day 1 - Web Exploitation / Save the Gifts
1. What is an IDOR vulnerability
   * IDOR - Insecure Direct Object Reference
   * an access control vulnerability
   * when an attacker gains access to information not intended for them
2. How to find IDOR vulnerabilities
   * found by changing user supplied data
   * change components in a request or cookie
3. IDOR challenge walkthrough
   * In the challenge change the user_id parameter to find and answer questions

# Task 7 - Day 2 - Web Exploitation / Elf HR Problems
1. HTTP
   * HTTP = Hypertext Transfer Protocol
   * HTTP is a client-server protocol used between a client and a web server
   * HTTP is a request response protocol
   * HTTP is stateless
   * A few HTTP methods include
     * GET - client requests content from a server
     * HEAD - similar to get but retrieves just the header
     * POST - client submits content to a server
     * PUT - replaces all representations of the target resource with the PUT request
2. Cookies
   * Cookies allow the stateless HTTP protocol to identify users and provide access control, among other things
   * A cookie is a piece of session metadata that resides on the client device
   * Cookies are set in the response portion of the conversation by the server
   * Cookies are sent by the client to present state and identify it as previously authenticated
   * Cookies typically are serialized in JSON format
   * A few cookie components include
     * Name - unique name
     * Value - unique value to help track state
     * Domain - web domain that the cookie is used in (scope)
     * Path - local path to the cookie
    * Manipulation
      * Cookie manipulation is an attack used to obtain unintended behavior from the target
3. Cookie manipulation example
   * Obtain cookie
   * Decode cookie
   * Identify cookie structure
   * Decode/change paramters of the cookie
   * Encode the cookie with the manipulated values
   * Refresh the web page or use the manipulated cookie in your request/script
4. Cookie manipulation challenge
   * Load the challenge web site.  Open developer tools.  Refresh the page.  Go to Storage > Cookies tab in developer tools.  Grab the cookie value and manipulate it based on the challenge to gain admin access.  One useful tool for this is https://gchq.github.io

# Task 8 - Day 3 - Web Exploitation / Christmas Blackout
1. Content Discovery
   * Content = assets and inner workings of the application: files, folders, pathways
   * Content Discovery - find things we aren't supposed to see normally: config files, passwords, backups, etc
2. Discovering Content
   * Manually - manually traverse a file system looking for items of interest
   * With Tools - use tools such as dirbuster and gobuster to help discover valuable assets
3. Default Credentials
   * Apps and services often come with default credentials enabled, you can exploit this
4. Challenge
   * Use a tool to find the admin page
   ```
   gobuster dir -w directory-list-lowercase-2.3-big.txt -u http://10.10.227.249
   ```
   * Use default creds to access the admin page
   * Find the flag

# Task 9 - Day 4 - Web Exploitation / Santa's Running Behind
1. Authentication
   * Authentication - process of verifying a user's identity
   * Proven via username and password, tokens, biometrics
   * Authentication is not Authorization, Authorization is what permissions are granted to the authenticated session
2. Fuzzing
   * Fuzzing - automated means of testing an element of a web app
   * Tools to perform fuzzing - Burp Suite, ffuf
3. Challenge
   * Load the web page from the challenge.  Launch Burp.  Click the Proxy tab and make sure the "Intercept is on" button is enabled (default).  In the web browser use FoxyProxy to proxy requests to Burp.  In the web page enter bogus login information and submit.  In Burp the POST request is held, right click and choose "Send to Intruder".  Click the Intruder tab.  In the Intruder tab click the Positions tab.  Clear out the positions with the clear button.  Highlight your bogus password and click the add button.  Change attack type to Sniper.  Go to the Payloads tab.  Ensure Payload set 1 is selected.  Click the Load button in Payload Options and find the wordlist in the /root folder.  Click Start Attack.

# Task 10 - Day 5 - Web Exploitation / Pesky Elf Forum
1. 
