# Room
https://tryhackme.com/room/linuxmodules

# Task 1 - Intro
Commands covered
* du
* grep, egrep, fgrep
* tr
* awk
* sed
* xargs
* curl
* wget
* xxd

# Task 2 - du
du stands for disk usage, it helps you identify files and directories along with how much space they use.

Flags
* -a - list files and folders
* -h - human readable format
* -c - print total size
* -d [number] - folder depth
* --time - timestamp

Examples
```
du -a /home/

du -a /home/ | grep user

du --time -d 1 .
```

# Task 3 - grep
Grep searches a file for a particular pattern of characters and displays all lines that contain that pattern, the pattern searched is referred to as the regular expression

Syntax
* grep "PATTERN" file.txt

egrep, fgrep, and grep
* egrep matches regular expressions in a string
* fgrep searches for a fixed string
* grep can do both with the -E and -F flags

Flags
* -R - recursive
* -h - disable prefixing of filenames in results
* -c - lists how many times the pattern was found
* -i - ignores case
* -l - lists the filename only, not the pattern
* -n - line number
* -v - not contains
* -E - match regular expressions in a string
* -e - specify multiple patterns

# Task 4 - tools
String Manipulations

Tools
* tr
* awk
* sed
* xargs
* sort
* uniq

# Task 5 - tr
tr - translate

Flags
* -d - delete a set of characters
* -t - concat source and dest
* -s - replace source with dest
* -c - reverse

Resources
* https://www.geeksforgeeks.org/tr-command-in-unix-linux-with-examples/
* https://linuxize.com/post/linux-tr-command/

# Task 6 - awk
Awk is a scripting language used for manipulating data and generating reports

Syntax
* awk [flags] [select pattern/find(sort/commands)] [input file]

Operation
* printing
    ```
    awk '{print}' b.txt
    ippsec youtube hackthebox 34024
    john youtube ctf 50024
    thecybermentor tcmsec courses 25923
    liveoverflow youtube ctf 45345
    nahamsec hackerone bughunting 12365
    stok hackerone bughunting 1234
    ```
* searching for a pattern
    ```
    awk '/ctf/' b.txt
    john youtube ctf 50024
    liveoverflow youtube ctf 45345
    ```
* field variables joined
    ```
    awk '{print $1 $3}' b.txt 
    ippsechackthebox
    johnctf
    thecybermentorcourses
    liveoverflowctf
    nahamsecbughunting
    stokbughunting
    ```
* field variables space
    ```
    awk '{print $1,$3}' b.txt 
    ippsec hackthebox
    john ctf
    thecybermentor courses
    liveoverflow ctf
    nahamsec bughunting
    stok bughunting
    ```
* NR variable, number record, numbers lines
    ```
    awk '{print NR,$0}' b.txt
    1 ippsec youtube hackthebox 34024
    2 john youtube ctf 50024
    3 thecybermentor tcmsec courses 25923
    4 liveoverflow youtube ctf 45345
    5 nahamsec hackerone bughunting 12365
    6 stok hackerone bughunting 1234
    ```
* FS variable, field separator, defined what field to display as well as delimiter
    ```
    awk 'BEGIN{FS="o"} {print $2}' b.txt
    utube hacktheb
    hn y
    r tcmsec c
    verfl
    ne bughunting 12365
    k hacker
    ```
* FS variable with END
    ```
    awk 'BEGIN{FS="o"} {print $1,$3} END{print "Total rows= " NR}' b.txt
    ippsec y x 34024
    j utube ctf 50024
    thecyberment urses 25923
    live w y
    nahamsec hacker 
    st ne bughunting 1234
    
    Total rows= 7
    ```
* RS variable, record separator, default is new line \n
    ```
    awk 'BEGIN{RS="o"} {print $0}' b.txt
    ippsec y
    utube hacktheb
    x 34024
    j
    hn y
    utube ctf 50024
    thecyberment
    r tcmsec c
    urses 25923
    live
    verfl
    w y
    utube ctf 45345
    nahamsec hacker
    ne bughunting 12365
    st
    k hacker
    ne bughunting 1234
    ```
