# Room
https://tryhackme.com/room/rpnessusredux

# Task 1 - Intro
Nessus is a vulnerablity scanner.  It uses techniques similar to nmap to find and report on vulnerabilities and then presents them in a nice GUI format

Nessus is available from Tenable here:
* https://www.tenable.com/products/nessus

# Task 2 - Installation
Nessus Installation

The installation guide is located here:
https://docs.tenable.com/nessus/Content/GettingStarted.htm

* 1 - Register for a Nessus Essentials account
    * https://www.tenable.com/products/nessus/nessus-essentials

* 2 - Download Nessus for your platform
    * https://www.tenable.com/downloads/nessus?loginAttempted=true

* 3 - Run the installer
    ```
    sudo dpkg -i Nessus-8.13.1-debian6_amd64.deb 
    (Reading database ... 461080 files and directories currently installed.)
    Preparing to unpack Nessus-8.13.1-debian6_amd64.deb ...
    Unpacking nessus (8.13.1) over (8.11.1) ...
    Setting up nessus (8.13.1) ...
    Unpacking Nessus Scanner Core Components...

    - You can start Nessus Scanner by typing /bin/systemctl start nessusd.service
    - Then go to https://kali:8834/ to configure your scanner
    ```
* 4 - Start the service
    ```
    sudo /bin/systemctl start nessusd.service 
    ```

* 5 - Open Nessus in your browser and wait while the software initializes
    * https://localhost:8834/#/

* 6 - In the dialogue select Nessus Essentials, click Continue, enter the Activation Code that was sent to your email

* 7 - Create a username and password

* 8 - Nessus will install plugins and start

* 9 - Eventually you'll be presented with a login screen, login, Nessus is now installed

# Task 3 - Navigation and Scans

* To create a scan, click New Scan
* You can create custom templates in the Policies menu
* Modification of plugins is found through the Plugin Rules menu
* For scans, Host Discovery is a simple scan to see what hosts are alive
* For scans, Basic Network Scan is considered useful for any host
* For scans, the Credentialed Patch Audit allows you to connect to a host and verify patches
* For scans, Web Application Tests are used exclusively for web apps

# Task 4 - Scanning a host

* In a Basic Network scan ...
    * you can use the Schedule option to set a specific time for it to run
    * to select ports, click Discovery and use the Scan Type drop down
    * for lower bandwidth links you can adjust options in the Advanced menu
    * enter a target IP, click Save
    * click the Play button to start the scan

# Task 5 - Scanning a web app

* To launch a web application scan, click New Scan and select Web Application Tests
* Fill out the target IP, select low bandwidth link in Advanced if needed, Save and run it