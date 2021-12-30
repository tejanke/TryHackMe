# Room
https://tryhackme.com/room/principlesofsecurity

# Task 1 - Intro
* Defense in depth is the used of multiple varied layers of security to provide a hardened security perimeter

# Task 2 - CIA Triad
* The CIA triad is a continuous cycle with three elements that can overlap
    * C - Confidentiality - protect data from unauthorized access and misuse
    * I - Integrity - ensure that data cannot be modified by unauthorized people
    * A - Availability - provide as much uptime as possible

# Task 3 - Principles of Privileges
* PIM - Privileged Identity Management
    * translate a user's role within an organization to an access role on a system
* PAM - Privileged Access Management
    * management of privileges for an access role on a system, password management, auditing policies, etc
* Principle of Least Privilege
    * privileges given that are only absolutely necessary to perform duties

# Task 4 - Security Models
* Any system or piece of technology storing information is called an information system
* Models
    * Bell-La Padula
        * achieves confidentiality
        * no write down, no read up
        * popular with government and military
    * Biba
        * achieves integrity
        * no write up, no read down
        * used when integrity is more important than confidentiality

# Task 5 - Threat Modeling and Incident Response
* The Threat Modeling Process
    * Prepration
    * Identification
    * Mitigation
    * Review
* Parts of an effective Threat Model
    * Threat intelligence
    * Asset identification
    * Mitigation capabilities
    * Risk assessment
* Frameworks
    * STRIDE
        * Spoofing identity, Tampering with data, Repudiation threats, Information disclosure, Denial of service, Elevation of privileges
    * PASTA
        * Process for Attack Simulation and Threat Analysis
* STRIDE
    * Spoofing - false identification as another, mitigate by authenticating requests
    * Tampering - mitigate with anti-tamper measures, integrity
    * Repudiation - mitigate with logging and tracking
    * Information Disclosure - mitigate by only showing information to the user that needs to see it
    * Denial of Service - prevent with highly available systems and security controls
    * Elevation of Privilege - an attacker can escalte to an unauthorized level, lock down security controls and privileges