* OFS variable, output field separator, delimiter while outputing
    ```
    separates only when variables defined, not whole line

    awk 'BEGIN{OFS=":"} {print $0}' b.txt
    ippsec youtube hackthebox 34024
    john youtube ctf 50024
    thecybermentor tcmsec courses 25923
    liveoverflow youtube ctf 45345
    nahamsec hackerone bughunting 12365
    stok hackerone bughunting 1234

    separates only when variables defined, not whole line

    awk 'BEGIN{OFS=":"} {print $1,$2,$3.$4}' b.txt
    ippsec:youtube:hackthebox34024
    john:youtube:ctf50024
    thecybermentor:tcmsec:courses25923
    liveoverflow:youtube:ctf45345
    nahamsec:hackerone:bughunting12365
    stok:hackerone:bughunting1234

    reflection join

    awk 'BEGIN{OFS=":"} {print $0,$0}' b.txt
    ippsec youtube hackthebox 34024:ippsec youtube hackthebox 34024
    john youtube ctf 50024:john youtube ctf 50024
    thecybermentor tcmsec courses 25923:thecybermentor tcmsec courses 25923
    liveoverflow youtube ctf 45345:liveoverflow youtube ctf 45345
    nahamsec hackerone bughunting 12365:nahamsec hackerone bughunting 12365
    stok hackerone bughunting 1234:stok hackerone bughunting 1234    
    ```
* ORS variable, output record separator, separate output
    ```
    awk 'BEGIN{ORS="\n\n"} {print $0}' b.txt
    ippsec youtube hackthebox 34024

    john youtube ctf 50024

    thecybermentor tcmsec courses 25923

    liveoverflow youtube ctf 45345

    nahamsec hackerone bughunting 12365

    stok hackerone bughunting 1234
    ```
* resources
    * https://www.tutorialspoint.com/awk/awk_workflow.htm
    * http://osr5doc.xinuos.com/en/OSUserG/_The_printf_statement.html
    * https://www.geeksforgeeks.org/awk-command-unixlinux-examples/
* usage tips
    * $0 is the whole line
    * awk is not zero indexed
    * use single quotes ' and '
    * awk treats double quotes "" as a raw string

Flags
* -f - specify the .awk script file to use
* -F - specify field separator without using BEGIN statement
* -v - specify variables
* -D - debug your scripts
* -o - specify output file

# Task 7 - sed
sed - Stream EDitor, a tool that can perform find and replace, searching, insertion, deletion, etc.

Syntax
* sed [falgs] [patter/script] [input file]

Flags
* -e - the following is a script command
* -f - file containing string pattern
* -E - used to extend regular expressions
* -n - suppress automatic printing or pattern spacing

Operation
* replace one character with another
    ```
    sed -e 's/o/O/g' file.txt
      │  │  │ │ │ │     │
      │  │  │ │ │ │     └─────────────────── input file
      │  │  │ │ │ └───────────────────────── operate globally on the input
      │  │  │ │ └─────────────────────────── replace with this
      │  │  │ └───────────────────────────── match this
      │  │  └─────────────────────────────── substitute mode
      │  └────────────────────────────────── what follows is the sed script
      └───────────────────────────────────── launch sed

    ippsec yOutube hackthebOx 34024
    jOhn yOutube ctf 50024
    thecybermentOr tcmsec cOurses 25923
    liveOverflOw yOutube ctf 45345
    nahamsec hackerOne bughunting 12365
    stOk hackerOne bughunting 1234
    ```
