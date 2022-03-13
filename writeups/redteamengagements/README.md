# room
https://tryhackme.com/room/redteamengagements

# task 1 - intro
* key to success is coordination, planning, and communication
* red team engagements
    * table top
    * adversary emulation
    * physical assessment

# task 2 - define scope and objectives
* key to success - clearly defined client objectives or goals
* set objectives are basis for the rest of the engagement
* how focused is the assessment
* engagement categories
    * general internal network pentest
    * focused adversary emulation
* key to success - well defined scope
* scope will define what you can and cannot do/target
    * short example scope
        * no data exfiltration
        * prod servers off limits
        * 10.20.30.0/24 is out of scope
        * 10.30.40.0/24 is in scope

# task 3 - rules of engagement
* ROE - rules of engagement
* ROE - legally binding outline of the client objectives and scope with details
* first official document of planning process, requires proper authorization
* ROE structure example
    * executive summary
    * purpose
    * references
    * scope
    * definitions
    * rules of engagement and support agreement
    * provisions
    * requirements, restrictions, and authority
    * ground rules
    * resolution of issues / points of contact
    * authorization
    * approval
    * appendix
* resources
    * https://redteam.guide/docs/templates/roe_template/

# task 4 - campaign planning
* campaign planning uses the information aquired and planned from the client objectives and the ROE
* campaign plan example
    * engagement plan
    * operations plan
    * mission plan
    * remediation plan
    * example
        * https://redteam.guide/
        * https://redteam.guide/docs/checklists/red-team-checklist/

# task 5 - engagement documentation
* engagement documentation - where ideas and thoughts of campaign planning are officially documented
* example
    * engagement plan
        * concept of operations
        * resource plan
    * operations plan
        * personnel
        * stopping conditions
        * ROE
        * technical requirements
    * mission plan
        * command playbooks
        * execution times
        * responsibilties
    * remediation plan
        * report
        * remediation consultation

# task 6 - concept of operations
* CONOPS - concept of operations
* CONOPS - details the high level overview of the proceedings of an engagement - compared to a executive summary in a pentest report
* CONOPS servers as a business / client reference
* CONOPS is semi technical / high level
* CONOPS critical components
    * client name
    * service provider
    * timeframe
    * general objectives / phases
    * other training objectives
    * high level tools
    * threat group

# task 7 - resource plan
* resource plan - brief overview of dates, knowledge required, resource requirements
* resource plan should be bulleted
* resource plan example
    * header
        * personnel writing
        * dates
        * customer
    * engagement dates
        * recon dates
        * initial compromise dates
        * post exploitation and persistence dates
        * misc dates
    * knowledge required
        * recon
        * initial compromise
        * post exploitation
    * resource requirements
        * personnel
        * hardware
        * cloud
        * misc

# task 8 - operations plan
* operations plan - flexible documentat that provides specific details of the engagement and actions
* should follow writing scheme of resource plan
* operations plan example
    * header
        * personnel writing
        * dates
        * customer
    * halting / stopping conditions
    * required / assigned personnel
    * specific TTPs and attacks planned
    * communications plan
    * rules of engagement
* resources
    * https://vectr.io/

# task 9 - mission plan
* mission plan - cell specific document that details exact actions to be completed by operators
* mission plan example
    * objectives
    * operators
    * exploits / attacks
    * targets
    * execution plan variations

# task 10 - conclusion
* conclusion