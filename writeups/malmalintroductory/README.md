# Room
https://tryhackme.com/room/malmalintroductory

# Task 1 - Purpose of Malware Analysis
Malware analysis is a form of incident response and one should consider:
* Point of Entry - where did the malware come from?
* Indicators of Compromise - has the malware been executed?
* What it does - infect other devices, install backdoors?
* Prevention - can it be prevented?

# Task 2 - Malware Campaigns
Targeted
* Created for a specific purpose against a specific target

Mass Campaign
* Most common
* Infect as many devices as possible

# Task 3 - Identify if a Malware Attack has happened
Malware attack process
* Delivery
  * USB
  * PDF attachments
* Execution
  * Encryption
  * Key Loggers
  * Adware
* Maintaining Persistence
  * After gaining access, keep it
* Propagation
  * Infect as many as possible

Signature types
* Host-Based
  * Results of execution process
  * Have files been modified
  * Has additional software been installed
* Network-Based
  * Network communication
  * Searching for shares
  * Call home

# Task 4 - Static vs Dynamic Analysis
Two categories of Malware Analysis
* Static
  * gain a high level abstraction of the sample
  * signature analysis
  * checksums
* Dynamic
  * executing the sample and observing what happens

# Task 5 - Tools
Static Analysis
* Dependency Walker - depends
* PeID
* PE Explorer
* PEview
* ResourceHacker
* IDA Freeware
* WinDbg

# Task 6 - Analysis environment
Connect via RDP

# Task 7 - MD5 checksums
Reviewing MD5 hashes in Windows using the hashtab application

http://implbits.com/products/hashtab/

# Task 8 - Check MD5 hashes
Use the MD5 hashes of the applications found in the task and look them up in Virustotal to see if they are malicious

https://www.virustotal.com/gui/home/search

# Task 9 - Check if an exe is obfuscated / packed
PeID is a great tool for checking the compiler / packer of a file.  The hex value for an executable is always "4D 5A"

Use PeID to discover the compiler for a few task files

# Task 10 - Obfuscation / Packing
Packing is a form of obfuscation that is used to prevent analysis of programs

Use PeID to discover the packer for a task file

# Task 11 - Packed & Non-Packed Code
PeID can automatically detect a lot of packers, but it cannot de-obfuscate them

Open IDA pointing to example packed file

# Task 12 - Intro to Strings
Strings are the ASCII/Text contents of a program, for example, passwords, addresses, etc

strings --accepteula [filename]

Use strings and PE Explorer to examine task files

# Task 13 - Intro to Imports
Disassemblers reverse compiled code from machine code to human-readable instructions (assembly).  Debuggers use the same techniques as disassemblers but facilitate analysis and stepping through an application's execution

Use IDA to examine a task file

# Task 14 - Practical
Use MD5 hash, Virustotal, strings, and PeID on a task file