# Room
https://tryhackme.com/room/oscommandinjection

# Task 1 - Intro
* Command Injection - the abuse of an app's behavior to execute commands on the OS with the privileges of the user running the app
* Also called RCE - Remote Code Execution
* Resources
    * https://www.contrastsecurity.com/security-influencers/insights-appsec-intelligence-report
    * https://owasp.org/www-project-top-ten/

# Task 2 - Discovering command injection
* Look for code that passes data from user input directly to a system call
* Examples
    * exec() in PHP
    * subprocess.popen() in Python

# Task 3 - Exploiting command injection
* Types of command injection
    * Blind - there is no direct output for you to tell if your payload executed or not
    * Verbose - direct output is available for you to verify your payload ran or not
* Detecting Blind command injection
    * Use commands that can stall the app
        * sleep
        * timeout
    * Use commands that generate network traffic
        * ping
    * Alternative output
        * redirect output to a file then cat it out
* Detecting Verbose command injection
    * Verify the output shown to you

# Task 4- - Remediating command injection
* Remediating command injection
    * Avoid vulnerable functions
    * Sanitize input with filters

# Task 5 - Practical - Command injection
* Test out various command injection to return data to the screen using the vulnerable input form
    * ;

# Task 6 - Conclusion
Conclusion