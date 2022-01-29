# room
https://tryhackme.com/room/btredlinejoxr3d

# task 1 - intro
* memory analysis tools
    * volatility
        * https://www.volatilityfoundation.org/
    * redline
        * https://www.fireeye.com/services/freeware/redline.html
* redline allows you to analyze a potentially compromised host through a memory dump

# task 2 - data collection
* collecting data
    * standard collector - minimum data, but quick
    * comprehensive collector - takes an hour, provides full analysis
    * ioc search collector - run data collection against known iocs
* example
    * open redline
    * choose standard collector
    * chose OS
    * edit the script and select items of interest like disk, and network
    * choose an output location for the collector
    * click ok
    * collector is saved to the output location where you can then copy it to the other system and run it or run it on the current system
        * runredlineaudit.bat
    * after running the collector you can analyze the session file with the .mans extension

# task 3 - interface
* after opening your saved session file, you can view all the details of the data collected
* user guide
    * https://www.fireeye.com/content/dam/fireeye-www/services/freeware/ug-redline.pdf

# task 4 - collector analysis
* open the saved session file and analyze it

# task 5 - ioc search collector
* ioc - indicators of compromise - artifacts of potential compromise and host intrusion
* iocs can be hashes: md5, sha1, sha256 or other information such as IPs, domain names, file attributes, and so on
* create ioc files with ioc editor
    * https://www.fireeye.com/services/freeware/ioc-editor.html

# task 6 - ioc search and collector analysis
* use the existing save session file located in the Administrator folder
* create and then apply an ioc definition to this previously saved report
* analyze the report and answer the challenge questions
* use virustotal.com for the missing pieces

# task 7 - endpoint investigation
* use the existing saved session file located on the desktop endpoint investigation folder
* answer questions based on the analysis
* useful sections
    * file system
    * event logs
    * file download history
    * system information

# task 8 - conclusion
* resource guides
    * https://www.fireeye.com/content/dam/fireeye-www/services/freeware/ug-redline.pdf
    * https://www.fireeye.com/content/dam/fireeye-www/services/freeware/ug-ioc-editor.pdf