# room
https://tryhackme.com/room/redteamfundamentals

# task 1 - intro
* pentests may show vulnerabilities so you can take proactive action but may not teach you how to respond to a security incident

# task 2 - vulnerability assessment and pentest limitations
* vulnerability assessment
    * simplest form of security assessment
    * identity as many vulnerabilties in as many systems as possible
    * assessment machine may be on trusted network
    * scan hosts to identify vulnerabilities
    * not trying to exploit
* pentest
    * adds to vulnerability assessment by exploring the impact of an exploit
    * attempt to exploit, existing controls may reveal it is not possible
    * post exploitation to identify information that can be extracted
* advanced persistent threats
    * pentest differs from a real attack
        * pentests are loud, real attackers hide themselves
        * non-technical attack vectors like social engineering may be overlooked in a pentest
        * during a pentest some security measures might be relaxed, like full scale IR
    * APT - advanced persistent threat
        * highly skilled
        * sponsored by nations or criminal enterprise
        * targets critical infrastructure, financial organizations, and governments

# task 3 - red team engagements
* a red team engagement is a shift from pentesting that allows an organization to test defense and IR
* red team engagements emulate a real threat actor's TTPs - Tactics, Techniques, and Procedures
* red team engagements have clear goals, referred to as crown jewels or flags
* red team engagements usually do not inform the blue team as to keep the response as true as possible
* red team engagements consider
    * technical infrastructure
    * stealth and evasion
    * social engineering
    * physical intrusion
* red team engagement types
    * full engagement - simulate attacker workflow end to end
    * assumed breach - attacker is already in the system using a regular user's creds
    * table top - simulation between red and blue team to discuss scenarios and responses

# task 4 - teams and functions of an engagement
* teams
    * red cell - offensive portion of the engagement
    * blue cell - defenders, internal staff, organization's management
    * white cell - referre that monitors adherence to rules of engagement
* roles
    * red team lead - plans and organizes engagement at high level
    * red team assistant lead - assist team lead, plans and documentation
    * red team operator - executes assignments, interpret and analyze plans
* resources
    * https://redteam.guide/docs/definitions/

# task 5 - engagement structure
* red team core function is adversary emulation
* red team can use cyber kill chains to summarize and assess steps of engagement
* blue team can use cyber kill chains to map behaviors and breakdown adversary movement
* cyber kill chains
    * lockheed martin cyber kill chain
        * https://www.lockheedmartin.com/en-us/capabilities/cyber/cyber-kill-chain.html
    * unified kill chain
        * https://unifiedkillchain.com/
    * varonis cyber kill chain
        * https://www.varonis.com/blog/cyber-kill-chain
    * active directory attack cycle
        * https://github.com/infosecn1nja/AD-Attack-Defense
    * mitre att&ck framework
        * https://attack.mitre.org/

# task 6 - overview of red team engagement
* practical overview

# task 7 - conclusion
* conclusion