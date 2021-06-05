# Room
https://tryhackme.com/room/hardeningbasicspart2

# Task 1 - Intro
Intro

# Task 2 - Quiz
GPG uses a nonce for the session key and follows the OpenGPG standard.  To generate GPG keys use gpg --gen-key.  For symmetric encryption of a file use gpg -c, asymmetric gpg -e

SSH version 2 is the most secure version at this time.  To generate SSH keys use ssh-keygen.  Keys are stored in a user's home directory in the subdirectory .ssh.  If you need to specify the type of get to generate with ssh-keygen use -t.  All SSH config is stored in /etc/ssh/sshd_conf

References:
* https://www.gnupg.org/gph/de/manual/r1023.html
* https://linux.die.net/man/1/ssh-keygen

# Task 3 - GNU Privacy Guard
PGP is widely used to encrypt and decrypt email.  When your email is sent, it is encrypted with your own public key as well as a session key, nonce.  The session key is encrypted with the public key and sent with cipher text.  To decrypt the email, the receiver decrypts with their private key in order to discover the session key.  The session key combined with the private key are used to decrypt the cipher text and original message

GPG Keys
* create keys: gpg --gen-key
* stored in directory: .gnugpg
* view keys: gpg --list-keys

# Task 4 - Encrypt your files
Symmetric encryption works by using one key to encrypt and decrypt

GPG encrypt a file
* symmetric encrypt: gpg -c file_name
* symmetric decrypt: gpg -d file_name

Asymmetric encryption uses two keys, one to encrypt (public key), one to decrypt (private key).  Never share the private key, always share the public key

GPG with asymmetric encryption
* export public keys: gpg --export -a -o file_name
* asymmetric encrypt file: gpg -e file_name

# Task 5 - SSH version 1
SSH version 1 has been replaced by version 2, you shouldn't use v1.  Configuration of the SSH protocol is done using /etc/ssh/sshd_config on the Protocol line

# Task 6 - SSH keys
You can use ssh-keygen to generate SSH keys.  They are stored in a hidden directory named .ssh off of the generating user's home directory.  You can use the -t switch to specify the type of encryption and -b for the bit size.  To login remotely to a server using SSH keys, copy your public key to it using ssh-copy-id username@server.  You can also copy them manually by logging into the remote host via password, opening the .ssh/authorized_keys file, and pasting the local hosts .ssh/id_rsa.pub inside

# Task 7 - Disable Username & Password SSH Login
After you have verified login with SSH keys is working for a host, you can disable password based authentication by modifying the SSH configuration file at /etc/ssh/sshd_config and changing PasswordAuthentication yes to no.  If your keys do not work, or are lost, you will be locked out

# Task 8 - X11 Forwarding and SSH Tunneling
X11 Forwarding allows you to forward GUI application displays.  To turn it on/off modify the X11 Forwarding line in /etc/ssh/sshd_config

SSH Tunneling allows you to forward traffic over SSH to a remote host.  To modify it change the AllowTCPForwarding, GatewayPorts, and PermitTunnel in /etc/ssh/sshd_config

# Task 9 - SSH Logging
The log file for SSH is stored at /var/log/auth.log.  You can increase verbosity by modifying the LogLevel line in /etc/ssh/sshd_config.  The log levels are:
* QUIET
* FATAL
* ERROR
* INFO <--- default
* VERBOSE
* DEBUG1
* DEBUG2
* DEBUG3

# Task 10 - Mandatory Access Control
Mandatory Access Control (MAC) in Linux is implemented with SELinux and AppArmor and defines who can access what

# Task 11 - AppArmor
AppArmor is preinstalled in Ubuntu.  Both AppArmor and SELinux can be used to implement MAC.  AppArmor will:
* prevent malicious actors from accessing data on your systems
* let applications have their own profiles
* allow you to create custom profiles

AppArmor configuration is located in /etc/apparmor.d, the sbin.dhclient and usr.* files are AppArmor profiles.  The abstractions directory contains partially written profiles that you can use to create your own profiles

# Task 12 - AppArmor CLI Utilities
CLI Utilities
* install with apt install apparmor-utils
* aa-status - list app status and profiles loaded
  * status modes:
    * enforce - enforce the active profile
    * complain - allows process but it is logged
    * audit - same as complain but logged to /var/log/audit/audit.log
* aa-enforce
* aa-disable
* aa-audit
* aa-complain

# Task 13 - Chapter 4 Quiz
Quiz based on the content above

# Task 14 - SSH and Encryption
SSH and Encryption

# Task 15 - Conclusion
Conclusion