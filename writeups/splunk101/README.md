# Room
https://tryhackme.com/room/splunk101

# Task 1 - Intro
Splunk is a SIEM used for security as well as data analysis, DevOps, and other fields.  A SIEM is a Security Information and Event Management system, which is software that provides a central location to collect and log data, that data is aggregated and normalized.  It is then made available to be queried by an analyst

SIEMs provide:
* Threat detection
* Investigation
* Time to respond

Other SIEM features include:
* Basic security monitoring
* Advanced threat detection
* Forensics & Incident Response
* Log Collection
* Normalization
* Notifications and Alerts
* Security Incident Detection
* Threat Response Workflows

# Task 2 - Navigating Splunk
http://127.0.0.1:8000

Home screen
* Splunk Bar
  * Messages
  * Settings
  * Activity
  * Help
  * Find
* Apps Panel
  * Search & Reporting
* Explore Splunk

# Task 3 - Splunk Apps
Search & Reporting is a Splunk App and is installed by default.  You can make Search & Reporting the default page by editing the user-prefs.conf file.

Splunk Apps can be installed from a direct download on the Splunk website or through Splunkbase.  Home > Apps > Install app from file

# Task 4 - Adding Data
Splunk can be feed any data in the form of event logs, website logs, firewall logs, etc.  Data sources are grouped into categories.  Home > Add Data > Monitor > Local Event Logs.  Settings > Data Inputs > Local Event Log Collection > Microsoft-Windows-Sysmon/Operational > Save

# Task 5 - Splunk Queries
Practical using the Splunk interface to search for answers to the questions posed in the challenge

Resources
* https://docs.splunk.com/Documentation/Splunk/8.1.2/SearchTutorial/Aboutthesearchapp
* https://docs.splunk.com/Documentation/Splunk/8.1.2/SearchTutorial/Startsearching
* https://docs.splunk.com/Documentation/Splunk/8.1.2/SearchTutorial/Aboutthetimerangepicker
* https://docs.splunk.com/Documentation/Splunk/8.1.2/SearchTutorial/Usefieldstosearch
* https://docs.splunk.com/Documentation/Splunk/8.1.2/SearchTutorial/Usefieldlookups
* https://docs.splunk.com/Documentation/Splunk/8.1.2/SearchTutorial/Searchwithfieldlookups
* https://docs.splunk.com/Documentation/Splunk/8.1.2/Knowledge/AboutSplunkregularexpressions

# Task 6 - Sigma Rules
Sigma is a generic and open signature format that allows you to describe relevant log events in a straightforward manner.  Sigman rules are written in YAML

* https://uncoder.io/
* https://github.com/SigmaHQ/sigma

# Task 7 - Dashboards and Visualizations
Dashboards are panels displaying different data in one view, visualizations allow us to view data in a visual format

Resources
* https://docs.splunk.com/Documentation/Splunk/8.1.2/Viz/WebFramework
* https://docs.splunk.com/Documentation/Splunk/8.1.2/Viz/Aboutthismanual
* https://docs.splunk.com/Documentation/Splunk/8.1.2/Viz/CreateDashboards
* https://docs.splunk.com/Documentation/Splunk/8.1.2/Viz/AddPanels
* https://docs.splunk.com/Documentation/Splunk/8.1.2/SearchTutorial/Createnewdashboard

# Task 8 - Alerts
Alerts

* https://docs.splunk.com/Documentation/SplunkCloud/8.1.2012/Alert/Alertexamples

# Task 9 - Conclusion
Conclusion