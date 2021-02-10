# Room
https://tryhackme.com/room/avengers

# Task 1 - Deploy
Deploy VM

# Task 2 - Cookies
HTTP Cookies are used to store user information and preferences, they can also be used to track you.

# Task 3 - HTTP Headers
HTTP Headers let a client and server pass information between each other.  HTTP is a request/response protocol.  Header names a values are separated by a single colon :.  The two main HTTP methods are GET and POST.  GET is used to fetch information and POST is used to send it.

Get the flag
```
curl -I http://10.10.247.232
HTTP/1.1 200 OK
X-Powered-By: Express
flag2: [removed]
Content-Type: text/html; charset=utf-8
Content-Length: 7292
ETag: W/"1c7c-b4Vh59Xa/FV0DZE2ey13jTNNa4A"
Set-Cookie: connect.sid=s%3Akgkeya35Jz1hiBcYsvUpOm6rT81o5qLY.gJ8zzs5dBB1ZhtDERUgPTilNXxBPXaiDbZBKakPKOEc; Path=/; HttpOnly
Date: Tue, 09 Feb 2021 23:57:29 GMT
Connection: keep-alive
```

# Task 4 - Enumeration and FTP
Scan the machine with nmap
```
nmap -A -T4 [ip]
```
Connect to the FTP service and get the flag

# Task 5 - GoBuster
GoBuster is a fast directory scanner.  Use GoBuster to scan the host for the hidden directory

```
gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://10.10.247.232 -t 50
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.247.232
[+] Threads:        50
[+] Wordlist:       /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2021/02/09 19:02:58 Starting gobuster
===============================================================
```

# Task 6 - SQL Injection
SQL injection is a code injection technique that manipulates SQL queries

# Task 7 - Remote Code Execution
Complete challenge