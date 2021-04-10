# Room
https://tryhackme.com/room/malresearching

# Task 1 - Intro
Intro

# Task 2 - Deploy
Deploy VM

# Task 3 - Checksums 101
Checksums are the result of mathematical operations against an input with a fixed length output being a sequence of characters.  Checksums use bits as the input for the math operations.  The more complex math operations, the higher the security.  Checksums are also known as hashes and their primary purpose is to verify the integrity of data

Files with different contents having the same hash is known as a hash collision.  This is rare and representative of the complexity of the math operation that the hash is derived from

The term for an individual piece of binary is a bit.  Some example hash algorithms are MD5, SHA1, SHA-256, and SHA-512.  Ronald Rivest developed the MD5 algorithm

# Task 4 - Online Sandboxing
Sandboxing is a technique used to isolate processes and prevent direct interaction with one another.  Examples include using Virtualbox to run an OS.  Some malware has been known to escape virtual environments.  Some online services include:

* https://any.run/
* https://hybrid-analysis.com/

Complete a task by reviewing analysis from any.run for Emotet

# Task 5 - Practical
Practical using hashtab, get-filehash, and certutil.exe

```
get-filehash [filename] -algorithm [algorithm]
```

```
certutil -hashfile [filename] [algorithm]
```

# Task 6 - VirusTotal
Practical using VirusTotal to review a report

# Task 7 - Conclusion
Fin