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

