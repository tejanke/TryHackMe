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

# Task 6 - Day 1 - Save the Gifts
1. What is an IDOR vulnerability
   * IDOR - Insecure Direct Object Reference
   * an access control vulnerability
   * when an attacker gains access to information not intended for them
2. How to find IDOR vulnerabilities
   * found by changing user supplied data
   * change components in a request or cookie
3. IDOR challenge walkthrough
   * In the challenge change the user_id parameter to find and answer questions

# Task 7 - Day 2 - Elf HR Problems
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

