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