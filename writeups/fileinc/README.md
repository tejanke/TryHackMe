# Room
https://tryhackme.com/room/fileinc

# Task 1 - Intro
* File inclusion includes LFI (Local File Inclusion), RFI (Remote File Inclusion), and directory traversal
* Parts of a URL
    * http://webapp.thm/get.php?file=usercv.pdf
        * http - protocol
        * webapp.thm - domain
        * get.php - file
        * ? - query string
        * file - parameters

# Task 2 - Deploy the VM
Deploy the VM

# Task 3 - Path Traversal
* Path traversal is also known as directory traversal
* It can occur when user input is passed to a function like file_get_contents in PHP
* Another name for the attack is dot-dot-slash, ../
* The idea is you go up one directory for each ../ until you reach the root, then you make a path to the target file
* Example Linux items of interest
    * /etc/issue
    * /etc/profile
    * /proc/version
    * /etc/passwd
    * /etc/shadow
    * /root/.bash_history
    * /var/log/dmessage
    * /var/mail/root
    * /root/.ssh/id_rsa
    * /var/log/apache2/access.log

# Task 4 - Local File Inclusion - LFI
* LFI often occurs because of no security awareness
* Example LFI with no directory specified
    * /lab1.php?file=/etc/passwd
* Example LFI with directory defined
    * /lab1.php?file=../../../../etc/passwd

# Task 5 - Local File Inclusion - LFI #2
* More LFI labs
* Filters can prevent ../, to get around that use ....// which will match ../ and leave you with ../
* Explicit file typing can append a file extension, to remove that use the null byte %00 or 0x00

# Task 6 - Remote File Inclusion - RFI
* RFI is a technique to include remote files into a vulnerable application
* Occurs when input is not sanitized
* RFI risk is higher since it can lead to RCE

# Task 7 - Remediation
* Keep systems and services up to date
* Turn off errors that leak to the user
* Use a WAF
* Disable functions that cause file inclusion vulnerabilities
* Analyze the web app
* Sanitize user input
* Specify allow and block lists

# Task 8 - Challenge
* Challenge 1
    * to grab the flag you must change the static form method from GET to POST, you can use developer tools to do this in a browser
    * the file requested should be the one in the challenge
* Challenge 2
    * to grab the flag you'll need to abuse the Cookie and set the value to that of the file you are looking for, you also need to pass a null byte to defeat the static file extension
* Challenge 3
    * to grab this flag you have to use curl with the -X flag for POST
* RCE
    * host a text file locally with "<?php echo shell_exec('hostname');?>" in it
    * in the vulnerable input box place the URL To your hosted file