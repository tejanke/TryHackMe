# Room
https://tryhackme.com/room/introtoisac

# Task 1 - Intro
ISAC - Information Sharing and Analysis Centers - used to share and exchange various Indicators of Compromise (IOCs) to obtain threat intelligence.  IOCs can include hashes, IPs, YARA rules and more

ISAC examples
* AlienVault OTX
* Threat Connect
* MISP

# Task 2 - Basic Terminology
* APT - Advanced Persistent Threat - a team or group (threat group), or country (nation state), that engages in long term attacks against organizations or countries
  * FireEye list of APT groups
    * https://www.fireeye.com/current-threats/apt-groups.html
* TTP - Tactics, Techniques, and Procedures
  * Tactic - adversary's goal or objective
  * Technique - how the adversary achieves the goal or objective
  * Procedure - how the technique is executed
* TI - Threat Intelligence - overarching term for all collected information on adversaries and TTPs
  * Another similar term is CTI - Cyber Threat Intelligence
* IOCs - Indicators of Compromise - indicators for malware and adversary groups like file hashes, IPs, names, etc

# Task 3 - What is Threat Intelligence
Threat Intelligence AKA TI and CTI, is used to provide information about the threat landscape

Threat Intelligence types
* Strategic - aligned to goals of the organization that helps them make informed decisions with security budgets and strategies
* Tactical - identifies adversary attack patterns by using TTPs and attack models
* Operational - IOCs and how the adversary operates

# Task 4 - What are ISACs
Information Sharing and Analysis Centers (ISACs) are member driven organizations delivering all hazards threat and mitigation information to asset owners and operators.  ISACs can be community driven or vendor specific

https://www.nationalisacs.org/member-isacs

Blue team ISACs
* https://us-cert.cisa.gov/
* https://otx.alienvault.com/
* https://threatconnect.com/
* https://www.misp-project.org/

# Task 5 - Using Threat Connect to create a Threat Intel dashboard
Threat Connect has both free and paid versions.  Threat Connect allows you to create an intelligence dashboard that includes top sources by observations, latest intelligence, top sources by false positives, top tags, indicator breakdowns, and custom tags

https://threatconnect.com/

# Task 6 - Intro to AlienVault OTX
AlienVault OTX is provided by AT&T Cybersecurity and is one of the main ISACs used for threat intelligence.  AlienVault uses Pulses to create trackers for categories.  Pulses can include a variety of IOCs like file hashes, IP addresses, domains, URLS, YARA rules, CVEs, and more

https://otx.alienvault.com/

# Task 7 - Using OTX to gather Threat Intelligence
Pulses can include a variety of IOCs like file hashes, IP addresses, domains, URLS, YARA rules, CVEs, and more.  A majority of Pulses are community created and maintained.  A Pulse contains three sections - description, indicator overview, and indicators themselves

# Task 8 - Creating IOCs
The creation of IOCs is done with tools such as strings, winmd5free, and Mandiant IOC Editor

# Task 9 - Investigation
Use standard Windows information gathering procedures to grab file names and file sizes for the quarantined files in the VM.  Use WinMD5 to grab file hashes