* replace word on specific lines
    ```
    sed -e '1,3 s/youtube/YOUTUBE/g' file.txt
      │  │  │ │ │    │       │    │     │
      │  │  │ │ │    │       │    │     └── input file
      │  │  │ │ │    │       │    └──────── operate globally on the input
      │  │  │ │ │    │       └───────────── replace with this
      │  │  │ │ │    └───────────────────── match this
      │  │  │ │ └────────────────────────── substitute mode
      │  │  │ └──────────────────────────── end search at line 3
      │  │  └────────────────────────────── start search at line 1
      │  └───────────────────────────────── what follows is the sed script
      └──────────────────────────────────── launch sed

    ippsec YOUTUBE hackthebox 34024
    john YOUTUBE ctf 50024
    thecybermentor tcmsec courses 25923
    liveoverflow youtube ctf 45345
    nahamsec hackerone bughunting 12365
    stok hackerone bughunting 1234
    ```
* view specific lines
    ```
    sed -n '3,5p' file.txt
      │  │  │ ││    │
      │  │  │ ││    └────────────────────── input file
      │  │  │ │└─────────────────────────── print matching pattern
      │  │  │ └──────────────────────────── end at line 5
      │  │  └────────────────────────────── start at line 3
      │  └───────────────────────────────── suppress output duplicates
      └──────────────────────────────────── launch sed

    thecybermentor tcmsec courses 25923
    liveoverflow youtube ctf 45345
    nahamsec hackerone bughunting 12365
    ```
* view the entire file except specific lines
    ```
    sed '3,5d' file.txt
      │  │ ││    │
      │  │ ││    └───────────────────────── input file
      │  │ │└────────────────────────────── print everything except pattern
      │  │ └─────────────────────────────── end at line 5
      │  └───────────────────────────────── start at line 3
      └──────────────────────────────────── launch sed

    ippsec youtube hackthebox 34024
    john youtube ctf 50024
    stok hackerone bughunting 1234
    ```
* view specific ranges of lines, chaining sed scripts
    ```
    sed -n -e '1,2p' -e '4,5p' file.txt
      │  │  │  │ ││   │  │ ││    │
      │  │  │  │ ││   │  │ ││    └───────── input file
      │  │  │  │ ││   │  │ │└────────────── print matching pattern
      │  │  │  │ ││   │  │ └─────────────── end at line 5
      │  │  │  │ ││   │  └───────────────── start at line 4
      │  │  │  │ ││   └──────────────────── what follows is the sed script
      │  │  │  │ │└──────────────────────── print matching pattern
      │  │  │  │ └───────────────────────── end at line 2
      │  │  │  └─────────────────────────── start at line 1
      │  │  └────────────────────────────── what follows is the sed script
      │  └───────────────────────────────── suppress output duplicates
      └──────────────────────────────────── launch sed  

    ippsec youtube hackthebox 34024
    john youtube ctf 50024
    liveoverflow youtube ctf 45345
    nahamsec hackerone bughunting 12365
    ```
* replace specific Nth occurence of pattern
    ```
    sed 's/o/O/1' file.txt
      │  │ │ │ │     │
      │  │ │ │ │     └──────────────────── input file
      │  │ │ │ └────────────────────────── replace ONLY the first occurence of pattern
      │  │ │ └──────────────────────────── replace with this
      │  │ └────────────────────────────── match this
      │  └──────────────────────────────── substitute mode
      └─────────────────────────────────── launch sed

    ippsec yOutube hackthebox 34024
    jOhn youtube ctf 50024
    thecybermentOr tcmsec courses 25923
    liveOverflow youtube ctf 45345
    nahamsec hackerOne bughunting 12365
    stOk hackerone bughunting 1234
    ```

* replace specific Nth occurence of pattern
    ```
    sed 's/o/O/2' file.txt
      │  │ │ │ │     │
      │  │ │ │ │     └──────────────────── input file
      │  │ │ │ └────────────────────────── replace ONLY the second occurence of pattern
      │  │ │ └──────────────────────────── replace with this
      │  │ └────────────────────────────── match this
      │  └──────────────────────────────── substitute mode
      └─────────────────────────────────── launch sed    

    ippsec youtube hackthebOx 34024
    john yOutube ctf 50024
    thecybermentor tcmsec cOurses 25923
    liveoverflOw youtube ctf 45345
    nahamsec hackerone bughunting 12365
    stok hackerOne bughunting 1234
    ```    
