# Room
https://tryhackme.com/room/vulnerabilities101

# Task 1 - Intro
Intro

# Task 2 - Intro to vulnerabilities
* A vulnerability is a weakness or flaw in the design, implementation, or behaviours of a system or application
* Categories of vulnerabilities
    * Operating system
    * Configuration based
    * Weak or default creds
    * App logic
    * Human factors

# Task 3 - Scoring vulnerabilities - CVSS and VPR
* Vulnerabiity management is the process of evaluating, categorizing, and remediating threats
* Vulnerability scoring serves a vital role in vulnerability management
* Popular vulnerability management scoring systems
    * CVSS - Common Vulnerability Scoring System
        * Made up of 5 ratings
            * None - 0
            * Low - 0.1 - 3.9
            * Medium - 4.0 - 6.9
            * High - 7.0 - 8.9
            * Critical - 9.0 - 10.0
        * Complex, requires a calculator to score properly
            * https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator
        * Static in the rating value, doesn't change much if at all
    * VPR - Vulnerabiity Priority Rating
        * Made up of 4 ratings
            * Low - 0.0 - 3.9
            * Medium - 4.0 - 6.9
            * High - 7.0 - 8.9
            * Critical - 9.0 - 10.0
        * Risk driven
        * Rating value is dynamic and scales based on new information and exploitability

# Task 4 - Vulnerability Databases
* Databases that keep track of vulnerabilities
    * NVD - National Vulnerability Database
        * https://nvd.nist.gov/vuln/full-listing
    * Exploit DB
        * https://www.exploit-db.com/
* Terms
    * vulnerability - a weakness or flaw in the design, implementation, or behaviors of a system or app
    * exploit - an action that takes advantage of the vulnerability
    * proof of concept - a technique or tool that demonstrates the exploit

# Task 5 - Finding a vulnerability
* In this example use exploit-db to search for tomcat 9.0

# Task 6 - Exploitation example
* Walk through the exploitation example and answer the challenge question

# Task 7 - Conclusion
Conclusion