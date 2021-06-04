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