* replace Nth occurence and every match after
    ```
    sed 's/e/E/2g' file.txt
      │  │ │ │ ││    │
      │  │ │ │ ││    └──────────────────── input file
      │  │ │ │ │└───────────────────────── operate globally, replace the rest
      │  │ │ │ └────────────────────────── replace second occurence and...
      │  │ │ └──────────────────────────── replace with this
      │  │ └────────────────────────────── match this
      │  └──────────────────────────────── substitute mode
      └─────────────────────────────────── launch sed    

    ippsec youtubE hackthEbox 34024
    john youtube ctf 50024
    thecybErmEntor tcmsEc coursEs 25923
    liveovErflow youtubE ctf 45345
    nahamsec hackEronE bughunting 12365
    stok hackeronE bughunting 1234
    ```
* use regex to match space
    ```
    cat file1.txt 

    ippsec     youtube hackthebox 34024
    john youtube    ctf 50024
    thecybermentor    tcmsec courses     25923
    liveoverflow  youtube    ctf 45345
    nahamsec     hackerone     bughunting 12365
    stok hackerone           bughunting 1234

    sed 's/  */ /g' file1.txt
      │  │ │││ │ │   │ 
      │  │ │││ │ │   └──────────────────── input file
      │  │ │││ │ └──────────────────────── operate globally
      │  │ │││ └────────────────────────── replace with one space
      │  │ ││└──────────────────────────── match any number of previous
      │  │ │└───────────────────────────── match next trailing space
      │  │ └────────────────────────────── match first space
      │  └──────────────────────────────── substitute mode
      └─────────────────────────────────── launch sed        

    ippsec youtube hackthebox 34024
    john youtube ctf 50024
    thecybermentor tcmsec courses 25923
    liveoverflow youtube ctf 45345
    nahamsec hackerone bughunting 12365
    stok hackerone bughunting 1234
    ```

Resources
* https://www.geeksforgeeks.org/sed-command-in-linux-unix-with-examples/
* https://www.gnu.org/software/sed/manual/sed.html
* https://www.tecmint.com/linux-sed-command-tips-tricks/

# Task 8 - xargs
xargs handles positional arguments in a command

Flags
* -0 - terminate arguments with null, helps with spaces in filenames
* -a [file] - read file
* -d [delimiter] - delimiter
* -L [int] - max number of non blank inputs
* -s [int] - buffer size while running xargs
* -x - exit the command if buffer size exceeded
* -E [str] - specify end of file string
* -I [str] - replace occurence in arguments
* -p - prompt user before running command
* -r - if input is blank don't run
* -n [int] - limit of max args
* -t - verbose

Operations
* use echo to pass 3 strings as input to xargs, in xargs turn on verbose [-t], rename the input strings to "argVar" [-I argVar], and finally run bash to touch each arg and list it
    ```
    echo "file1 file2 file3" | xargs -t -I argVar bash -c '{ touch argVar; ls -lrta argVar; }'

    bash -c '{ touch file1 file2 file3; ls -lrta file1 file2 file3; }'
    -rw-r--r-- 1 abc abc 0 Feb 13 08:22 file3
    -rw-r--r-- 1 abc abc 0 Feb 13 08:22 file2
    -rw-r--r-- 1 abc abc 0 Feb 13 08:22 file1
    ```
* use find to look for files recursively from the current directory and pass their null separated names [-print0] (to account for spaces in filenames) to xargs, in xargs change the argument terminator to null [-0] (helps with spaces in filenames), turn on verbose [-t], prompt the user if they wish to run the command [-p], run the command rm -f on each argument
    ```
    ls -lrta 

    -rw-r--r-- 1 abc abc 0 Feb 13 08:28 file3
    -rw-r--r-- 1 abc abc 0 Feb 13 08:28 file2
    -rw-r--r-- 1 abc abc 0 Feb 13 08:28 file1

    find . -type f -print0 | xargs -0 -t -p rm -f
    
    rm -f ./file3 ./file1 ./file2?...y
    
    ls
    ```
