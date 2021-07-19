# Room
https://tryhackme.com/room/linuxfunctionhooking

# Task 1 - Intro
Review Shared Libraries, Function Hooking, and LD_PRELOAD

# Task 2 - What are Shared Libraries
* Shared Libraries
  * pre-compiled C code
  * linked during final steps of producing an executable
  * provides reusable code
    * functions
    * routines
    * classes
    * data structures
  * contain addresses of functions required by programs during runtime
  * common shared libraries
    * libc
    * glibc
    * libcurl
    * libcrypt

# Task 3 - Technical Review
Review is sourced from man page of ld.so

* Example
  * check dynamically linked libraries needed by the ls command
    * ldd 'which ls'

* man info
  * DT_RPATH
  * DT_RUNPATH
  * LD_LIBRARY_PATH
  * DT_NEEDED
  * /etc/ld.so.cache
  * -z nodeflib
  * /lib
  * /usr/lib
  * LD_PRELOAD
  * --preload
  * /etc/ld.so.preload

# Task 4 - Code Example
Code Example

# Task 5 - Review
* Examples
  * export LD_PRELOAD=$(pwd)/malicious.so
  * sudo sh -c "echo $(pwd)/malicious.so > /etc/ld.so.preload"

* Check
  * ldd /bin/ls

# Task 6 - Hiding files from ls
* Examples
  * readdir()
  * dirent

# Task 7 - Conclusion
Conclusion
