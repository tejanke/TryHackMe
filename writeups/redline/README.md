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