* use find to look for files recursively from the current directory and pass their null separated names [-print0] (to account for spaces in filenames) ignoring any permissions errors [2>/dev/null] to xargs, in xargs change the argument terminator to null [-0] (helps with spaces in filenames), and then run the egrep command, egrep takes a regex pattern in single quotes that will search for 1- any line starting with "r" [^r] 2- that matches an AlPhAnUmEr1C pattern [[[:alnum:]]] and 3- ends with "0" [*0$]
    ```
    head flag.txt; wc flag.txt
    eMFm5ES3tZBwYMfaxbCYv56fwX3eCtJn
    sWscbzQ8JlghCBcvI7nupl64tbILlUYL
    8x5y0uPfLWApFlsm3JWbVA0a7E63UdP9
    QA4TasEIDTIV5GGXRrtDOkmtW74Gsvzm
    HGIBQPcFebvmjeRcdF0XNxLXNBxX0Yoe
    h1bTBhyZwACbyopIfNCKgQLOgwLNDZ4c
    XFckYhk9HvmrypQnTVWZw1Vx6BXcRGvE
    arReN9OLg5b1gMA2ZJQJtYRm86U4tqwj
    ai2QuCyiNer0vpEZDeP3pcI1voASQxjF
    lCHo2Exctjmiq7a7UTT82sNQzEIVeI5C
    1000  1000 33000 flag.txt

    find . -type f -print0 2>/dev/null | xargs -0 egrep '^r[[:alnum:]]*0$'
    rAJr4MvzgvIMJ9nPHfy6wWvRbvUM5J90
    ```

Tips
* You can escape command line flags with --

Resources
* https://www.hackingarticles.in/exploiting-wildcard-for-privilege-escalation/

# Task 9 - uniq and sort
The unique command filters output and removes duplicate lines that are adjacent to each other.  The sort command sorts lines alphabetically and numerically

uniq flags
* -c - count occurrences of every line
* -d - only print lines that are repeated
* -u - only print lines that are already unique
* -i - ignore case

sort flags
* -r - reverse order
* -c - check if file is already sorted
* -u - sort and remove duplicate lines
* -o [file] - save output to file

# Task 10 - curl
curl stands for crawl URL, it outputs the data of a URL to the screen.  curl can be used for troubleshooting, searching for data, and recon on a target

Syntax
* curl [url]

Flags
* -# - display a progress meter
* -o [file] - save with a name you specify
* -O - save with the name as is from the server
* -C - - resume broken download
* --limit-rate - limits the download or upload rate
* -u - user authentication
* -T - helps upload files
* -x - specify a proxy server
* -I - show headers
* -A - specify user-agent
* -L - follow redirects
* -b - save a cookie
* -d - POST data
* -X - specify method

Resources
* https://www.geeksforgeeks.org/curl-command-in-linux-with-examples/
* https://curl.se/docs/manpage.html
* https://www.tecmint.com/linux-curl-command-examples/

# Task 11 - wget
wget can retrieve information from a URL

Flags
* -b - background the download process
* -c - resume partial download
* -t [int] - specify number of times to retry
* -O [filename] - specify output name of downloaded file
* -o [filename] - overwrite logs in another file
* -a [filename] - append logs
* -i [filename] - read list of URLs from a file
* --user [username] - login username
* --password [password] - login password
* --ask-password - ask for a password during the login process
* --limit-rate=[size] - limit download rate, size in k, m, kB, and mB
* -w=[int] - waiting time before fetching the URL
* -T=[int] - timeout waiting for the URL
* -N - enable timestamps
* -U - specify the user-agent

# Task 12 - xxd
xxd is used for hexdumps

Flags
* -b - display binary representation
* -E - change character encoding from ASCII to EBCDIC
* -c [int] - sets the number of bytes to be represented in one row
* -g - how many bytes/octets should be in a group
* -i - output formatting
* -l - length of output
* -p - converts string passed into plain hexdump
* -r - revert hexdump to binary
* -u - use uppercase hex letters
* -s - seek at offset

