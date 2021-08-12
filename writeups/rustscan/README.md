# Room
https://tryhackme.com/room/rustscan

# Task 1 - About
* https://github.com/RustScan/RustScan

# Task 2 - Install
* https://github.com/RustScan/RustScan/wiki/Installation-Guide

# Task 3 - Accessibility
RustScan provides accessibility options to help with it's useability for ALL people

# Task 4 - Fast
RustScan is a very fast, low-level, asynchronous scanner

# Task 5 - Extensibility
RustScan has extensibility through the RustScan Scripting Engine, it supports:
* Python
* Shell script
* Perl
* Any binary program in the $PATH

# Task 6 - Adaptibility
RustScan can adapt it's operation based on feedback from what it is scanning

# Task 7 - Practical
* Scan all ports
```
rustscan -a 1.2.3.4
```
* Pass the nmap version check
```
rustscan -a 1.2.3.4 -- -sV
```
* Pass the nmap aggressive scan flag
```
rustscan -a 1.2.3.4 -- -A
```

# Task 8 - Quiz
* Get help
```
rustscan -h
```
* Use quiet mode
```
rustscan -q
```
* Use a port range
```
rustscan -r
```
* Check the version
```
rustscan -v
```
* Select a batch size for the scan
```
rustscan -b
```
* Set a timeout for the scan
```
rustscan -t
```