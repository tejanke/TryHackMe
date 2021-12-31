# Room
https://tryhackme.com/room/ssrfqi

# Task 1 - Intro
* SSRF = Server-Side Request Forgery
* a vulnerability that allows a malicious user to make the web server create requests to a target of the attacker's choosing
* two types
    * regular - data returned to attacker's screen
    * blind - no info returned to attacker's screen

# Task 2 - SSRF Examples
* Build a SSRF to return the flag
    * https://website.thm/item/2?server=server.website.thm/flag?id=9&x=&server=api

# Task 3 - Finding a SSRF
* Common SSRF
    * when a full URL is used in a parameter
        * https://website.thm/form?server=http://othersite.thm/store
    * in a hidden form field
        * value="http://api.website.thm/store"
    * a partial URL is used as a parameter
        * https://website.thm/form?server=api
    * a path of the URL is used as a parameter
        * https://website.thm/form?dst=/forms/contact
* Resources
    * https://requestbin.com/

# Task 4 - Defeating Common SSRF Defenses
* Deny List - all requests are accepted except from those on the deny list
    * Bypass with localhost references like 0, 127.1.2.3, or 127.0.0.1.nip.io
* Allow List - all requested are denied unless they are specifically allowed
    * Bypass by taking advantage of loose matching, must begin with: website.thm, loose match: website.thm.attacker.com
* Open Redirect - server redirects to another website
    * Bypass similar to allow list

# Task 5 - Practical
* Open the support website and create an account.  Visit the hidden endpoint /customers/new-account-page to view/change your avatar.  Reviewing the page source notice that the full path is given for the avatar background image.  Change the value to a test value and update the profile.  Change the value to x/../private to default the rule and access the base64 encoded flag.