Operations
* hexdump your string
    ```
    echo "hello world" | xxd
    00000000: 6865 6c6c 6f20 776f 726c 640a            hello world.
    ```
* change character set to EBCDIC
    ```
    echo "hello world" | xxd -E
    00000000: 6865 6c6c 6f20 776f 726c 640a            ..%%?..?.%..    
    ```
* binary output
    ```
    echo "hello world" | xxd -b
    00000000: 01101000 01100101 01101100 01101100 01101111 00100000  hello 
    00000006: 01110111 01101111 01110010 01101100 01100100 00001010  world.
    ```
* c format
    ```
    echo "hello world" | xxd -i
    0x68, 0x65, 0x6c, 0x6c, 0x6f, 0x20, 0x77, 0x6f, 0x72, 0x6c, 0x64, 0x0a
    ```
* specify length
    ```
    echo "hello world" | xxd -l12
    00000000: 6865 6c6c 6f20 776f 726c 640a            hello world.
    
    echo "hello world" | xxd -l5
    00000000: 6865 6c6c 6f                             hello
    ```

Tips
* read plaintext
    ```
    cat file | xxd -r -p
    ```

# Task 13 - gpg, tar, and others

gpg
* GNU Privacy Guard
* encrypt and decrypt files
* https://www.tutorialspoint.com/unix_commands/gpg.htm
* http://irtfweb.ifa.hawaii.edu/~lockhart/gpg/

tar
* tape archive
* gzip, bzip, archiving
* https://neverendingsecurity.wordpress.com/2015/04/13/linux-tar-commands-cheatsheet/
* https://www.geeksforgeeks.org/tar-command-linux-examples/

id
* list user group associations

pwd
* print current working directory

uname
* provides system information

ps
* list processes

kill
* terminate processes

netstat
* lists open system ports
* has a relative: ss
* https://www.rekha.com/netstat-cheat-sheet-for-newbies.html
* https://linux.die.net/man/8/netstat
* https://neverendingsecurity.wordpress.com/2015/04/13/ss-socket-statistics-commands-cheatsheet/

less
* less is more
* view files, forward scrolling
* https://www.tecmint.com/linux-more-command-and-less-command-examples/#:~:text=Learn%20Linux%20%27less%27%20Command,using%20page%20up%2Fdown%20keys.

more
* more is less
* view files, backwards scrolling

most
* view files backwards and forwards
* https://ostechnix.com/the-difference-between-more-less-and-most-commands/
* 

diff
* compare byte by byte
* can only use on 2 files at a time
* https://www.networkworld.com/article/3279724/comparing-files-and-directories-with-diff-and-comm.html#:~:text=The%20diff%20command%20would%20make,both%20commands%20is%20the%20same.&text=The%20comm%20command%20can%20provide,it%20can%20compare%20two%20files.
* https://www.geeksforgeeks.org/diff-command-linux-examples/

comm
* what is common between two files
* https://www.geeksforgeeks.org/comm-command-in-linux-with-examples/

base64
* encode and decode base32/64

tee
* reads from stdin and writes to stdout
* use instead of file direction if you want to view results onscreen live

file
* reads the file headers to tell you what type of file it is

stat
* same as file with more detail

export
* used to set environment variables
* https://www.geeksforgeeks.org/export-command-in-linux-with-examples/

reset
* reset your terminal in case it starts acting up

systemctl
* interact with systemd, service manager
* https://stackoverflow.com/questions/43537851/difference-between-systemctl-and-service-command#:~:text=service%20operates%20on%20the%20files,file%20in%20%2Fetc%2Finit.
* https://gist.github.com/adriacidre/307d2f9f5179fc748f22edac5af3d218

service
* initialize services

tips
* use netcat as a port scanner
    ```
    nc -v -z 127.0.0.1 1000-5000
    ```
* use ss to list ports

# Task 14 - FIN