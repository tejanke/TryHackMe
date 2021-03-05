# Room
https://tryhackme.com/room/yara

# Task 1 - Intro
Yara - Yet Another Ridiculous Acronym

https://github.com/virustotal/yara

# Task 2 - What is Yara?
Yara is the pattern matching swiss army knife for malware researchers.  Yara can identify information based on both binary and textual patterns.  Rules are used to label these patterns.  Malware uses strings to store textual data

# Task 3 - Installing Yara
Apt Linux distros
* sudo apt install yara
Via github for other Linux distros and Windows
* https://github.com/virustotal/yara

# Task 4 - Deploy VM
Deploy VM for challenge tasks

# Task 5 - Intro to Yara Rules
Yara uses a proprietary language for rules.  Yara rules are saved with the .yar extension.  Every yara command requires two arguments
* the rule file
* name of file, directory, or process ID to use the rule for

* Example
    ```
    touch afile

    vim firstrule.yar

    cat firstrule.yar
    rule examplerule {
            condition: true
    }

    yara firstrule.yar afile
    examplerule afile

    yara firstrule.yar notafile
    error scanning notafile: could not open file
    ```

# Task 6 - Expanding on Yara Rules
Yara Rules doc

https://yara.readthedocs.io/en/stable/writingrules.html

Great infographic

https://medium.com/malware-buddy/security-infographics-9c4d3bd891ef#18dd

* Meta
  * reserved for descriptive information by the rule author
* Strings
  * strings to search for
* Conditions
  * conditional statements for the rule
* Combining keywords
  * and, not, or

# Task 7 - Yara Modules
Frameworks that improve Yara functionality

Examples
* https://cuckoosandbox.org/
* https://pypi.org/project/pefile/

# Task 8 - Other tools
* LOKI
  * free Indictaor of Compromise scanner
* THOR
  * multi-platform IOC and Yara scanner
* FENRIR
  * a bash script similar to the two above
* YAYA
  * created by the EFF, runs on Linux only

# Task 9 - Using LOKI and its Yara rule set

Using Loki
* Help
  ```
    cmnatic@thm-yara:~/tools/Loki$ python loki.py -h                                                                                                   
  usage: loki.py [-h] [-p path] [-s kilobyte] [-l log-file] [-r remote-loghost]                                                                      
                [-t remote-syslog-port] [-a alert-level] [-w warning-level]                                                                         
                [-n notice-level] [--printall] [--allreasons] [--noprocscan]                                                                        
                [--nofilescan] [--nolevcheck] [--scriptanalysis] [--rootkit]                                                                        
                [--noindicator] [--reginfs] [--dontwait] [--intense] [--csv]                                                                        
                [--onlyrelevant] [--nolog] [--update] [--debug]                                                                                     
                [--maxworkingset MAXWORKINGSET] [--syslogtcp]                                                                                       
                [--logfolder log-folder] [--nopesieve] [--pesieveshellc]                                                                            
                [--nolisten] [--excludeprocess EXCLUDEPROCESS]                                                                                      
                                                                                                                                                    
  Loki - Simple IOC Scanner                                                                                                                          
                                                                                                                                                    
  optional arguments:                                                                                                                                
    -h, --help            show this help message and exit                                                                                            
    -p path               Path to scan                                                                                                               
    -s kilobyte           Maximum file size to check in KB (default 5000 KB)                                                                         
    -l log-file           Log file                                                                                                                   
    -r remote-loghost     Remote syslog system
    -t remote-syslog-port
                          Remote syslog port
    -a alert-level        Alert score
    -w warning-level      Warning score
    -n notice-level       Notice score 
    --printall            Print all files that are scanned
    --allreasons          Print all reasons that caused the score
    --noprocscan          Skip the process scan
  ```
* Update Loki
  ```
  python loki.py --update
  ```
* Running Loki against example files
  ```
  python ../../tools/Loki/loki.py -p .                                                                          
  python: can't open file '../../tools/Loki/loki.py': [Errno 2] No such file or directory                                                            
  cmnatic@thm-yara:~/suspicious-files$ python ../tools/Loki/loki.py -p .                                                                             
                                                                                                                                                    
        __   ____  __ ______                                                                                                                         
      / /  / __ \/ //_/  _/                                                                                                                         
      / /__/ /_/ / ,< _/ /                                                                                                                           
    /____/\____/_/|_/___/                                                                                                                           
        ________  _____  ____                                                                                                                        
      /  _/ __ \/ ___/ / __/______ ____  ___  ___ ____                                                                                              
      _/ // /_/ / /__  _\ \/ __/ _ `/ _ \/ _ \/ -_) __/                                                                                              
    /___/\____/\___/ /___/\__/\_,_/_//_/_//_/\__/_/                                                                                                 
                                                                                                                                                    
    Copyright by Florian Roth, Released under the GNU General Public License                                                                        
    Version 0.32.1                                                                                                                                  
                                                                                                                                                    
    DISCLAIMER - USE AT YOUR OWN RISK                                                                                                               
    Please report false positives via https://github.com/Neo23x0/Loki/issues                                                                        
  ```

# Task 10 - Creating Yara rules with yarGen
yarGen

https://github.com/Neo23x0/yarGen

Creation of yara rules from strings found in malware files while removing all benign strings

* Update yarGen
  ```
  python3 yarGen.py --update
  ```
* Generate a yara rule
  ```
  python3 yarGen.py -m file2 --execludegood -o file2.yar
  ```
* Parameters
  * -m - path
  * --excludegood - force to exclude all goodware strings
  * -o location and name
* Resources
  * https://www.nextron-systems.com/2015/02/16/write-simple-sound-yara-rules/
  * https://www.nextron-systems.com/2015/10/17/how-to-write-simple-but-sound-yara-rules-part-2/
  * https://www.nextron-systems.com/2016/04/15/how-to-write-simple-but-sound-yara-rules-part-3/

# Task 11 - Valhalla
