# Room
https://tryhackme.com/room/metasploitintro

# Task 1 - Intro
* Metasploit is a popular exploitation framework that supports all phases of a pentesting engagement
* Metasploit versions
    * Metasploit pro
    * Metasploit framework
* Main Metasploit framework components
    * msfconsole
    * modules
    * tools

# Task 2 - Main components of metasploit framework
* The metasploit console is launched with
    *msfconsole
* Terms 
    * exploit - a piece of code that uses a vulnerabiilty
    * vulnerability - a design, coding, or logic flaw that affects a system
    * payload - the exploit that takes advantage of a vulnerability
* metasploit modules and categories
    * /opt/metasploit-framework-5101/modules
    * auxiliary - supporting modules like scanners and fuzzers
    * encoders - obfuscate a payload
    * evasion - attempt to avoid AV
    * exploits - exploits available by OS/system
    * nops - do nothing code, one CPU cycle
    * payloads - exploit code that will take advantage of a vulnerability
    * post - modules to use in the last stage of the process
* payload types
    * singles - self contained payloads
    * stagers - setup a control connection to transfer other parts of the payload
    * stages - downloaded by the stager to proceed with exploitation chain

# Task 3 - msfconsole
* Launch the console with the msfconsole command
* msfconsole can be used like a regular shell and supports most Linux commands
* to get help - use the help command
* to show history - use the history command
* msfconsole supports tab completion to help you save time typing / feel through commands
* parameters are context specific, unless they are global, when you move away from your module context so does current reference to that parameter
* to enter a module, you will type the use command
* to display parameters in the current context, type show options
* to get more information on a specific option, type show [option_name]
* leave a context using the back command
* grab information from a module using the info command
* use the search command to look for modules, it supports fuzzy searching and type setting

# Task 4 - Working with modules
* use the set command to change a parameter
* use the unset command to put the parameter back to default
* use the unset all command to remove all parameter changes
* use the setg command to set global parameters
* use the unsetg command to put the global parameter back to default
* use the exploit or run command to launch the attack
    * -z will background the attack using the session as set below
* the background command will place the current session in the background
* the sessions command will list all active sessions

* some popular options include
    * RHOSTS - ip of the target
    * RPORT - port of the target
    * PAYLOAD - exploit used for the current attack
    * LHOST - the attacker IP
    * LPORT - the attacker port
    * SESSION - the metasploit session ID

# Task 5 - Summary
Summary