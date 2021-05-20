# Room
https://tryhackme.com/room/httpindetail

# Task 1 - What is HTTP(S)
* HTTP - HyperText Transfer Protocol
  * set of rules for communicating with web servers
* HTTPS - HyperText Transfer Protocol Secure
  * secure version of HTTP, encrypted

# Task 2 - Requests and Responses
HTTP is a request / response protocol

* URL - Uniform Resource Locator
  * instruction on how to access a resource on the internet
  * http://user:password@website.com:80/testing?id=1234#task1
    * http = scheme/protocol
    * user:password = for services that require authentication it can be passed in this fashion
    * website.com = host
    * 80 = port, HTTP is usually 80, HTTPS is usually 443
    * testing = path, the file name or location of the resource
    * ?id=1234 = query string
    * #task1 = fragment / page reference pointer

* Request
  * GET / HTTP/1.1
    * GET = request method
    * / = page being requested
    * HTTP/1.1 = the version of HTTP

* Example
```
GET / HTTP/1.1
Host: tryhackme.com
User-Agent: Mozilla/5.0 Firefox/87.0
Referer: https://tryhackme.com/

```
* Line 1 - request method, page being requested, and HTTP version
* Line 2 - host site we are requesting
* Line 3 - the local user agent
* Line 4 - a referer reference
* Line 5 - blank

* Example Response Fields
  * Server = web server software and version
  * Date = current date and time of the web server
  * Content-Type = what sort of information is transmitted, HTML, images, etc
  * Content-Length = how long the response is

# Task 3 - HTTP Methods
HTTP methods are a way for the client to show their intended action.

* GET - get information from the server
* POST - submit data to the server
* PUT - submit and update information to the server
* DELETE - remove information from the server

# Task 4 - HTTP Status Codes
Ranges
* 100-199 - Informational
* 200-299 - Success
* 300-399 - Redirection
* 400-499 - Client Errors
* 500-599 - Server Errors

Common Status Codes
* 200 OK - request completed with success
* 201 - Created - resource created
* 301 - Permanent Redirect - redirects browser
* 302 - Temporary Redirect - temporary redirect
* 400 - Bad Request - the request was bad
* 401 - Not Authorized - authentication is incorrect
* 403 - Forbidden - no permissions
* 404 - Page Not Found - page doesn't exist
* 405 - Method Not Allowed - resource doesn't allow this request
* 500 - Internal Service Error - server error
* 503 - Service Unavailable - server can't handle your request

# Task 5 - Headers
Headers are additional bits of data you can send to the web server when making requests

Common Request Headers
* Host - the host header allows you to specify what actual website you are looking to go to for a web server that hosts multiple web sites, such as www.example.com or www.example2.com
* User-Agent - advises the web server of your browser details so that it can format the website properly
* Content-Length - tells the server how much data to expect
* Accept-Encoding - tells the server what type of compression the browser supports
* Cookie - session cookie to use

Common Response Headers
* Set-Cookie - session information to store
* Cache-Control - how long to store the content you receive
* Content-Type - what type of data is returned, HTML, CSS, images, etc
* Content-Encoding - what method of compression is used

# Task 6 - Cookies
Cookies are small pieces of data stored on your computer to use in your session.  Cookies are saved when you receive the Set-Cookie header.  Every subsequent request uses the Cookie header with that cookie.  Cookies remind the server who you are.  Cookies are used to store information about your session like authentication

# Task 7 - Making Requests
HTTP Challenge with manual requests

```
GET /room HTTP/1.1
Host: tryhackme.com
User-Agent: Mozilla/5.0 Firefox/87.0
```

```
GET /blog?id=1 HTTP/1.1
Host: tryhackme.com
User-Agent: Mozilla/5.0 Firefox/87.0
```

```
DELETE /user/1 HTTP/1.1
Host: tryhackme.com
User-Agent: Mozilla/5.0 Firefox/87.0
Content-Length: 0
```

```
PUT /user/2 HTTP/1.1
Host: tryhackme.com
User-Agent: Mozilla/5.0 Firefox/87.0
Content-Length: 14

username=admin 
```

```
POST /login HTTP/1.1
Host: tryhackme.com
User-Agent: Mozilla/5.0 Firefox/87.0
Content-Length: 33

username=thm&password=letmein 
```