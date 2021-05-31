# Room
https://tryhackme.com/room/linuxfundamentalspart2

# Task 1 - Intro
Course Intro

# Task 2 - SSH to machine
SSH is a remote terminal that is encrypted.  SSH to the box and complete the tasks

# Task 3 - Flags and Switches
Most programs allow you to specify command line arguments in the form of flags or switches to extend the functionality of the command

```
ls -a
ls --help
man ls
ls -h
```

# Task 4 - Filesystem interaction
Filesystem interaction commands
* touch - create a file
* mkdir - create a directory
* cp - copy a file or directory
* mv - move a file or directory
* rm - delete a file or directory
* file - determines the type of the file

```
touch test1
mkdir test2
cp test1 test2
mv test2\test1 .
file test1
rm test1
```

# Task 5 - Permissions 101
Common permissions include
* read = r
* write = w
* execute = x

To find the permission of a file you could use ls -l
```
tryhackme@linux2:~$ ls -l myfile
-rw-r--r-- 1 tryhackme tryhackme 16 May  5 10:47 myfile
```

Permissions are assigned on the basis of
* user (owner)
* group
* other (everyone else)

Permissions have number values assigned to them as well
* read = 4
* write = 2
* execute = 1

Example
```
tryhackme@linux2:~$ ls -l myfile
-rw-r--r-- 1 tryhackme tryhackme 16 May  5 10:47 myfile
│ │  │  │
| |  |  |
| |  |  └────────────────── everyone else permissions, here they are r-- or 4
| |  └───────────────────── group permissions, here they are r-- or 4
| └──────────────────────── owner permissions, here they are rw- or 4+2 = 6
└────────────────────────── the - indicates a file, d indicates directory

The total permission value read left to right is 6 (rw-) 4 (r--) 4 (r--) or 644
```

Other commands
* su - the su command can be used to switch to another user
* su [user] - switch to another user in the current directory
* su -l [user] - inherits environment variables, drops your shell in the user's home directory

# Task 6 - Common Directories
Common Directories in the Filesystem
* /etc - stores system file used for the operating system as well as configurations, /etc/passwd, /etc/shadow, /etc/sudoers
* /var - variable data, used for frequently accessed or written services, /var/log
* /root - the root user's home directory
* /tmp - volatile temporary data store

# Task 7 - Conclusion
Conclusion

# Task 8 - Advance
Advanced to part 3