# Room
https://tryhackme.com/room/contentdiscovery

# Task 1 - Intro
* Content can be a file, pictures, backups, etc
* Looking for things that aren't intended to be public
* Discovery methods
    * Manual
    * Automated
    * OSINT

# Task 2 - Manual - Robots.txt
* Robots.txt is a document that tells search engines what pages to index or not

# Task 3 - Manual - favicon
* The favicon is the small icon shown in the browser address bar and is used for branding
* Some frameworks include default favicons, and if not changed can be used to identify the backend
* OWASP favicon database
    * https://wiki.owasp.org/index.php/OWASP_favicon_database

# Task 4 - Manual - Sitemap.xml
* The sitemap.xml gives a list of every file and directory that the owner wishes to be available on a search engine
* It can also be used to discover old content

# Task 5 - Manual - HTTP Headers
* Each web request includes various HTTP headers in the response
* Some headers can be used to identify the web server or other backend components that you can attack

# Task 6 - Manual - Framework stack
* Viewing the source of a web site can often give clues about the framework in use
* Use that information to research the frameworks documentation for default settings and credentials

# Task 7 - OSINT - Google Hacking / Dorking
* Dorking uses the advanced search feature of Google to extract certain information and display the result
* Examples
    * site: - results only from specific sites
    * inurl: - contains specific word in URL
    * filetype: - a particular file extension
    * intitle: - specific word in the title
* Resources
    * https://en.wikipedia.org/wiki/Google_hacking

# Task 8 - OSINT - Wappalyzer
* Wapalzer is a tool that helps identify frameworks, payment processors, etc
* https://www.wappalyzer.com/

# Task 9 - OSINT - Wayback Machine
* The Wayback machine is a historical archive of a site and allows you to see what a page looked like on different days and years
* https://archive.org/web/

# Task 10 - OSINT - GitHub
* Git is a version control system that tracks changes to files in a project
* GitHub is a hosted version of Git on the Internet

# Task 11 - OSINT - S3 Buckets
* S3 Buckets are a storage service provided by Amazon AWS that allows storage of files and static web site content
* A common S3 Bucket URL is : https://[name].s3.amazonaws.com

# Task 12 - Automated Discovery
* Automated discovery is the process of using tools to discover content
* These tools use wordlists
* Wordlist resource
    * https://github.com/danielmiessler/SecLists
* Example tools
    * ffuf
    * dirb
    * gobuster