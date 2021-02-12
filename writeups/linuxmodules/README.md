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

# Task 3 - 0xef
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

# Task 4 - STROPS
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

