# room
https://tryhackme.com/room/malremnuxv2

# task 1 - intro
intro

# task 2 - deploy
deploy

# task 3 - analyzing malicious pdfs
* PDFs can execute malicous javascript, python, exes, and powershell code
* tools
    * peepdf
    * peepdf demo.pdf
    * echo 'extract js > out.txt' > script.txt
    * peepdf -s script.txt demo.pdf
    * cat out.txt

# task 4 - analyzing malicious office macros
* malware infection via office docs is very common
* tools
    * vmonkey
    * vmonkey demo.doc

# task 5 - entropy, packing and unpacking
* remnux provides many tools for static analysis
* file entropy is indicative of bad intent of a file
* PE - Portable Executable
* file entropy scores how random the data within a PE is
    * scale 0 to 8
    * higher = more random
    * encrypted files have high entropy
    * high entropy files should be analyzed first
* packers use an executable as a source and output to another executable
* legit devs use packing to reduce the size of their apps and protect work from being stolen
* entry point - first pieces of code executed when launched
* when an executable is packed, it must be unpacked before code can execute
* packers change entry point from original location to unpacking stub
* packed files have high entropy
* upx is a common packer

# task 6 - memory
* tools
    * volatility
    * volatility -f mem.raw imageinfo
    * volatility -f mem.raw --profile=Win7SP1x64 pslist
    * volatility -f mem.raw --profile=Win7SP1x64 dlllist -p 3704

# task 7 - summary
summary

# task 8 - conclusion
* resources
    * https://docs.remnux.org/
    * https://downloads.volatilityfoundation.org/releases/2.4/CheatSheet_v2.4.pdf