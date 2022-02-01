# room
https://tryhackme.com/room/splunk2gcd5

# task 1 - intro
* deploy the VM
* contents from boss of the soc 2017
* resources
    * https://github.com/splunk/botsv2

# task 2 - data
* data review
* resources
    * https://docs.splunk.com/Documentation/Splunk/latest/SearchReference/Metadata
    * https://www.splunk.com/en_us/blog/tips-and-tricks/metadata-metalore.html
* reference command for metadata
    ```
        |  metadata type=sourcetypes index=botsv2 
        |  eval firstTime=strftime(firstTime, "%Y-%m-%d %H:%M:%S") 
        |  eval lastTime=strftime(lastTime, "%Y-%m-%d %H:%M:%S") 
        |  eval recentTime=strftime(recentTime, "%Y-%m_%d %H:%M:%S") 
        |  sort - totalCount
    ```

# task 3 - level 100 questions
* go through and find information about Amber and her actions
* some search queries from the tasks that i found useful
    ```
    index="botsv2" sourcetype="pan:traffic" app="web-browsing"

    index="botsv2" sourcetype="pan:traffic" app="web-browsing" src_ip="[ambers_ip]"

    index="botsv2" [ambers_ip] sourcetype="stream:http"

    index="botsv2" [ambers_ip] sourcetype="stream:http" 
    |  stats count by site

    index="botsv2" [ambers_ip] sourcetype="stream:http" [site_name]

    index="botsv2" [ambers_ip] sourcetype="stream:http" [site_name]
    | dedup site
    | stats count by site

    index="botsv2" [ambers_ip] sourcetype="stream:http" [site_name] image/png 
    |  stats count by uri_path

    index="botsv2" sourcetype="stream:smtp" amber

    index="botsv2" sourcetype="stream:smtp" [ambers_lastname]
    | stats count by sender_mail_from
    ```

# task 4 - level 200 questions
* find information about brewertalk
* some search queries that were helpful for me
    ```
    index="botsv2" amber tor

    index="botsv2" amber tor install 
    |  reverse

    index="botsv2" brewertalk dest_port=53| spath "query_type{}" | search "query_type{}"=A

    index="botsv2" brewertalk.com src_ip="[ip_address]"

    * sourcetype="stream:http" kevin 
    |  stats count by cookie 
    |  sort - count
    ```

# task 5 - level 300 questions
* Mallory and her macbook
* some search queries that were helpful for me
    ```
    index="botsv2" mallory

    index="botsv2" mallory host="MACLORY-AIR13" (*.ppt OR *.pptx)

    index="botsv2" sourcetype=ps *.crypt

    index="botsv2" kutekitten "\\/users\\/mkraeusen\\/*" 
    |  stats count by columns.md5    
    ```
* virustotal was useful in learning more about the file hash

# task 6 - level 400 questions
* Forthly vs APT
* some search queries that were helpful for me
    ```
    index="botsv2" attachment sourcetype="stream:smtp"
    | stats count by attach_filename{}

    index="botsv2" invoice.zip password

    index="botsv2" 45.77.65.211 sourcetype="stream:TCP" ssl_issuer="*"

    index="botsv2" winsys32.dll

    index="botsv2" sourcetype="stream:ftp"

    index="botsv2" sourcetype="stream:ftp" method=RETR

    index="botsv2" \\Software\\Microsoft\\Network sourcetype=WinRegistry data="*"
    ```
* virustotal and the other links were useful in learning more about the file