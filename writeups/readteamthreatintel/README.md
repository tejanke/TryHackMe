# room
https://tryhackme.com/room/redteamthreatintel

# task 1 - intro
* TI - threat intelligence
* CTI - cyber threat intelligence
* TTP - tactics, techniques, and procedures

# task 2 - what is threat intelligence
* CTI - cyber threat intelligence
* IOC - indicators of compromise
* TTP - tactics, techniques, and procedures
* ISAC - information and sharing analysis center
* CTI can be consumed by collecting IOCs and TTPs distributed by ISACs
* defenders use threat intelligence to provide context to the threat landscape
* IOCs are traces left by attackers such as domains, IPs, files, etc

# task 3 - applying threat intel to the red team
* a red team will leverage CTI to aid in aversary emulation
* a red team will often use a threat intelligence platform or framework
    * mitre att&ck
    * tiber-eu
    * ost map
* cyber frameworks collect known TTPs and categorize them
    * for example
        * threat group
        * kill chain phase
        * tactic
        * objective / goal
* after an adversary is identified the goal is to classify and record all TTPs
* TTP leverage is used as a planning technique
* threat intelligence operators can be employed to gather TTPs

# task 4 - tiber-eu framework
* TIBER-EU - threat intelligence-based ethical red teaming
* developed by the european central bank
* centers around the use of threat intelligence
* resources
    * https://www.ecb.europa.eu/pub/pdf/other/ecb.tiber_eu_framework.en.pdf
    * https://www.crest-approved.org/tiber-eu/index.html
    * https://www.fireeye.com/content/dam/fireeye-www/services/pdfs/pf/ms/sb-tiber-eu.pdf

# task 5 - TTP mapping
* map TTPs to a standard cyber kill chain
* to begin, select adversary as target based on
    * target industry
    * employed attack vectors
    * country of origin
    * other factors
* resources
    * https://attack.mitre.org/
    * https://mitre-attack.github.io/attack-navigator/

# task 6 - other red team applications of cti
* CTI can be used for
    * c2 traffic
        * user agents
        * ports, protocols
        * listener profiles
    * malware and tooling
        * iocs
        * behaviors
* a red team can use CTI to identify adversaries traffic and modify their c2 traffic to emulate it

# task 7 - creating a cti campaign
* a threat intel driven campaign will take all knowledge and topics and combine them to create a wll planned and researched campaign
* practical

# task 8 - conclusion
* conclusion